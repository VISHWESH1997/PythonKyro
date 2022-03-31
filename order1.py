def inputs():
    count=1  # keeping count
    a= True  # for while condition
    ord= input(" Do you want to check or print order if yes Type Y/y or for NO type N/n:\n") #type Y or y go inside or else no
    ord = ord.lower() # to have uniformity
    if (ord == 'y'):
        while a:                
            days =0  
            try:    # exception handling
                print (" For order {} Please specify the time of order with space in between the number and time of order ".format(count))
                time,md = input().split()
                time = int(time)
                md = md.lower()
            except: # repeats until you get it right
                print (" Please enter the date or days as this example: 30 days or 2 months or 4 weeks. Try again\n")
                continue
               
            if (md == "month" or md == "months"):
                days += time * 30
            elif (md == "weeks"or md == "week"):
                days += time * 7
            else:
                days = time
            days_list.append(days)   
            item = []
            it1 = input("\nCould you specify items in this order with space in between each item\n").split()
            it1 = [x.lower() for x in it1]
            item.append(it1)
            list_item.append(it1)
            print ("\n Order '{0}' was placed for item(s) {1} {2} {3} ago". format(str(count), ', '.join(map(str,it1)),time,md))
            ord_1= input("\nIs there more orders press 'y' for yes or else 'n' for no?\n")
            ord_1 = ord_1.lower()
            if (ord_1 !=  "y"):
                a = False
            else:
                count += 1
                continue


def work():
    
    for i in range (len(days_list)):
        if (30 - days_list[i] < 0):
            list_item.remove(temp_item[i])
    list_items = sum(list_item,[])
    frequent=[]
    for i in range(len(list_items)):
        if (list_items.count(list_items[i]) > 1):
            frequent.append(list_items[i])
    if frequent:
        print("most frequently used item in 30 days are " ,', '.join(set(frequent)))
    if (bool(list_items) == False):
        print ("No items bought in 30 days") 
    if (bool(list_items) == True and bool(frequent) == False):
        print ("Recent bought items in 30 days are " , ', '.join(set(list_items)))
        
# Execution starts here below

list_item =[]  # contain list of items bought in 2d matrix form
days_list =[]  # contains days list or how much time ago items were ordered in 1d list form
inputs()       # calling function to take inputs like order items and order days
temp_item = tuple(list_item)  # if we use both as list then both point to same heap memory
if (list_item and days_list):  # an empty list is taken as False value
    work()                     # if we have some or atleast one item in list then this function is called, the working of the problem
else:
    print("You did not order anything\n") # if nothing in list prints no orders

#end of code