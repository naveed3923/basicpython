#Given a string, return a new string where the first and last chars have been exchanged.



def front_back(str):
    a=str[1:len(str)-1]
    if len(str)<=1:
        return str
    else:
        return(str[-1]+a+str[0])
