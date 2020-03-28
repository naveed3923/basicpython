#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


def string_match(a, b):
    min_len=min(len(a),len(b))
    count=0
    for i in range(0,min_len-1):
        lst1=a[i:i+2]
        lst2=b[i:i+2]
        if lst1==lst2:
            count=count+1
    return count
