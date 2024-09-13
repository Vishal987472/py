# Initialize an empty dictionary to store user information
users = {}

# Function to add a new user
def add_user():
    user_id = input("Enter User ID: ")
    user_name = input("Enter User Name: ")
    while True:
        try:
            user_age = int(input("Enter User Age: "))
            break
        except ValueError:
            print("Invalid age. Please enter a valid age.")
    # Store user information in the dictionary
    users[user_id] = {"Name": user_name, "Age": user_age}
    print("User added successfully!")

# Function to print user details based on ID
def print_user_details():
    user_id = input("Enter User ID to retrieve details: ")
    # Check if user ID exists in the dictionary
    if user_id in users:
        print("User ID:", user_id)
        print("User Name:", users[user_id]["Name"])
        print("User Age:", users[user_id]["Age"])
    else:
        print("User ID not found!")

# Main program
while True:
    print("\n1. Add User")
    print("2. Print User Details")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user()
    elif choice == "2":
        print_user_details()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")