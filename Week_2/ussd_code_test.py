# USSD Interface Simulation

# 1. Welcome screen with Nigerian greeting
print("=== Welcome to Naija Mobile Service ===")
print("Good day! How you dey?")

# 2. Ask user to "dial" a USSD code
ussd_code = input("Please dial your USSD code (e.g., *123#): ")

# 3. Print menu with newline formatting
print("\nMenu:")
print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# 4. Ask user to choose an option
choice = input("Select an option (1, 2, or 3): ")

# 5. Display confirmation using f-strings
print(f"\nYou selected option {choice}.")

# 6. Ask for an amount if applicable
if choice in ["2", "3"]:  # For airtime or data purchase
    amount = float(input("Enter amount (₦): "))
    # 7. Final message
    if choice == "2":
        print(f"₦{amount} airtime purchase successful. Thank you for using Naija Mobile!")
    else:
        print(f"₦{amount} data purchase successful. Thank you for using Naija Mobile!")

elif choice == "1":
    print("Your account balance is ₦1,500. Enjoy your day!")

else:
    print("Invalid option. Please try again.")
