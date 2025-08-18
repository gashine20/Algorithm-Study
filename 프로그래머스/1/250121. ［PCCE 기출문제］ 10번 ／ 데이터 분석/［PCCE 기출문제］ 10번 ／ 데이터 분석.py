def solution(data, ext, val_ext, sort_by):
    by = ["code", "date", "maximum", "remain"]
    filtered_data = list(filter(lambda x : x[by.index(ext)] <= val_ext, data))
    
    return sorted(filtered_data, key = lambda x : x[by.index(sort_by)])