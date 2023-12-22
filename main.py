import pikepdf
import time
from colorama import Fore

password_file = open("passwords.txt") #write here text file name which contain the passwords 

i = 0
start_time = time.time()
for password in password_file:
    i += 1
    print(Fore.RED+f"\r {i} Password is tested {password.strip()}", end = "") 
    try:
        pikepdf.open("protected_pdf.pdf",password = password.strip("\n"))# "protected_pdf.pdf" this place write your password protected pdf name.
        end_time = time.time()
        print("\n")
        print(Fore.GREEN+ f"password found in {str(end_time-start_time)[:4]} second \nPassword is: ", end = "")
        print(Fore.BLUE+ f" {password}")

        break
    except:
        pass