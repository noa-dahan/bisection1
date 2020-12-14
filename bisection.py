#Noa Dahan, id:208375709
#Ofir Ben Zaken, id:208839712
import sympy as sp
import math

def division(polinom1,a,b,num_Of_Parts,name_f):
    epsi=0.00000001
    roots=[]
    D_jump=float((b - a) / num_Of_Parts)
    for i in range(num_Of_Parts):
        temp1=polinom1(a)
        temp2=polinom1(a+D_jump)
        if temp1*temp2 < 0 :
            print("we found a range where there is an extreme point")
            root= bisection(polinom1,a,a+D_jump, epsi)
            if(root!=False):
                if math.isclose(root, 0.0, abs_tol=0.1):
                    root=0
                if name_f == "div":
                    if (polinom1(round(root,1))==0.0):
                        roots.append(root)
                else:
                    roots.append(root)
        a=a+D_jump
    return roots


def bisection(polinom1,start_point,end_point,epsi):
    Error=math.ceil(-(math.log(epsi / (end_point - start_point), math.e)) / math.log(2, math.e))
    count_iter=0
    flag=True
    m = (start_point + end_point) / 2
    while flag:
        if (polinom1(start_point)* polinom1(m))<0:
            end_point=m
        elif (polinom1(end_point)* polinom1(m))<0:
            start_point = m
        else:
            return False
        count_iter += 1
        m_1 = m
        m = (start_point + end_point) / 2
        if abs(m - m_1) < epsi:
            flag=False
        if count_iter>Error:
            print("The function does not match for bisection method")
            flag = False
            return False
    return m

#main
x =sp.symbols('x')
polinom1=x**4+x**3-3*x**2
start_point=-3
end_point=2

print("example:")
print("The polinom is:",polinom1)
print("The start_point is:",start_point)
print("The end_point is:",end_point)
p_roots=division(lambda x :x**4+x**3-3*(x**2),start_point,end_point,51,'fun')
print(p_roots)
lambda x:x**4+x**3-3*x**2
d_roots=division(lambda x2 :4*(x2**3)+3*(x2**2)-6*x2,start_point,end_point,51,'div')
print("d:",d_roots)