def backtrack(s, options):
    if is_s(s):
        process_s(s)
    else:
        for option in options:
            s.append(option)
            if is_valid(s):
                backtrack(s, options)
            s.pop()

# s = solution