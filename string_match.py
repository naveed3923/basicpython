def string_match(a, b):
    min_len=min(len(a),len(b))
    count=0
    for i in range(0,min_len-1):
        lst1=a[i:i+2]
        lst2=b[i:i+2]
        if lst1==lst2:
            count=count+1
    return count
