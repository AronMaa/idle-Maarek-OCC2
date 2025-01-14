import time

class IdlePigGame:
    def __init__(self):
        self.bacons = 0
        self.pigs = 1
        self.pig_earning_rate = 1  # bacons earned per second per pig
        self.upgrade_cost = 50
        self.pig_cost = 20

    def display_status(self):
        print(f"\nBacons: {self.bacons}")
        print(f"Pigs: {self.pigs}")
        print(f"Earnings per second: {self.pigs * self.pig_earning_rate} bacons")
        print("1. Buy a new pig (20 bacons)")
        print("2. Upgrade pig earning rate (50 bacons)")
        print("3. Wait and earn bacons")
        print("4. Exit game")

    def buy_pig(self):
        if self.bacons >= self.pig_cost:
            self.bacons -= self.pig_cost
            self.pigs += 1
            print("You bought a new pig!")
        else:
            print("Not enough bacons to buy a pig.")

    def upgrade_pigs(self):
        if self.bacons >= self.upgrade_cost:
            self.bacons -= self.upgrade_cost
            self.pig_earning_rate += 1
            print("Pig earning rate upgraded!")
        else:
            print("Not enough bacons to upgrade.")

    def earn_bacons(self, seconds):
        self.bacons += self.pigs * self.pig_earning_rate * seconds

    def play(self):
        print("Welcome to the Idle Pig Game!")
        print("Your pigs will earn bacons for you. Buy more pigs or upgrade them to earn faster!\n")
        last_time = time.time()
        while True:
            self.display_status()
            choice = input("What would you like to do? (Enter 1, 2, 3, or 4): ")

            # Calculate earnings since last action
            current_time = time.time()
            elapsed_time = int(current_time - last_time)
            self.earn_bacons(elapsed_time)
            last_time = current_time

            if choice == "1":
                self.buy_pig()
            elif choice == "2":
                self.upgrade_pigs()
            elif choice == "3":
                print("Waiting... (bacons will accumulate)")
                time.sleep(5)  # Simulate idle time
            elif choice == "4":
                print("Thanks for playing! See you next time!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    game = IdlePigGame()
    game.play()


if __name__ == "__main__":
    main()
