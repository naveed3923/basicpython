#Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(str):
    result=""
    for i in range(0,len(str)):
        result=result+str[0:i+1]
    return result    
