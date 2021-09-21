def solution(e,l):
    a=int(e[:2])
    b=int(e[3:])
    c=int(l[:2])
    d=int(l[3:])
    if b-d<1:
        if c-a==1:
            print(2+3)
        elif c-a>1 and c-a<3:
            print(2+3+4)
        else:
            print(2+3+(c-a)*4)
    if b-d>1:
        #if c-a==1:
         #   print(2+3+4)
        if c-a>1:
            print(2+3+(c+1-a)*4)
 #   print(a,b,c,d)
obj=solution("10:00","13:21")
obj=solution("09:42","11:42")
