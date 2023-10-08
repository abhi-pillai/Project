from numberguess import guess
print("\t\t\t\tGuess The Number\n") 
mode=input("Enter mode:[E:Easy| M:Medium| D:Difficult\n")
if mode=='E':
  guess(10)
elif mode=='M':
  guess(100)
elif mode=='D':
  guess(1000)
else:
  print("Invalid Selection\n")