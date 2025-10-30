def activity_selection(activities):
    activities.sort(key = lambda x:x[1])
    selected = []
    last_end_time = 0
    for start, end in activities:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end
    return selected