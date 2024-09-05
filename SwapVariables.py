# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# def Swap(a,b):
#     print("a =", a)
#     print("b =", b)

#     if(a>b):
#         a = a+b
#         b = a-b
#         a = a-b
#         print("a =", a)
#         print("b =", b)

#     else:
#         b = a+b
#         a = b-a
#         b = b-a
#         print("a =", a)
#         print("b =", b)

# print(Swap(a,b))

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

def SwapBit(a,b):

    print("a =", a)
    print("b =", b)

    a = a^b
    b = a^b 
    a = a^b

    print("a =", a)
    print("b =", b)

print(SwapBit(a,b))

