import random
def guess(n):
  num= random.randrange(1,n)
  i=5
  print("You got only 5 attempts")
  while i>0:
    guess=int(input(f"Guess a numberfrom 1 to{n}\n"))
    if guess>num:
      print("Too High")
    elif guess<num:
      print("Too Low")
    else :
      print("You Got It");
      break
    i=i-1
  if i==0:
    print("Better Luck Next Time!!")