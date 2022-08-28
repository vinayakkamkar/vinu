try:
 a=int(input("enter value of a"))
 b=int(input("enter value of b"))
 c=a/b
 print("a/b=%d"%c)
except Exception as e:
 print("can't divide by zero")
 print(e)
else:
 print("else block")
