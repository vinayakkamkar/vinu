import fibonacci
n=int( input("enter range"))
if(n<0):
    print("enter valied range")
else:
    print("the range is  \n")
    fibonacci.fibonacci(n)
