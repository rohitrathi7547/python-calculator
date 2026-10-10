while True:
 a=int(input("x"))
 b=int(input("y"))
 op=(input("What to do?+,-,*,/,%,^,exit"))
 if op=="exit":
  print("bye bye")
 break
 if op=="+":
  print(a+b)
 elif op=="-":
  print(a-b)
 elif op=="*":
  print(a*b)
 elif op=="/":
  if b== 0:
   print("cannot divide by zero")
 else:
  print(a/b)
 elif op=="%":
  print(a%b)
 elif op=="^":
  print(a**b)
 else:
  print("error")
