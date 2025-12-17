__import__ 

initiated = True
param = __path__['loc/user/set.crossg']

if initiated == True :
    print('initiated!')
    if param == "null":
        SystemExit
    else:
        new_param = "Internal"
        param = new_param