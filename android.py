# ==============================================
# android.py
# Simple Android information app (CLI version)
# Author: Your Name
# For GitHub project
# ==============================================

class AndroidPhone:
    def __init__(self, brand, model, storage, android_version, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.android_version = android_version
        self.price = price

    def info(self):
        print("====================================")
        print("        🤖 Android Information       ")
        print("====================================")
        print(f"Brand:         {self.brand}")
        print(f"Model:         {self.model}")
        print(f"Storage:       {self.storage}")
        print(f"Android Ver:   {self.android_version}")
        print(f"Price:         ${self.price}")
        print("====================================")


def main():
    print("Welcome to android.py!")
    print("Choose an Android phone:\n")

    phones = {
        "1": AndroidPhone("Samsung", "Galaxy S23 Ultra", "512GB", "Android 14", 1299),
        "2": AndroidPhone("Google", "Pixel 8 Pro", "256GB", "Android 14", 999),
        "3": AndroidPhone("Xiaomi", "Mi 13", "128GB", "Android 13", 699),
        "4": AndroidPhone("OnePlus", "11", "256GB", "Android 14", 799),
    }

    for key in phones:
        print(f"{key}. {phones[key].brand} {phones[key].model}")

    choice = input("\nEnter number: ")

    if choice in phones:
        phones[choice].info()
    else:
        print("❌ Wrong selection!")

if __name__ == "__main__":
    main()
