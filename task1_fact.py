a=input("Enter a number: ")
def fact(a):
    if a<2:
        return 1
    else:
        return (fact(a-1)*a)
result=fact(int(a))
print("Factorial of",a ,"is:",result)