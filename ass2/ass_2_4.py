
def bin_dec():
    val= int(input("enter the binary value : "))
    ans =0
    i=0
    while (val) != 0 :
        a=pow(2,i)
        mod = val%10
        ans=ans+a*mod
        val=val//10
        i=i+1  
    print(ans)

def oct_dec():
    val= int(input("enter the octal value : "))
    ans =0
    i=0
    while (val) != 0 :
        a=pow(8,i)
        mod = val%10
        ans=ans+a*mod
        val=val//10
        i=i+1  
    print(ans)

def hex_dec() :
    print("enter the hexa value : ")
    a= input()
    return int(a,16)
print(bin_dec())
print(oct_dec())
print(hex_dec())


    

