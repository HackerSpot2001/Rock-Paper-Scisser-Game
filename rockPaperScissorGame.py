#!/usr/bin/python3
import random

def game():
    gameComponents = ["Rock","Paper","Scissor"]
    while True:
        try:
            print("\n")
            for i in range(len(gameComponents)):
                print(f"{i+1}. {gameComponents[i]}")
            print("e) Exit")
            word = random.choice(gameComponents)
            inp = str(input("> "))
            if inp.capitalize() == word.capitalize():
                print("[+] You Win.....")
            
            if (inp.lower() == "exit") or  inp.lower().startswith("e") :
                break
                
            if inp.lower() != word.lower():
                print("[-] You Loose...")

            if inp.capitalize() not in gameComponents:
                print(f"[-] Please enter Correct input")
        except KeyboardInterrupt:
            exit(0)

game()