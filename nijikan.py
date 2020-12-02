x1=float(100)
y1=float(87.5)
x2=float(50)
y2=float(35)
x3=float(-50)
y3=float(0)
def f1(a,b,c):
    return a*x1**2+b*x1+c-y1
def f2(a,b,c):
    return a*x2**2+b*x2+c-y2
def f3(a,b,c):
    return a*x3**2+b*x3+c-y3
f1=0
f2=0 
f3=0
a=((f1-f2)/(x1-x2)-(f2-f3)/(x2-x3)+(y1-y2)/(x1-x2)-(y2-y3)/(x2-x3))*((x1-x2)*(x2-x3))/((x1**2-x2**2)*(x2-x3)-(x2**2-x3**2)*(x1-x2))
b=(f2-f3)/(x2-x3)-a*(x2**2-x3**2)/(x2-x3)+(y2-y3)/(x2-x3)  
c=y1-a*x1**2-b*x1
print("答えはy="+str(a)+"x^2"+str(b)+"x"+str(c))
