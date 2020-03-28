def front_back(str):
    a=str[1:len(str)-1]
    if len(str)<=1:
        return str
    else:
        return(str[-1]+a+str[0])
