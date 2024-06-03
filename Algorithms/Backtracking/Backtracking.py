def backtrack(s, candidates):
    if is_s(s):
        process_s(s)
    else:
        for candidate in candidates:
            s.append(candidate)
            if is_valid(s):
                backtrack(s, candidates)
            s.pop()

# s = solution