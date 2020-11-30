# This little and funny program calculate the love score
# of a relationship

# The original post is from buzzfedd and you can find it
# here https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

# Getting user input
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Inizializing the actual code by defing the variables
relazione = name1 + name2
lower_case_relazione = relazione.lower()

t = lower_case_relazione.count("t")
r = lower_case_relazione.count("r")
u = lower_case_relazione.count("u")
e = lower_case_relazione.count("e")
true = t + r + u + e

l = lower_case_relazione.count("l")
o = lower_case_relazione.count("o")
v = lower_case_relazione.count("v")
e = lower_case_relazione.count("e")
love = l + o + v + e

love_score = true + love

# Setting the conditions
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}%, you go together like coke and mentos.")
  #"Your score 10 < x > 90, you go together like coke and mentos."

elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}%, you are alright together")
 #"Your score is 40-50, you are alright together."

else:
  print(f"You score is {love_score}%, you have to know her better")
