from questions import ques

print("\t\t\tScience Quiz\n")
name = input("Enter your name\n")
print(f"Welcome!{name}, Let's Start The Quiz")
score = 0
i = 1
for i in ques:
  print(f"{i}:{ques[i]['Question']}\n")
  print(f"{ques[i]['Options']}\n")
  ans = input("Enter your answer[a/b/c/d]\n")
  if ans == ques[i]['Answer']:
    score = score + 1
i = i + 1
print(f"Your Score:{score}")
