import os,sys
from code_3 import encrypt_message
from code_3 import decrypt_message
import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_3.py")
        assert exists == True
    except:
        sys.exit()

def get_caesar_encryption(word,key):
    return "".join( [chr(ord(x)+key) for x in word])

def test_encryption():
    check_if_file_exists()
    words = ["Texas", "Virginia", "Brazil", "ElPaso", "Lisboa"]
    secret = random.choice(words)
    key = random.randint(1,4)
    secret_encrypted ="".join( [chr(ord(x)+key) for x in secret])
    user_encryption = encrypt_message(secret,key)
    assert secret_encrypted == user_encryption

def test_decryption():
    check_if_file_exists()
    words = ["Texas", "Virginia", "Brazil", "ElPaso", "Lisboa"]
    secret = random.choice(words)
    key = random.randint(1,4)
    secret_encrypted ="".join( [chr(ord(x)+key) for x in secret])
    user_decryption = decrypt_message(secret_encrypted,key)
    assert secret == user_decryption

