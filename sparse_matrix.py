class SparseMatrix:
    def __init__(self):
        self.data = {}

    def set(self, row: int, col: int, value: float):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get(self, row: int, col: int) -> float:
        return self.data.get((row, col), 0.0)

    def __str__(self):
        return str(self.data)

def dense_to_sparse(dense_matrix):
    sparse_matrix = SparseMatrix()
    
    for i, row in enumerate(dense_matrix):
        for j, value in enumerate(row):
            if value != 0:
                sparse_matrix.set(i, j, value)
    
    return sparse_matrix

# Example Usage
dense_matrix = [
    [0, 0, 3, 0],
    [4, 0, 0, 5],
    [0, 0, 0, 0],
    [7, 0, 0, 0]
]

sparse_matrix = dense_to_sparse(dense_matrix)
print("Sparse Matrix Representation:", sparse_matrix)
