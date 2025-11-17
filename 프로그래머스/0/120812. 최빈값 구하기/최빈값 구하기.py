def solution(array):
    dict = {}
    count = 0
    num_set = set(array)
    
    for num in num_set:
        dict[num] = array.count(num)
    
    mode_num = max(dict.values())
    mode_arr = [k for k, v in dict.items() if v == mode_num]
    
    if len(mode_arr) > 1:
        return -1
    
    return mode_arr[0]