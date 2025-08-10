import os


def newuser_signup():
    print("<o><o><o><o><o> SIGN UP <o><o><o><o><o>")
    user_name = input("Enter Newuser_Name: ")
    password = input("Enter Password: ") 

    if not strong_pswrd_check(password):
        print("Signup failed")
    else:
        print("Signup success")
        print("Now sign in to login")
        with open("user.txt", "a") as file:
            file.write(user_name + "," + password + "\n")


def strong_pswrd_check(p):
    special_symbol = "@#$%^&*()_-"  #its in string 
    if len(p) < 6:
        print("Create password with minimum 6 characters")
        return False

    for value in special_symbol:  #taking one one value from sp symbol  by use of for loop
        if value in p:
            return True

    print("Password must contain at least one special symbol")
    return False


def login():
    print("<o><o><o><o><o> LOGIN <o><o><o><o><o>")
    user_name = input("Enter user_name: ")
    password = input("Enter password: ")

    if not os.path.exists("user.txt"):
        print("Data not found. Please sign up first.")
        return False

    file = open("user.txt", "r")
    for each_line in file:
        line = each_line.strip()#line in file modifying it to without space and new line
        if "," in line:
            stored_user, stored_pass = line.split(",") #modified line dividinv it into  section by comma and later storing in two different variables
            if stored_user == user_name and stored_pass == password: #according to stored variable are matched with new entry 
                print("Login success")
                file.close()
                return True
    file.close()
    print("Login failed. Username or password is incorrect.")
    return False



def add_product():
    print("Add Product To Stock:")
    p_name = input("Enter Product Name/ID: ")
    p_quantity = input("Enter Quantity: ")
    p_net_wt = input("Enter Net Weight: ")
    stone_wt = input("Enter Stone Weight: ")
    p_gross_wt = str(float(p_net_wt) + float(stone_wt))

    with open("stock.txt", "a") as file:# append mode due to storing before data to new data or before data file not found then create its own new file
        file.write(p_name + " , " + p_quantity + " , " + p_net_wt + " , " + stone_wt + " , " + p_gross_wt + "\n")
    print("Product Added Successfully")


def view_stock():
    print("<o><o><o><o><o> STOCK <o><o><o><o><o>")

    if not os.path.exists("stock.txt"):
        print("No stock found. Please add stock first.")
        return

    file = open("stock.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("Stock is empty.")
        return

    print("SI_NO | Product        | Qty | Net Wt | Stone Wt | Gross Wt")
    print("-----------------------------------------------------------")

    SI_NO = 1
    for data in lines:
        index = data.strip().split(" , ")
        if len(index) == 5:
            print(str(SI_NO) + "     | " + index[0] + "             | " + index[1] + "   | " + index[2] + "     | " + index[3] + "       | " + index[4])
            SI_NO += 1
        

def main():
    while True:
        print("\n<><><><><><> GOLD SHOP MANAGEMENT SYSTEM <><><><><><>")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            newuser_signup()

        elif choice == "2":
            if login():
                while True:
                    print("\nSTOCK MENU")
                    print("1. Add Product")
                    print("2. View Stock")
                    print("3. Logout")
                    stock_choice = input("Enter your choice (1-3): ")

                    if stock_choice == "1":
                        add_product()
                    elif stock_choice == "2":
                        view_stock()
                    elif stock_choice == "3":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == "3":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2 or 3.")


main()
