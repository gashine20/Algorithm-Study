def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    
    def find_index(s):
        index = 0
        if s == "code":
            index = 0
        elif s == "date":
            index = 1
        elif s == "maximum":
            index = 2
        elif s == "remain":
            index = 3
        return index
    
    
    # filter -> map
    index = find_index(ext)
    filtered_data = list(filter(lambda x : x[index] <= val_ext, data))
    
    # sort
    index2 = find_index(sort_by)
    sorted_data = sorted(filtered_data, key = lambda x : x[index2])
    
    return sorted_data