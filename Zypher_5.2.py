import random
import hashlib
from cryptography.fernet import Fernet
import base64
import time
import webbrowser as w

salt='ZYPHER'

secret_key_prior='ZYPHER{'
secret_key_main='匴倀义刀㕙䌀弱䬀㝔䬀㙃䄀呟刀'   
secret_key_latter='}'


def intro():
    global username
    username=input("Enter your username...")
    time.sleep(2)
    
    print(  "===================================================\n\n")
    
def menu():
    print("Welcome " +"Ryan"+"!\n")
    time.sleep(2)
    print("That's ryt..\n")
    time.sleep(1)
    print("we know who you are and what you're upto")
    time.sleep(3)
    print("what we do not know is, are you really as skilled as you think you're..")
    time.sleep(5)
    print("If you've reached till here, it does indicate that u've some impressive abilities")
    time.sleep(6)
    print("But this one is no cake son...solve this to decipher ur destiny")
    time.sleep(5)
    print("Or shd I say "+salt)
    time.sleep(4)
    print(  "===================================================\n\n")
    
    print(salt+"\n\n\
Menu:\n\
(a) Rabbit\n\
(b) Enter key\n\
(c) Exit ")

    choice = input("What would you like to do, "+ username +" (a/b/c)? ")
    
    if choice=='a':
        url='https://cyscomvit.com/' 
        w.open(url)
    elif choice=='b':
        x=input()
        if key(x):
            print("Key accepted")
            time.sleep(3)
            print("now find the flag and use it to unlock the secret files")
            time.sleep(7)
            print("good luck")
        else:
            print("Key invalid")
    else:
        global loop
        loop=False
        print("Choose stg within the menu kid..")

def encrypt(flag,key):
    enc=''.join([chr((ord(flag[i]) << key) + ord(flag[i + 1]))+chr(ord(salt[random.randint(1, 10)])<<key) for i in range(0, len(flag), 2)])
    print(enc)
    return enc

def decrypt(enc_text,key):
    ...
    #return flag
    #use the flag to unlock file


def key(x):
    if x==hashlib.sha256(salt.encode('utf-8')).hexdigest()[4]:
        return True

#encrypt('FLAG',x)

loop=True

def ui_flow():
    intro()
    if username=='FOX3R':
        while loop:
            menu()   
    else:
        print("Access denied")  
ui_flow()