def length_of_longest_substring(s):
    max_length = 0
    n = len(s)

    for start in range(n):
        seen = []
        current_length = 0

        for end in range(start, n):
            if s[end] in seen:
                break
            seen.append(s[end])
            current_length += 1
        
        if current_length > max_length:
            max_length = current_length

    return max_length

result = length_of_longest_substring("abcabcbb")
print(result)  
