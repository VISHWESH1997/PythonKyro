import ast

def inputs():
    count=0  # keeping count
    global countx
    ord= input(" Do you want to check or print order if yes Type Y/y or for NO type N/n:\n") #type Y or y go inside or else no
    ord = ord.lower() # to have uniformity
    if (ord == 'y'):
        b=open("sample.txt", encoding="utf8")
        for line in b:
            days=0
            temp=[]
            print (line)
            stripped_line = (line.strip())
            stripped_line=stripped_line.replace(',','')
            line_list = stripped_line.split()
            if ('and' in line_list):
                line_list.remove('and')
                list_item.append(line_list)
                temp=line_list
            else:
                list_item.append(line_list)
                temp=line_list
            count += 1
            try:
                time = int(temp[-3])
            except:
                print ("\nGive input as such => Order x was placed for the item Watch 12 months ago.\n ")
                print ("Give input as such => Order x was placed for the item Watch 10 Days ago.\n ")
                print ("Please check order {0} and change it as shown above\n".format(temp[1]))
                countx += 1
                continue
            md = temp[-2]
            md= md.lower()
            if (md == "month" or md == "months"):
                days += time * 30
            elif (md == "weeks"or md == "week"):
                days += time * 7
            else:
                days = time
            days_list.append(days)
        b.close()
        if (countx > 0):
            print ("\n There are {0} errors in file".format(str(countx)))
        for i in range (len(days_list)):
            if (days_list[i] - 30 <= 0):
                temp_lists.append(list_item[i][7:-3])
            

def work():
    temp_list = sum(temp_lists,[])  # creating 2d list to a 1d list for easy traversal
    temp_list = [x.lower() for x in temp_list]
    frequent=[]                     # checking frequency of items
    for i in range(len(temp_list)):
        if (temp_list.count(temp_list[i]) > 1):
            frequent.append(temp_list[i])
    if frequent:
        print("\nmost frequently used item in 30 days are " ,', '.join(set(frequent)))
    if (bool(temp_list) == False):
        print ("\nNo items bought in 30 days") 
    if (bool(temp_list) == True and bool(frequent) == False):
        print ("\nRecent bought items in 30 days are " , ', '.join(set(temp_list)))






list_item =[]  # contain list of items bought in 2d matrix form
days_list =[]  # contains days list or how much time ago items were ordered in 1d list form
temp_lists = []
countx = 0   # this is used for checking number of errors in the file
inputs()     # calling function to take inputs like order items and order days
if (countx > 0):
    exit(0)
if (list_item and days_list):  # an empty list is taken as False value
    work()                     # if we have some or atleast one item in list then this function is called, the working of the problem
else:
    print("You did not order anything\n") # if nothing in list prints no orders


