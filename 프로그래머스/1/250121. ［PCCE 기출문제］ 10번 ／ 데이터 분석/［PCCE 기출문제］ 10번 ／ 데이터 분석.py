def solution(data, ext, val_ext, sort_by):
    dic = {'code':0,'date':1,'maximum':2,'remain':3}
    filtered_data = []
    for i in data:
        if i[dic[ext]] <val_ext:
            filtered_data.append(i)
    filtered_data.sort(key=lambda data: data[dic[sort_by]])
    return filtered_data