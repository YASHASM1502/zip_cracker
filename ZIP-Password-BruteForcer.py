import os
import zipfile
from time import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

banner = '''
 ###################################
 # ZIP Password BruteForcer        #
 ###################################
 # Coded By Sir.4m1R               #
 # The404Hacking                   #
 # Digital Security ReSearch Group #
 # T.me/The404Hacking              #
 ###################################
 GitHub:
 https://github.com/The404Hacking/ZIP-Password-BruteForcer

 [1] Zip Password Cracker
 [0] Exit
'''
print(banner)

a = int(input(" [?] Enter Number : "))

if a == 0:
    cls()
    print(" [!] Good Bye :)")
    quit()

elif a == 1:
    cls()
    textzippass = '''
 #########################################
 # Zip Password Brute Forcer (Top Speed) #
 #########################################
 # The404Hacking                         #
 # Digital Security ReSearch Group       #
 # T.me/The404Hacking                    #
 #########################################
 '''
    print(textzippass)

    file_path = input(" [+] ZIP File Address: ")
    print("")
    word_list = input(" [+] Password List Address: ")

    def main(file_path, word_list):
        try:
            zip_ = zipfile.ZipFile(file_path)
        except zipfile.BadZipFile:
            print(" [!] Please check the file's Path. It doesn't seem to be a ZIP file.")
            quit()

        i = 0
        c_t = time()

        with open(word_list, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                i += 1
                password = line.strip()
                try:
                    zip_.extractall(pwd=password.encode('utf-8'))
                    t_t = time() - c_t
                    print("\n [*] Password Found :)\n" + " [*] Password: " + password + "\n")
                    print(" [***] Took %.2f seconds to crack. That is, %.2f attempts per second." % (t_t, i / t_t))
                    quit()
                except Exception:
                    pass
        print(" [X] Sorry, Password Not Found :(")

    main(file_path, word_list)
