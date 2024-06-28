data = {1001: ['vikas', 'Vikas123', 5000],
        1002: ['Sandyy', 'Ashish234', 100]}
class ATM:
    def login(self):
        acc_no = int(input('enter your account number: '))
        password = input('enter your Password: ')
        if acc_no in data.keys() and password == data[acc_no][1]:
            print("Login Successfully :")
            while True:
                print("1.Check Balance \n2.Credit \n3.Withdrawal \n4.Password Change\n5.Details \n6.Logout! ")

                choice = int(input())
                if choice == 1:
                    print(f"Your Account balance is {data[acc_no][2]}\n\n")
                elif choice == 2:
                    credit = int(input('enter your credit amount: '))
                    data[acc_no][2] = data[acc_no][2] + credit
                    print(f"{credit} Rupees credited successfully !\n\n")
                elif choice == 3:
                    withdrawal = int(input('Enter Withdrawal Amount: '))
                    data[acc_no][2] = data[acc_no][2] - withdrawal
                    print(f"Your current balance is {data[acc_no][2]}\n\n")
                elif choice == 4:
                    while True:

                        old_password = input('Please enter your old password : ')
                        if old_password == data[acc_no][1]:
                            print('''Your password should contain\n1.Minimum length should be 8 \n2.Minimum 1 character should be lower \n3.Minimum 1 character should be Upper \n4.Minimum 1 number should be there''')
                            while True:
                            
                                new_password = input('Enter your new password: ')
                                upper = False
                                lower = False
                                number = False
                                for i in new_password:
                                    if i.isupper():
                                        upper = True
                                for i in new_password:
                                    if i.islower():
                                        lower = True
                                for i in new_password:
                                    if i.isdigit():
                                        number = True
                                if upper and lower and number and len(new_password) >= 8:
                                    while True:
                                        confirm_password = input('Retype your new password ! ')
                                        if new_password == confirm_password:
                                            print("Your Password changed Successfully :")
                                            data[acc_no][1] = new_password
                                            break
                                            
                                        else:
                                            print("Password Confirm wrong:")
                                    break
                                else:
                                    print("Please enter validing password ")
                            break
                                
                              
                            
                        else:
                            print("Wrong Old password !")
                            print("Try Again!")
                    else:
                        print("Incorrect Password ! ")

                elif choice == 5:
                    print(f"1.Name = {data[acc_no][0]}\n2.Password = {data[acc_no][1]}\n3.Balance = {data[acc_no][2]} \n\n")
                elif choice == 6:
                    print("Your Account is logged out.")
                    break
                else:
                    print("Invalid choice!")

        else:
            print("You are not allowed to Login !!!")

    def signup(self):
        name = input("Enter your name : ")
        print('''Your password should contain\n1.Minimum length should be 8 \n2.Minimum 1 character should be lower \n3.Minimum 1 character should be Upper \n4.Minimum 1 number should be there''')
        while True:
            password = input('Enter your  password: ')
            upper = False
            lower = False
            number = False
            for i in password:
                if i.isupper():
                    upper = True
                if i.islower():
                    lower = True
                if i.isdigit():
                    number = True
            if upper and lower and number and len(password) >= 8:
                new_account = list(data.keys())[-1] + 1
                balance = float(input('Enter your Balance: '))
                
                data[new_account] = [name, password, balance]
                print(f"Your Account Number is {new_account}")
                print("Account Created Successfully  ")
                break
            else:
                print("Your password is not following the rules!")
                print("Try again ")
    def forgot_password(self):

        acc_no_=int(input('Enter your Account number : '))
        name_=input('Enter your name: ')
        
        if acc_no_ in list(data.keys()) and name_ == data[acc_no_][0]:
            
            print("Your Details are correct ! ")
            while True:
                paas=input('Enter your new password : ')
            
                upper = False
                lower = False
                number = False
                for i in paas:
                    if i.isupper():
                        upper = True
                for i in paas:
                    if i.islower():
                        lower = True
                for i in paas:
                    if i.isdigit():
                        number = True
                if upper and lower and number and len(paas) >= 8:
                    while True:
                        confirm_password = input('Retype your new password ! ')
                        if paas == confirm_password:
                            print("Your Password changed Successfully :")
                            data[acc_no_][1] = paas
                            break
                        else:
                            print("Password confirm wrong: ")
                    break
                else:
                    print('Enter validing password ! ')

a = ATM()
while True:
    print("1.For Login\n2.For Signup\n3.For Forgot Password\n4.Exit")

    log_signup = int(input())
    if log_signup == 1:
        a.login()
    elif log_signup == 2:
        a.signup()
    elif log_signup == 3:
        a.forgot_password()
    elif log_signup==4:
        print("Thankyou for using our services ! ")
        break


