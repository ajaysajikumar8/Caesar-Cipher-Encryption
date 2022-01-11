alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#the encrypting function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #if the direction is decode, then shift number is set to negative, this will cause the new position to decrease
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        #to find the position of current letter
        position = alphabet.index(char)
        #assigning a new position 
        new_position = position + shift_amount
        #entering the alphabet at new position to the end_text 
        end_text += alphabet[new_position]
    else:
        #if there are any spaces, symbols or numbers, the program will not replace that character with a new one. the characters not in the alphabet list will be left as it is
        end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)

#A flag is set, so that the user can run the program as long as he wants. When the user decides to stop the program, the flag is switched thus causing the loop to break. 
flag = True
while(flag):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    choice = input("Type \"yes\" if you want to go again. Otherwise type \"no\": ").lower()
    if choice == "no":
        flag = False
print("Have a good day!")