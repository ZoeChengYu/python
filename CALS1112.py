def f(s:str):
    if len(s)==1:
        return s
    else:
        for i in range(len(s)):
            x=s[i]
            y=s[:i]+s[i+1:]
            print( x+f(y))

