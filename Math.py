import random
prob=int(input("Number of problems you'll solve for the day?"))
while prob>0:
  num1=random.randrange(1,50)
  num2=random.randrange(1,50)
  op=random.randrange(1,5)  #returns number from 1 to 4
  if(op==1):
    sum=num1+num2
    ans=int(input(f"{num1} + {num2} = "))
    if(ans==sum):
      print("Bravo! You got it right")
    else:
      print(f"Wrong answer.Answer is {sum}")
  if(op==2):
    diff=num1-num2
    ans=int(input(f"{num1} - {num2} = "))
    if(ans==diff):
      print("Bravo! You got it right")
    else:
      print(f"Wrong answer.Answer is {diff}")
  if(op==3):
    product=num1*num2
    ans=int(input(f"{num1} x {num2} = "))
    if(ans==product):
      print("Bravo! You got it right")
    else:
      print(f"Wrong answer.Answer is {product}")
  if(op==4):
    div=(num1*1.0)/num2
    ans=float(input(f"{num1} / {num2} = "))
    if(ans==div):
      print("Bravo! You got it right")
    else:
      print(f"Wrong answer.Answer is {div}")
  prob=prob-1