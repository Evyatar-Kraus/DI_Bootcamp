
#instructions below ↓↓↓

user_input_text = input("Please enter your text:\n")
#while the input isn't decrypt or encrypt keep going
#:= is walrus operator so that it always get the value of input
#then the value is checked if its in the allowed values - encrypt/decrypt
#if not the loop runs again
while (user_setting_choice := input("Do you want to encrypt/decrypt? (Enter encrypt/decrypt)\n").lower()) not in {"encrypt", "decrypt"}:
    pass

user_shift_num = int(input("Please enter your shift num\n"))

#if decrypt is chosen - make the number the opposite to return to before the encryption
#if encryption was with left shift (-3 for example) to decrypt we will shift right 3
#so the user inserts the same shift num like 3 with the same plus/minus sign on both encrypt and decrypt
if user_setting_choice == 'decrypt' :
    user_shift_num = user_shift_num * -1

caesar_chars_list = []
for char in list(user_input_text):
    caesar_chars_list.append(chr( int(ord(char)) + user_shift_num)) #ord turns number to its ascii number val - than we change the num
    #with the shift and with chr we make that new ascii value into the char at that value

caesar_text =  ''.join(caesar_chars_list)
print(caesar_text)


# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced
# by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would
# become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
# Create a python program that encrypts and decrypts messages with caesar
# cypher, the user entries the program, and then the program asks him
# if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

# Hint:
# for letter in text:
#     cypher_text += chr(ord(letter) + 3)
