def recursion(n):
 if(n<1):
    print("factorial not possible")
 elif(n>1):
    return n*recursion(n-1)
 else:
    return 1
n=int(input("enter number:"))
print("factorial of given number is",recursion(n))
