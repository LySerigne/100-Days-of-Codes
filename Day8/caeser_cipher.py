
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''
    if direction == 'decode':
        shift_amount *= -1
        # There are different way of doing this
        # For instance if shift = 7, then 7 * (-1) = -7 and so on

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")

    # A touch of art to make it prettier
from art import logo
print(logo)

# This allow the user to keep giving input without having to run the program again
active = True
while active:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # This will prevent the code to break if the shifted amount is greater than the number of letter in the alphabet
    shift = shift % 26

    caeser(start_text=text, shift_amount=shift, cipher_direction=direction) 

    result = input("Type 'yes' if you want to keep going or 'no' when you're done: ")
    if result == 'no':
        active = False
        print("Goodbye")

    
