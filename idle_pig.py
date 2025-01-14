import time

class IdlePigGame:
    def __init__(self):
        self.coins = 0
        self.pigs = 1
        self.pig_earning_rate = 1  # Coins earned per second per pig
        self.upgrade_cost = 50
        self.pig_cost = 20

    def display_status(self):
        print(f"\nCoins: {self.coins}")
        print(f"Pigs: {self.pigs}")
        print(f"Earnings per second: {self.pigs * self.pig_earning_rate} coins")
        print("1. Buy a new pig (20 coins)")
        print("2. Upgrade pig earning rate (50 coins)")
        print("3. Wait and earn coins")
        print("4. Exit game")

    def buy_pig(self):
        if self.coins >= self.pig_cost:
            self.coins -= self.pig_cost
            self.pigs += 1
            print("You bought a new pig!")
        else:
            print("Not enough coins to buy a pig.")

    def upgrade_pigs(self):
        if self.coins >= self.upgrade_cost:
            self.coins -= self.upgrade_cost
            self.pig_earning_rate += 1
            print("Pig earning rate upgraded!")
        else:
            print("Not enough coins to upgrade.")

    def earn_coins(self, seconds):
        self.coins += self.pigs * self.pig_earning_rate * seconds

    def play(self):
        print("Welcome to the Idle Pig Game!")
        print("Your pigs will earn coins for you. Buy more pigs or upgrade them to earn faster!\n")
        last_time = time.time()
        while True:
            self.display_status()
            choice = input("What would you like to do? (Enter 1, 2, 3, or 4): ")

            # Calculate earnings since last action
            current_time = time.time()
            elapsed_time = int(current_time - last_time)
            self.earn_coins(elapsed_time)
            last_time = current_time

            if choice == "1":
                self.buy_pig()
            elif choice == "2":
                self.upgrade_pigs()
            elif choice == "3":
                print("Waiting... (coins will accumulate)")
                time.sleep(5)  # Simulate idle time
            elif choice == "4":
                print("Thanks for playing! See you next time!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
