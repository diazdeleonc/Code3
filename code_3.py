
def encrypt_message(message, key):
   encrypted_secret = ""
   for letter in message:
      encrypted_secret = encrypted_secret + chr((ord(letter)+key))
   return encrypted_secret

def decrypt_message(secret, key):
  decrypted_secret = ""
  for letter in secret:
      decrypted_secret = decrypted_secret + chr((ord(letter)-key))
  return decrypted_secret
   
if __name__ == "__main__": 

   message = "This is a secrete message"
   key = 5
   encrypted = encrypt_message(message, key)
   print(encrypted)
   decrypted = decrypt_message(encrypted, key)
   print(decrypted)