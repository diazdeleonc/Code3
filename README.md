## CODE4-Caesar-Cipher-Encryption-and-Decryption

## Instructions

In this CODE assignment, you will program a Caesar Cipher. The Caesar Cipher is one of the oldest mechanisms to hide secrets. The cipher relies on substitution to encrypt and decrypt information. In this assignment, we are asked to encrypt and encrypt information using the underlying logic of the Caesar Cipher.

There are three elements in a Caesar Cipher:

1. Secret: word to encrypt
2. Key: number of characters by which the word will change
3. Encrypted message: the message that has been encrypted

### Implementing the solution using customized functions

To code the Caesar Cipher, you are asked to code the following two functions:

* `encrypt_message(message,key)`
  + The function receives the message and key for encrypting the secret and returns the encrypted message.
* `decrypt_message(secret,key)`
  +  The function receives the secret and the key to return the original message.

### Some useful functions and tips

* `ord()` function returns the numerical ASCII value of a character
  + To change the value of a letter, you might want to execute `ord(letter)+value`
* `chr()` function return the character value from an ASCII value
  + For example, if you have changed a letter value, you can use chr() to return the character: `chr(ord(letter)+value)`
* `for letter in word:` is a for loop that will allow you to traverse each character of a text
* You will have to concatenate all new values of encryption or decryption
  + A easy way to concatenate characters in a new word is: `new_word = new_word + new_character`
  + In your code, you might want something like the following `new_word = new_word + chr(ord(letter)+value)`

## Create your user prompts

In this code assignment, you can create any user prompt. The automated testing will check only the following the results of the following two functions:

* encrypt_message
* decrypt_message

You **must code your user prompts inside** `if __name__ == "__main__":`
