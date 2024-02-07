

# Python program to convert decimal into other number systems
i=0 
while i<5:
    print("enter the value")
    dec = int(input())
    print("The decimal value of", dec, "is:")
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.")
    i=i+1
