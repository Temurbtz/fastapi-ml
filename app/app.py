from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import List, Dict, Union
import spacy
import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
import os

load_dotenv()

sentry_dsn = os.getenv("SENTRY_DSN")

sentry_sdk.init(
    dsn=sentry_dsn,
    traces_sample_rate=1.0,
    _experiments={
        "continuous_profiling_auto_start": True,
    },
)

ner_model = spacy.load("ner_model/output/model-best")
text_class_model = spacy.load("text_classification/output/model-best")

app = FastAPI()
app.add_middleware(SentryAsgiMiddleware)

ner_cache: Dict[str, List[Dict[str, Union[str, int]]]] = {}
class_cache: Dict[str, Dict[str, Union[str, float]]] = {}

class TextRequest(BaseModel):
    texts: List[str]

class EntityResponse(BaseModel):
    text: str
    label: str
    start: int
    end: int

class ClassificationResponse(BaseModel):
    label: str
    score: float

class CombinedResponse(BaseModel):
    entities: List[EntityResponse]
    classification: ClassificationResponse

@app.get("/")
async def root():
    return {"message": "NER and Text Classification API is up and running"}

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0  # This will raise an exception

@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    sentry_sdk.capture_exception(exc)  
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    sentry_sdk.capture_exception(exc)  
    return JSONResponse(
        status_code=422,
        content={"message": "Validation Error", "errors": exc.errors()},
    )

@app.post("/ner", response_model=Dict[str, List[EntityResponse]])
async def predict_ner(request: TextRequest):
    responses = {}
    for text in request.texts:
        if text in ner_cache:
            responses[text] = ner_cache[text]
        else:
            try:
                doc = ner_model(text)
                entities = [
                    {"text": ent.text, "label": ent.label_, "start": ent.start_char, "end": ent.end_char}
                    for ent in doc.ents
                ]
                ner_cache[text] = entities
                responses[text] = entities
            except Exception as e:
                sentry_sdk.capture_exception(e) 
                responses[text] = []  
    return responses

@app.post("/classify", response_model=Dict[str, ClassificationResponse])
async def predict_classification(request: TextRequest):
    responses = {}
    for text in request.texts:
        if text in class_cache:
            responses[text] = class_cache[text]
        else:
            try:
                doc = text_class_model(text)
                top_label = max(doc.cats, key=doc.cats.get)
                top_score = doc.cats[top_label]
                classification = {"label": top_label, "score": top_score}
                
                class_cache[text] = classification
                responses[text] = classification
            except Exception as e:
                sentry_sdk.capture_exception(e) 
                responses[text] = {"label": "error", "score": 0.0} 
    return responses
