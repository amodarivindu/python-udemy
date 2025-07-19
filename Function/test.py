def get_data(values):
    data = {
        'Date': '2020/06/06',
        'Score': max(values),
        'Grade': 'B1'
    }
    
    return data
x = [87, 99, 85, 23]
results = get_data(x)
print( "the result is: ", results)