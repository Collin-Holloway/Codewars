#Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

    #S is misinterpreted as 5
    # is misinterpreted as 0
    #I is misinterpreted as 1
def correct(string):
    mis = {"0":"O", "5":"S", "1":"I"}
    for c in string:
        if c in mis:
            string = string.replace(c, mis[c])
    return string