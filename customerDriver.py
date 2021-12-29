#B1901850
#13/4/2020
from customerApp import *

def menu():
    print("Telco Subscription by Private Telco")
    print("--------------------------------------------------------------")
    print("1 Add a customer")
    print("2 Display all customers")
    print("3 Display total value of all postpaid subscription")
    print("4 List number of customer in a particular group")
    print("5 Display customers with user-specified postpaid plan")
    print("6 Display customer with the most internet data in his/her plan")
    print("7 Remove customer, based on index")
    print("8 Read customer information from file")
    print("9 Write customer information to file")
    print("0 Quit")
    print(" ")
    
def main():
    
    groupName= input("Enter group's name:")
    newgroup = CustomerGroup(groupName)

    menu()
    
    choice = input("Your choice?")

    #while loop below will continue to loop through and ask for input of choice until the input value is 0
    while choice != "0":

        if choice == "1":
            customerName=input("Customer name?")
            customerAge=int(input("Customer age?"))
            #if statement below is checking whether the customer's age falls between 18 and 70
            if customerAge < 18 or customerAge > 70:
                print("The customer's age must be between 18 and 70.")

            else:  
                customerPlan=input("Postpaid plan('SP/AP/PP')?")
                
                options = ['sp','SP','ap','AP','pp','PP']

                #The customer will be asked to input a plan again and again in the while loop below until the value is valid(value is in the 'options' list)
                while customerPlan not in options:
                    print("Invalid type! Please enter again!")
                    customerPlan=input("Postpaid plan('SP/AP/PP')?")

                customerFee=int(input("Postpaid fee?"))

                #The customer will be asked to input a fee again and again in the while loop below until the value is greater than 0
                while customerFee <= 0:
                    print("Invalid value! Please enter again!")
                    customerFee=int(input("Postpaid fee?"))

                newgroup.addcustomer(Customer(customerName,customerAge,customerPlan,customerFee))

                print("... Customer has been added successfully.")

        elif choice == "2":
            #if statement below will check whether the list is currently empty or not 
            if len(newgroup.getcustomers()) == 0:
                print("No customer registered in this group")

            else:
                print("All customers in this group:")
                print(newgroup.displayCustomer())

        elif choice == "3":
            feetotal, datatotal=newgroup.totalValue()
            print("Total value of all postpaid subscription is " + "RM"+str(feetotal)+" and total internet data "+str(datatotal)+"GB")
            
        elif choice == "4":
            groupName= input("Enter group name:")        
            numbofcustom =newgroup.noOfCustomer()
            print("Total customer in group "+"'"+groupName+"'"+":"+" "+str(numbofcustom))

        elif choice == "5":
            customerPlan=input("Postpaid plan('SP/AP/PP')?")
            #the if and elif statements will allow strings to be printed depending on the plan that the user searched
            if customerPlan.lower() == "sp":
                print("Customer with saver plan:")

            elif customerPlan.lower() == "ap":
                print("Customer with advanced plan:")
            
            elif customerPlan.lower() == "pp":
                print("Customer with premium plan:")

            print(newgroup.findCustomerByType(customerPlan))

        elif choice == "6":
            print("Customer with the highest internet data:")
            print(newgroup.highestvalue())

        elif choice == "7":
            #if statement below will check whether the list is currently empty or not
            if len(newgroup.getcustomers()) == 0:
                print("No customer registered in this group")

            else:
                positiontodelete=int(input("Which customer to withdraw?"))
                validcheck=newgroup.customerWithdraw(positiontodelete)
                #if statement below will check whether False is returned from the customerWithdraw method
                if validcheck == False:
                    print("Invalid index. Try again!")

                else:
                    #The deleted customer will be displayed in a concatenated string if the deleted value is returned
                    print("Customer with index "+str(positiontodelete)+":"+"{"+validcheck+"}"+" has been removed!")   
                
        elif choice == "8":
            nameoffile = input("Please enter filename to load from:")
            newgroup.loadFromFile(nameoffile)
            print("File loaded successfully")

        elif choice == "9":
            nameoffile = input("Please enter filename to save to:")
            newgroup.saveToFile(nameoffile)
            print("File saved successfully")

        print(" ")
        menu()
        choice = input("Your choice?")

    print(" ")
    print("Thank you!")

main()
            
            
            
            
            
                
                
            
