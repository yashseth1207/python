class complex:
    def __init__(self,a,b) :
        self.real= a
        self.imag=b

print("enter 1st complex no : ")
val= int(input("enter the real value : "))
val1= int(input("enter the imag value : "))
one=complex(val,val1)

print("enter 2nd complex no : ")
val= int(input("enter the real value : "))
val1= int(input("enter the imag value : "))
two=complex(val,val1)

print("enter 3rd complex no : ")
val= int(input("enter the real value : "))
val1= int(input("enter the imag value : "))
three=complex(val,val1)

print("enter 4th complex no : ")
val= int(input("enter the real value : "))
val1= int(input("enter the imag value : "))
four=complex(val,val1)

print("enter 5th complex no : ")
val= int(input("enter the real value : "))
val1= int(input("enter the imag value : "))
five=complex(val,val1)

val= one.real+two.real+three.real+four.real+five.real
val1= one.imag+two.imag+three.imag+four.imag+five.imag
ans = complex(val,val1)
print(ans.real,"+",ans.imag,"i",sep="")