import random
keepPlaying = True

print(f"""Welcome to Guess The Number!
Type 'stopgame' anytime to stop the game.

""")

while keepPlaying:
    
    try:
    
        tries = input("How many tries do you want? (1 - 100) —> ")
        if tries.lower() == "stopgame":
            keepPlaying = False
            break
        tries = int(tries)
        if tries < 1 or tries > 100:
            print("Invalid amount. Chose for you. (10)")
            tries = 10
            
        val = input("Max number to guess? (10 - 3000) —> ")
        if val.lower() == "stopgame":
            keepPlaying = False
            break
        val = int(val)
        if val < 10 or val > 3000:
            print("Invalid amount. Chose for you. (100)")
            val = 100
            
        tried = 0
        value = random.randint(1,val)
        
        while True:
            ans = input(f"""
Enter your guess ({tries - tried} tries left) —> """)
            if ans.lower() == "stopgame":
                keepPlaying = False
                break
            
            ans = int(ans)
            if tried >= tries:
                ans2 = input(f"""
You LOST! The number was {value}! Play again? [Y / N] —> """)
                if ans2.lower() == "y":
                    break
                elif ans2.lower() == "n":
                    keepPlaying = False
                    break
            else:
                if ans > value:
                   print("Number is smaller")
                   tried += 1
                elif ans < value:
                    print("Number is bigger")
                    tried += 1
                else:
                    ans2 = input(f"""
You WON! It took you {tried} tries! Play again? [Y / N] —> """)
                    if ans2.lower() == "y":
                        break
                    elif ans2.lower() == "n":
                        keepPlaying = False
                        break
                    
    except ValueError:
        print("""You entered an invalid character. Please try again.
        """)
