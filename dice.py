import random

def roll_dice():
    return random.randint(1, 6)

def main():
    for step in range(1, 6):
        dice1 = roll_dice()
        dice2 = roll_dice()
        
        print(f"Step-{step}: {dice1}:{dice2}")
        
        if dice1 == dice2:
            print(f"Both dice showing {dice1}:{dice2}")
        else:
            print("Condition not met")
        
        print()  # Empty line for separation

if __name__ == "__main__":
    main()
