###An empty function, maximum(), is provided for you. Your goal is to implement it so that it returns the maximum value in the values list that is given as argument.

test_values = [4, 3, 5, 6, 2, 1]

def maximum(values):
    answer = None
    for value in values:
        if answer == None or answer < value:
            answer = value
    return answer
max_value = maximum(test_values)