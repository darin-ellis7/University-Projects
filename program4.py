#Author: Darin Ellis
#Email: dmel227@g.uky.edu
#Section 014
#Purpose: To receive data from two files, one for the inventory, one for the transactions,
#then process that data to produce a receipt detailing the purchases.
#Preconditions: Filenames input by the user to open inventory/transactions
#Postconditions: Reports invalid UPCs to the shell. Calculates and outputs the
#totals of taxable and food costs, the tax, the total bill, and number of items purchased.
#Date Completed: 12/10/14 

#get_data_from_file()
#Purpose: this function will retrieve the data from a given file and put it into a large string.
#This string will then be stripped and split and then returned to main.
#Preconditions: name of file to open (string)
#Postconditions: the data in the form of a list of strings
def get_data_from_file(fileType):
    message = "Input the name of the " + fileType + " you wish to open: "
    filename = input(message) 
    file_flag = False
    while file_flag == False:
        try:
            infile = open(filename, "r")
            file_flag = True
        except IOError:
            filename = input("Could not open file. Please input new file name: ")
    datastr = infile.read()
    stripdata = datastr.strip()
    datalst = stripdata.split("\n")
    infile.close()
    return datalst

#check_UPC()
#Purpose: to check if a upc code has the appropriate check digit
#Preconditions: a upc code to be checked
#Postconditions: true/false, depending on if the upc checks out or not
def check_UPC(upc):
    odd = int(upc[0]) + int(upc[2]) + int(upc[4]) + int(upc[6]) + int(upc[8]) + int(upc[10])
    product = odd * 3
    even = int(upc[1]) + int(upc[3]) + int(upc[5]) + int(upc[7]) + int(upc[9])
    result = even + product
    remainder = result % 10
    if remainder != 0:
        check_digit = 10 - remainder
    else:
        check_digit = 0
    if check_digit == int(upc[11]):
        check_flag = True
    else:
        check_flag = False
    return check_flag

#print_receipt()
#Purpose: to take the data from the inventory, receipt_upc, and receipt_qty, and use
#it to produce a receipt from the store
#Preconditions: inv_list, list of UPCs with product information;
#receipt_upc, list of UPCs indicating products bought; 
#receipt_qty, list of how many times an item was bought.
#Postconditions: returns nothing, receipt printed to shell
def print_receipt(inv_list, receipt_upc, receipt_qty):
    sales_tax_rate = .06
    print("\t \t Ellis Grocery \n")
    taxable_cost = 0
    tax = 0
    food_cost = 0
    item_counter = 0
    
    for upc in receipt_upc:
        upc_loc = inv_list.index(upc)
        item_name = inv_list[upc_loc + 1]
        item_cost = inv_list[upc_loc + 2]
        tax_or_food = inv_list[upc_loc + 3]
        item_qty = receipt_qty[receipt_upc.index(upc)]
        item_counter += item_qty
        if tax_or_food == "T":
            taxable_cost += float(item_cost) * item_qty
            tax += float(item_cost) * item_qty * sales_tax_rate
        else:
            food_cost += float(item_cost) * item_qty
        price = float(item_cost) * item_qty
        print(item_name)
        print("qty ", item_qty, " @ ", item_cost, " ea \t \t", price, " ", tax_or_food, "\n")
    
    print("===============================")
    print("Taxable \t \t \t $", round(taxable_cost, 2))
    print("Food \t \t \t $", round(food_cost, 2))
    print("Tax \t \t \t \t $", round(tax, 2))
    total_bill = taxable_cost + food_cost + tax
    print("Total Bill \t \t \t $", round(total_bill, 2))
    print("Total items sold \t \t", item_counter, "\n")
    print("Thanks for shopping with us!")

#the main function
def main():
    inv_list = get_data_from_file("inventory")
    trans_list = get_data_from_file("transaction")
    receipt_upc = []
    receipt_qty = []
    print("")
    
    for line in trans_list:
        check_flag = True
        if len(line) > 12:
            check_flag = False
            message = "too long"
        elif len(line) < 12:
            check_flag = False
            message = "too short"
        elif line.isnumeric() == False:
            check_flag = False
            message = "not alpha-numeric"
        elif check_UPC(line) == False:
            check_flag = False
            message = "invalid check digit"
        elif line not in inv_list:
            check_flag = False
            message = "UPC not found in inventory."
        elif check_flag == True:          #the identical UPC issue solution:
            if line not in receipt_upc:      #if it does not find the line in receipt_upc, it
                receipt_upc.append(line)    #adds it to receipt_upc and creates a corresponding
                receipt_qty.append(1)       #entry in receipt_qty
            else:
                receipt_qty[receipt_upc.index(line)] += 1
        if check_flag == False:
            print(line, " is an invalid UPC - ", message, "\n")
                
    print_receipt(inv_list, receipt_upc, receipt_qty)

main()