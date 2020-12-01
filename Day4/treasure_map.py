# 🚨 Don't change the code below 👇
row1 = ["🎁","🎁","🎁"]
row2 = ["🎁","🎁","🎁"]
row3 = ["🎁","🎁","🎁"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#This allows the input to be 
horizontal = int(position[0])
vertical = int(position[1])

#selected_row = map[vertical -1]
#selected_row[horizontal] = "X"

# The following code is more concise and have the same meaning
map[vertical -1][horizontal] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
