def main(n:int):
    n=abs(n) if n!=0 else 1
    halfDiamond=[]
    for i in range((n+1)//2):
        spaces=((n//2))-i
        halfDiamond.append((" "*spaces)+"*"+("*"*2*i))
        print(halfDiamond[i])
    mid=len(halfDiamond)-1 if n%2==0 else len(halfDiamond)-2
    for i in range(mid,-1,-1):
        print(halfDiamond[i])
    print("f")
if __name__=="__main__":
    ans=[1,4,5,-2]
    for a in ans:
        main(a)