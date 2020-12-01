import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(",")
# Fun fact: I've spent a lot of time figuring out why it wasn't working
# then I realized that I've made an extra space in .spli(" , ")

#Write your code below this line 👇
#x = len(names)
#random_payer = random.randint(0, x - 1)
#print(random_payer)
#payer = names[random_payer]
payer = random.choice(names)
print(payer+ " is going to pay the bill")
