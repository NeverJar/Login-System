import os
import json
import getpass
import pyfiglet
from hashlib import sha256
from pystyle import Colorate, Colors, Center, Box

def cls():
    os.system("cls" if os.name == "nt" else "clear")

class _base: 
    def login():
        cls()
        username = input("USER $> ")
        password = getpass.getpass("PASS $> ")
        hash = sha256(password.encode("utf8")).hexdigest()
        
        with open("db.json", "r") as f:
            data = json.load(f)

        if username not in data["usernames"]:
            print("Invalid Username")
            input()
            exit()
        
        if hash != data[username]["password"]:
            print("Invalid Password")
            input()
            exit()
        
        print("Logged in as %s" % username)
        input()
        exit()

    def register():
        cls()
        username = input("USER $> ")

        with open("db.json", "r") as f:
            data = json.load(f)
        
        if username in data["usernames"]:
            print("Username already registered")
            input()
            exit()
            
        password = getpass.getpass("PASS $> ")
        hash = sha256(password.encode("utf8")).hexdigest()

        data[username] = {"password": hash}
        data["usernames"].append(username)
        
        with open("db.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Successfully registered")
        input()
        exit()

    def menu():
        cls()
        print(Center.XCenter(Colorate.Horizontal(Colors.blue_to_purple, pyfiglet.figlet_format("Login System"))))
        print(Center.XCenter(Colorate.Horizontal(Colors.blue_to_purple, Box.SimpleCube("[1] Login \n[2] Register \n[3] Exit"))))
        choice = input("$> ")

        if choice == "1":
            _base.login()
        elif choice == "2":
            _base.register()
        elif choice == "3":
            exit()
        else:
            print(Center.XCenter(Colorate.Horizontal(Colors.blue_to_purple, "Invalid Input")))
            input()
            exit()

if __name__ == "__main__":
    _base.menu()
