class complex:
    def __init__(self,a,b) :
        self.real= a
        self.imag=b
    def output(self):
        print(self.real,"+",self.imag,"i",sep="")


a=10
b=0
yash=complex(a,b)
print("1st no")
yash.output()

a=5
b=-2
yash=complex(a,b)
print("2nd no")
yash.output()

a=3.5
b=6.4
yash=complex(a,b)
print("3rd no")
yash.output()

a=-6
b=7.2
yash=complex(a,b)
print("4th no")
yash.output()

a=10
b=0
yash=complex(a,b)
print("5th no")
yash.output()
