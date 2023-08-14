# part II
'''
Total Sales by Salesperson
o Total sales per customer
o Total sales by Product
o Total sales by Zone
o Total sales per month by each salesperson
o Total Sales and Quantities per Customer / Seller
o Total Sales and Quantities by Zone / Product
o Total Sales and Quantities per Customer / Product
o Total sales per Salesperson / Month
o Total Sales per Customer in the month: x
o List of customers above the global sales average
o List of sellers below average sales of sellers
'''
# Import all functions defined in the 'Functions.py' file
from Functions import *
# ----------------------------------------------------------------------------------------------------
# With the existing data in the 'Sales Records.csv' file, we create an 'lv' list, where we will load the data
lv=[] # list creation
header=[] # list with the first line to be used in the user view
count=0 # count lines from existing csv document
file=open("07-Data/SalesRecords.csv","r") # open file for reading
for record in file.readlines(): # for loop for reading rows
    if count==0:
        c=record.split(';')
        row=(c[0]),(c[1]),(c[2]),(c[3]),(c[4]),(c[5]),(c[7])
        header.append(row) # insert 1 line in header variable
        count+=1
    elif count != 1:
        fields=record.split(";") # separate the file fields by ";"
        linha=[int(fields[0]),int(fields[1]),fields[2],fields[3],fields[4],fields[5],int(fields[6]),float(fields[7])] # create a list and convert the data type
        lv.append(linha) # add to student list (lv)
    count+=1
# ----------------------------------------------------------------------------------------------------
while True: # Aplication Menu
    try:
        opc2 = menu2()
        if opc2==0: # exit the application
            clean()
            print('Application offline!\n\nCOPYRIGHT\n\nEMANUEL')
            break
# --------------------------------------------------------
        elif opc2==1: # menu analyze sales
            clean()
            while True:
                print(20*'-'+'SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                try: # prompt for the user to choose whether the sales analysis is about customers, vendors, zone or product
                    option=int(input('Enter\n1-Sales/Seller\n2-Sales/Customer\n3-Sales/zone\n4-Sales/product\n5-Sales/month\n0-Back to previous menu!'))
                    if option==0: # back to previous menu
                        clean()
                        break
# --------------------------------------------------------
                    elif option==1:# value/sales/seller
                        clean()
                        while True:
                            print(20*'-'+'SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            try: # the user has the option of inserting the salesperson's number or viewing the sales summary by salesperson
                                option1=int(input('Enter\n(number)-Salesperson(eg 100)\n(1)-Sales summary by salesperson\n'
                                '(2)-Sales summary/month/seller\n(0)-Back to previous menu!'))
                                clean()
                                sumSales=0
                                sellersList=[]
                                for l in lv: # create list of unique sellers
                                    if l[1] not in sellersList:
                                        sellersList.append(l[1])
                                if option1 in sellersList:# check if the seller entered by the user exists in the database if so calculates the sum of values
                                    print(20*'-'+'SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                    sellerNum=option1
                                    for lists in lv:
                                        if lists[1]==sellerNum:
                                            sumSales+=lists[7]
                                    print(f'The employee: {sellerNum}, has a total of {round(sumSales,2)} euros in sales! ')
                                elif option1==1:#o summary de vendas por seller, para cada seller(unico) faz a sum de valores
                                    clean()
                                    print(20*'-'+'SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                    salesSeller=[]
                                    for lists in lv:
                                        if lists[1] not in salesSeller:
                                            salesSeller.append(lists[1])
                                            salesSeller.append(lists[7])
                                        else:
                                            index= salesSeller.index(lists[1])
                                            sumSales = lists[7]+salesSeller[index+1]
                                            salesSeller[index+1]=sumSales
                                    for i in range(0,len(salesSeller),2):# summary listing output
                                        print(f'The employee :{salesSeller[i]} sold a total of: {round(salesSeller[i+1],2)} euros ')
# --------------------------------------------------------                                        
                                elif option1==2:
                                    clean()
                                    print(20*'-'+'SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                    summary=[]
                                    for lists in lv:
                                        month=lists[4].split('/')[1] # extract the month from the date and assign it to the month variable
                                        summary.append([f'{lists[1]}-{month}',lists[7]]) # add to the new summary list, the seller and month in the same field (concatenating strings)
                                    finalList=[]
                                    sum=0
                                    numcompras=0
                                    for l in summary:
                                        if l[0] not in finalList: # add in a new finalList the unique strings resulting from the concatenation of seller with month
                                            finalList.append(l[0])
                                            finalList.append(l[1])
                                            finalList.append(1) # add the value 1 of a sale to the final list for transaction count
                                        else:
                                            index=finalList.index(l[0]) #index of the seller code field already inserted in the list
                                            sum=l[1]+finalList[index+1] # add the values ​​to the existing ones, whenever the finalList already has the seller
                                            sumPurchases=finalList[index+2]+1 # add 1 to the existing value in the sales num field
                                            finalList[index+1]=sum # sum purchase values
                                            finalList[index+2]=sumPurchases # replace the purchase count value with the updated number
                                    #output
                                    for i in range(0,len(finalList),3): # go through the final list 3 by 3
                                        seller=finalList[i].split('-')[0] # extract the vendor code of the month by '-'
                                        month=finalList[i].split('-')[1] # extract the month
                                        value=finalList[i+1] # store value in value variable
                                        sumPurchases=finalList[i+2] # store the sum of transactions in the variable sum purchases
                                        print(f'The seller {seller}, made {sumPurchases} sale, in the month {month}, with the value of  {round(value,2)} euros!')
                                    print('\n')
# -------------------------------------------------------- 
                                elif option1==0: # back to previous menu
                                    clean()
                                    break
                                else:
                                    print(f'The seller {option1} does not exist!\nPlease enter a valid seller number!\nex:{sellersList}') # output if the seller number, entered by the user, does not exist or the option is wrong
                            except Exception :
                                clean()
                                print('Option not valid!') # output if user input is different from int
                            except:
                                clean()
                                print('Wrong value entered!')   
# ----------------------------------------------------------------------------------------------------
                    elif option==2: #value/sales/Customer
                        clean()
                        while True:
                            print(20*'-'+'CUSTOMER SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            try:
                                option1=int(input('Enter\n(Number) of customer(ex:5)\n(-1)summary of sales by customer\n'
                                '(-2)summary sales customer/month\n0-Back to previous menu!'))
                                clean()
                                print(20*'-'+'CUSTOMER SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                sumSales=0
                                customerList=[]
                                for l in lv: # unique customer list
                                    if l[2] not in customerList:
                                        customerList.append(l[2])
                                if 'customer:'+str(option1) in customerList:
                                    numCustomer='customer:'+str(option1)
                                    for lists in lv:
                                        if lists[2] ==numcustomer:
                                            sumSales+=lists[7]
                                    print(f'The Customer: {numCustomer}, has a total of {round(sumSales,2)} euros in purchases! ')
                                    print('\n')
                                elif option1==-1:
                                    customerSales=[]
                                    clean()
                                    print(20*'-'+'CUSTOMER SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                    for lists in lv:
                                        if lists[2] not in customerSales:
                                            customerSales.append(lists[2])
                                            customerSales.append(lists[7])
                                        else:
                                            index= customerSales.index(lists[2])
                                            custumerSalesSum = lists[7]+customerSales[index+1]
                                            customerSales[index+1]=custumerSalesSum
                                    for i in range(0,len(customerSales),2):
                                        print(f'{customerSales[i]} he bought : {round(customerSales[i+1],2)} euros ')
                                    print('\n')
                                elif option1==-2: # Total sales per month per customer
                                    clean()
                                    print(20*'-'+'CUSTOMER/MONTH SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                    # Insert the customer/month/value into the summary list as multiple lists
                                    summary=[]
                                    for lists in lv:
                                        month=lists[4].split('/')[1] # extract the month from the date and assign it to the month variable
                                        summary.append([f'{lists[2]}-{month}',lists[7]]) # add to the new summary list, the customer and month in the same field (concatenating strings)
                                    finalList=[]
                                    sum=0
                                    for l in summary:
                                        if l[0] not in finalList: # add to the new summary list, the customer and month in the same field (concatenating strings)
                                            finalList.append(l[0])
                                            finalList.append(l[1])
                                            finalList.append(1) # add the value 1 of a sale to the final list (number of sales)
                                        else:
                                            index=finalList.index(l[0]) #index of field already inserted in list
                                            sum=l[1]+finalList[index+1] # add the values ​​to the existing ones whenever the new list already has the customer
                                            sumPurchases=finalList[index+2]+1 # add 1 to the existing value in the sales num field
                                            finalList[index+1]=sum # sum purchase amounts
                                            finalList[index+2]=sumPurchases#  replaces the purchase count value with the updated number
                                    #output
                                    for i in range(0,len(finalList),3): # go through the final list 3 by 3
                                        customer=finalList[i].split('-')[0] # extract the name of the customer of the month by the '-'
                                        month=finalList[i].split('-')[1] # extract the month
                                        value=finalList[i+1] #armazenar valor na variável calor
                                        sumPurchases=finalList[i+2]
                                        print(f'The {customer}, made {sumPurchases} purchase, in the month {month}, worth {round(value,2)} euros! ')
                                    print('\n') 
                                elif option1==0:
                                    clean()
                                    break
                                else:
                                    clean()
                                    print(f'Customer number does not exist!\nPlease enter a valid customer!\n ex:\n{customerList}')
                            except:
                                clean()
                                print('Option not valid!')
# ----------------------------------------------------------------------------------------------------
                    elif option==4: #Value/Sales/Product
                        clean()
                        while True:
                            print(20*'-'+'PRODUCT SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            option1=input('Enter:\nProduct reference (ex:XPT123)\n(1)-summary of quantities per product!\n(0)-Back to previous menu!')
                            print(20*'-'+'PRODUCT SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            productList=[]
                            for l in lv: # unique product list
                                if l[5] not in productList:
                                    productList.append(l[5])
                            # treatment of input options
                            if len(option1)>6:
                                clean()
                                print('Code or option not valid!')
                            else:
                                if  option1.isdigit():
                                    option1=int(option1)
                                else:
                                    option1= option1.upper()
                            if option1 in productList: # sales of the product indicated by the user
                                clean()
                                sumSales=0
                                product= option1
                                for lists in lv:
                                    if lists[5] ==product:
                                        sumSales+=lists[7]
                                print(f'The value made with the sale of the product: {product} was: {round(sumSales,2)} euros!')
                                print('\n')
                            elif option1==1:#summary de vendas por product
                                clean()
                                print(20*'-'+'SALES ANALYSIS SYSTEM product'+20*'-'+'\n'+'\n')
                                sunSalesProduct=0
                                productSales=[]
                                for lists in lv:
                                    if lists[5] not in productSales:
                                        productSales.append(lists[5])
                                        productSales.append(lists[7])
                                    else:
                                        index= productSales.index(lists[5])
                                        sunSalesProduct = lists[7]+productSales[index+1]
                                        productSales[index+1]=sunSalesProduct
                                for i in range(0,len(productSales),2):
                                    print(f'The total sales of the product {productSales[i]} is: {round(productSales[i+1],2)} euros ')
                                print('\n')
                            elif option1==0: # previous menu
                                clean()
                                break 
                            else:
                                clean()
                                print('Option not valid!') 
# ----------------------------------------------------------------------------------------------------
                    elif option==3: #Value/sales/Zone
                        clean()
                        while True:
                            print(20*'-'+'ZONE SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            option1=input('Enter:\nThe zone (eg:N)\n(1)-summary of values ​​across all zones\n(0)-Back to previous menu!')
                            clean()
                            print(20*'-'+'ZONE SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            # treatment of input options
                            option1=option1.upper()   
                            zonelist=[] # list of unique zones
                            for l in lv: 
                                if l[3] not in zonelist:
                                    zonelist.append(l[3])                      
                        # calculation of value by zone selected by the user
                            sumSales=0
                            if option1 in zonelist:                              
                                for lists in lv:
                                    if lists[3] ==option1:
                                        sumSales+=lists[7]
                                print(f'A zone: {option1}, has a total of {round(sumSales,2)} euros in sales!')                                                                          
                            elif option1=='1': #summary sales zone
                                zoneSales=[]
                                for lists in lv:
                                    if lists[3] not in zoneSales:
                                        zoneSales.append(lists[3]) #add zone to the new zoneSales list
                                        zoneSales.append(lists[7]) # add corresponding value to the new zoneSales list
                                    else:
                                        index= zoneSales.index(lists[3]) #check the zone index in the new zoneSales list
                                        sumSales = lists[7]+zoneSales[index+1] # sum the checked value to the existing value in the new zoneSales list
                                        zoneSales[index+1]=sumSales # insert the value of the sum of values ​​in the place immediately after index (index+1)
                                for i in range(0,len(zoneSales),2): # for the range between 0 and the length of the zoneSales list, 2 to 2 positions 
                                    print(f'The total sales by zone {zoneSales[i]} is: {round(zoneSales[i+1],2)} euros ')
                            elif option1=='0':# previous menu
                                clean()
                                break
                            else :
                                print(f'Option inserted: {option1} is not valid for the menu!')
                                continue 
# ----------------------------------------------------------------------------------------------------                         
                    elif option==5:  #value/sales/month
                        clean()
                        while True:
                            print(20*'-'+'MONTH SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                            try:
                                option1=input('Enter;\nNumber of the month (ex:02)\n(-1) summary of values ​​for all months\n(0)-Back to the previous menu!')
                                print(20*'-'+'MONTH SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                                #initiate variables
                                summary=[]
                                namesList=[]
                                uniqueMonth=[]
                                sum=0
                                #work date
                                for lists in lv:
                                    mes=lists[4].split('/')[1] # extract the month from the date and assign it to the month variable
                                    namesList.append([mes,lists[7]]) # add to the new summary list, the month and value 
                                # insert the month/value in the summary list                     
                                for i in namesList:
                                    if i[0] not in summary:
                                        summary.append(i[0])
                                        summary.append(i[1])
                                    else:
                                        index=summary.index(i[0])
                                        sum=i[1]+summary[index+1]
                                        summary[index+1]=sum
                                # unique month lists
                                for m in namesList:
                                    if m[0]not in uniqueMonth:
                                        uniqueMonth.append(m[0])
                                # user inserts the number of the month to be consulted
                                if option1 in uniqueMonth:
                                    clean()
                                    for r in range(0,len(summary),2):
                                        if summary[r] ==option1:  
                                            print(f'In the month : {option1}, the total sales is: {round(summary[r+1],2)} euros !')
                                elif option1=='0':# Previous menu
                                    clean()
                                    break
                                elif option1=='-1':# Total sales per month summary
                                    clean()
                                    print(20*'-'+'MONTH SALES ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                                    summary=[]                               
                                    for i in namesList:
                                        if i[0] not in summary:
                                            summary.append(i[0])
                                            summary.append(i[1])
                                        else:
                                            index=summary.index(i[0])
                                            sum=i[1]+summary[index+1]
                                            summary[index+1]=sum
                                    for i in range(0,len(summary),2):
                                        print(f'The total sales in the month {summary[i]} was {round(summary[i+1],2)} euros!')
                                else :
                                    print(f'Option inserted: {option1} is not valid for the menu!')
                                    continue 
                            except:
                                print(f'The value {option1}, entered is not valid!')
                    else:
                        clean()
                        print(f'Option {option} is not valid in the menu!')
                except:
                    clean()
                    print('Option not valid!')    
# ----------------------------------------------------------------------------------------------------   
# List of customers above the global sales average                                                       
        elif opc2 == 3 :
            #calculations
            #globalAverage=(sumTotalSales/totalCustomers) 
            #averageCustomer=(sumCustomerSales/purcheseNumber)
            clean()
            sumTotalSales=0
            totalCustomers=0
            globalAverage=0
            sumCustomerSales=0
            sumPurcheses=0
            averageCustomer=0
            summaryCustomerSales=[]
            #comparison of total customer sales with the global average
            for l in lv: #creation of summary list with unique customers and sum of values
                sumTotalSales+=l[7]#variable that receives and sums all values
                if l[2] not in summaryCustomerSales:# verification of the existence of the unique customer and sum of the sale value
                    summaryCustomerSales.append(l[2])#add customer to list
                    summaryCustomerSales.append(l[7])#add the value to the list
                    totalCustomers+=1#count the number of customers
                    summaryCustomerSales.append(1)#add 1 to each transaction
                else:
                    index=summaryCustomerSales.index(l[2]) #checks the customer's index in the summary list
                    sumCustomerSales=summaryCustomerSales[index+1]+l[7]#sum the existing value to the new value
                    summaryCustomerSales[index+1]=sumCustomerSales#change the existing value by the sum of aggregated values
                    sumPurcheses=summaryCustomerSales[index+2]+1# variable that sums the number of purchases
                    summaryCustomerSales[index+2]=sumPurcheses#adds the number of purchases field to the summary list
            while True:
                print(20*'-'+'AGGREGATE SALES/AVERAGE/CUSTOMERS ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                try:                  
                    option=int(input('ENTER:\n(1)-Customers above global average\n(2)-customers below global average\n(0)-Back to previous menu!'))
                    
                    if option==0: # Main Menu
                            clean()
                            break
                    elif option==1:
                        clean()
                        print(20*'-'+'AGGREGATE SALES ANALYSIS SYSTEM/AVERAGE CUSTOMERS'+20*'-'+'\n'+'\n') 
                        #calculating the global mean and assigning it to a variable
                        globalAverage=round((sumTotalSales/totalCustomers),2)
                        #output 
                        print(f'The global average is : {globalAverage} euros!')
                        print('Customers with an average purchase above the global average are:')
                        for i in range(0,len(summaryCustomerSales),3):#traverse the summary list, with for loop its length with 3 iterations
                            averageCustomer=round((summaryCustomerSales[i+1]/summaryCustomerSales[i+2]),2)#customer average calculation
                            if averageCustomer > globalAverage:#comparison between sum of customers values ​​and global average
                                print(f'{summaryCustomerSales[i]}, with {summaryCustomerSales[i+2]} sales and average {averageCustomer} euros!') #output
                        print('\n')
                    elif option==2:
                        clean()
                        print(20*'-'+'AGGREGATE SALES ANALYSIS SYSTEM/AVERAGE CUSTOMERS'+20*'-'+'\n'+'\n') 
                        #calculation of the global average and assignment to a variable
                        globalAverage=round((sumTotalSales/totalCustomers),2)
                        #output s
                        print(f'The global average is : {globalAverage} euros!')
                        print('Customers with an average purchase below the global average are')
                        for i in range(0,len(summaryCustomerSales),3):#traverse the summary list, with for loop its length with 3 iterations
                            averageCustomer=round((summaryCustomerSales[i+1]/summaryCustomerSales[i+2]),2)#customer average calculation
                            if averageCustomer < globalAverage:#comparison between sum of customers values ​​and global average
                                print(f'{summaryCustomerSales[i]}, with {summaryCustomerSales[i+2]} sales and average {averageCustomer} euros!') #output
                        print('\n')
                    else:
                        clean()
                        print(20*'-'+'AGGREGATE SALES ANALYSIS SYSTEM/AVERAGE CUSTOMERS'+20*'-'+'\n'+'\n') 
                        print('Option not valid!') 
                except:
                    clean()
                    print(20*'-'+'AGGREGATE SALES ANALYSIS SYSTEM/AVERAGE CUSTOMERS'+20*'-'+'\n'+'\n') 
                    print('Option not valid!')
# ----------------------------------------------------------------------------------------------------   
#List of sellers below the global sales average  
        elif opc2 == 4:
            #List of sellers below average seller sales
            #calculations
            #globalAverage=(sumTotalSales/totalSellers) 
            #averageSeller=(sumSalesSeller/numberSales)
            clean()
            sumTotalSales=0
            totalSellers=0
            globalAverage=0
            sumSalesSeller=0
            numberSales=0
            averageSeller=0
            sellerSalesSummary=[]
            #comparison of total seller sales with the global average
            for l in lv: #creation of the summary list with the unique sellers and sum of values
                sumTotalSales+=l[7]#variable that receives and sums all values
                if l[1] not in sellerSalesSummary:# verification of the existence of the single seller and sum of the sale value
                    sellerSalesSummary.append(l[1])# add the seller to the list
                    sellerSalesSummary.append(l[7])#add the value to the list
                    totalSellers+=1# count the number of customers
                    sellerSalesSummary.append(1)
                else:
                    index=sellerSalesSummary.index(l[1]) # checks the seller's index in the summary list
                    sumSalesSeller=sellerSalesSummary[index+1]+l[7]# sum the existing value to the new value
                    sellerSalesSummary[index+1]=sumSalesSeller# change the existing value by the sum of aggregated values
                    sumPurcheses=sellerSalesSummary[index+2]+1# variable that sums the number of purchases
                    sellerSalesSummary[index+2]=sumPurcheses# adds the number of purchases field to the summary list   
            while True:
                print(20*'-'+'AGGREGATE SALES/AVERAGE/SELLERS ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                try:                      
                    option=int(input('INSERT:\n(1)-sellers below the global average\n(2)-sellers above the global average\n(0)-Back to the previous menu!'))
                    if option==0: # Main Menu
                            clean()
                            break 
                    elif option==1:
                        clean()
                        print(20*'-'+'AGGREGATE SALES/AVERAGE/SELLERS ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                        # calculation of the global average and assignment to a variable
                        globalAverage=round((sumTotalSales/totalSellers),2)
                        #output
                        print(f'The global average is : {globalAverage} euros!')
                        print('Sellers with an average purchase below the global average are:')
                        for i in range(0,len(sellerSalesSummary),3):#traverse the summary list, with for loop its length with 3 iterations
                            averageSeller=round(sellerSalesSummary[i+1]/sellerSalesSummary[i+2])# average seller calculation
                            if averageSeller < globalAverage:# comparison between the sum of seller values ​​and the global average
                                print(f'{sellerSalesSummary[i]}, with an average of {averageSeller} euros!') #output 
                        print('\n')
                    elif option==2:
                        clean()
                        print(20*'-'+'AGGREGATE SALES/AVERAGE/SELLERS ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                        #calculation of the global average and assignment to a variable
                        globalAverage=round((sumTotalSales/totalSellers),2)
                        #output
                        print(f'The global average is : {globalAverage} euros!')
                        print('Sellers with an average purchase above the global average are:')
                        for i in range(0,len(sellerSalesSummary),3):#traverse the summary list, with for loop its length with 3 iterations
                            averageSeller=round(sellerSalesSummary[i+1]/sellerSalesSummary[i+2])# average seller calculation
                            if averageSeller > globalAverage:#comparison between the sum of seller values ​​and the global average
                                print(f'{sellerSalesSummary[i]}, with an average of {averageSeller} euros!') #output 
                        print('\n')
                    else:
                        clean()
                        print(20*'-'+'AGGREGATE SALES/AVERAGE/SELLERS ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                        print('Option not valid!') 
                except:
                    clean()
                    print(20*'-'+'AGGREGATE SALES/AVERAGE/SELLERS ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                    print('Option not valid!')
# ----------------------------------------------------------------------------------------------------
        #-Total Quantities per customer / seller
        elif opc2==2:
            clean()
            sellersList=[]
            sellerNum=0
            customerList=[]
            numcustomer=0
            zonelist=[]
            productList=[]
            for l in lv: # unique sellers list
                if l[1] not in sellersList:
                    sellersList.append(l[1])
            for l in lv: # unique customer list
                if l[2] not in customerList:
                    customerList.append(l[2])
            for l in lv: # unique zone list
                if l[3] not in zonelist:
                    zonelist.append(l[3])
            for l in lv: # unique products list
                if l[5] not in productList:
                    productList.append(l[5])
            while True:
                print(20*'-'+'QUANTITY ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
                try:
                    option=int(input('Enter:\n(1)-Quantities/seller\n(2)-Quantities/customer\n(3)-Quantities/zone\n(4)-Quantities/product\n(0)-Back to previous menu!'))
                    if option==1: #seller
                        clean()
                        while True:
                            print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/seller'+20*'-'+'\n'+'\n') 
                            try:
                                option1=int(input('Introduce:\nSeller number (ex:100)\n1-summary of all collaborators\n0-Back to the previous menu!'))
                                clean()
                                sumQuantities=0
                                customerSellerQuantities=[]
                                if option1 in sellersList:
                                    print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/seller'+20*'-'+'\n'+'\n') 
                                    sellerNum=option1
                                    for lists in lv:
                                        if lists[1] ==sellerNum:
                                            sumQuantities+=lists[6]
                                    print(f'The seller: {sellerNum}, has a total of {sumQuantities} items sold!')
                                    print('\n')
                                elif option1==1:
                                    clean()
                                    print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/seller'+20*'-'+'\n'+'\n') 
                                    print('\n')
                                    for lists in lv:
                                        if lists[1] not in customerSellerQuantities:
                                            customerSellerQuantities.append(lists[1]) 
                                            customerSellerQuantities.append(lists[6]) 
                                        else:
                                            index= customerSellerQuantities.index(lists[1])
                                            sumQuantities = lists[6]+customerSellerQuantities[index+1] 
                                            customerSellerQuantities[index+1]=sumQuantities 
                                    for i in range(0,len(customerSellerQuantities),2):
                                        print(f'The total quantities per seller {customerSellerQuantities[i]} is: {customerSellerQuantities[i+1]} units')
                                    print('\n')
                                elif option1==0:
                                    clean()
                                    break
                                else:
                                    clean()
                                    print(f'Seller number does not exist.\nInsert:\nex:{sellersList}')
                            except:
                                clean()
                                print('Option not valid!')
# ----------------------------------------------------------------------------------------------------              
                    elif option==2: # customer
                        clean()
                        while True:
                            print(20*'-'+'QUANTITY ANALYSIS SYSTEM/customer'+20*'-'+'\n'+'\n') 
                            try:
                                option1=int(input('Enter:\nCustomer number (eg 5)\n(-1)-summary of all customers\n(0)-Back to previous menu!'))
                                sumQuantities=0
                                customerSellerQuantities=[]
                                clean()
                                if 'customer:'+str(option1) in customerList:
                                    print(20*'-'+'QUANTITY ANALYSIS SYSTEM/customer'+20*'-'+'\n'+'\n')
                                    numcustomer='customer:'+str(option1)
                                    for lists in lv:
                                        if lists[2] ==numcustomer:
                                            sumQuantities+=lists[6]
                                    print(f'The customer: {numcustomer}, has a total of {sumQuantities} items purchased!')
                                elif option1==-1:
                                    print(20*'-'+'QUANTITY ANALYSIS SYSTEM/customer'+20*'-'+'\n'+'\n') 
                                    for lists in lv:
                                        if lists[2] not in customerSellerQuantities:
                                            customerSellerQuantities.append(lists[2]) 
                                            customerSellerQuantities.append(lists[6]) 
                                        else:
                                            index= customerSellerQuantities.index(lists[2])
                                            sumQuantities = lists[6]+customerSellerQuantities[index+1] 
                                            customerSellerQuantities[index+1]=sumQuantities 
                                    for i in range(0,len(customerSellerQuantities),2):
                                        print(f'The total quantities purchased by {customerSellerQuantities[i]} is: {customerSellerQuantities[i+1]} units.')
                                    print('\n')
                                elif option1==0:
                                    clean()
                                    break
                                else:
                                    clean()
                                    print(20*'-'+'QUANTITY ANALYSIS SYSTEM/customer'+20*'-'+'\n'+'\n')
                                    print(f'The customer does not exist!\nThe existing customers are:\n{customerList}')
                            except:
                                clean()
                                print(20*'-'+'QUANTITY ANALYSIS SYSTEM/customer'+20*'-'+'\n'+'\n')
                                print('Option not valid!')
# ----------------------------------------------------------------------------------------------------                                 
                    elif option==3:#Quantities/zone
                        clean()
                        while True:
                            print(20*'-'+'QUANTITIES/ZONE ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                            option1=input('Enter:\nThe zone (eg:N)\n(1) for the summary of all zones\n(0)-Back to the previous menu!')
                            # treatment of input options
                            if len(option1)>1:
                                print('Invalid option')
                            else:
                                if  option1.isdigit():
                                    option1=int(option1)
                                else:
                                    option1=option1.upper()
                        # calculation of quantities by zone selected by the user
                            sumQuantities=0
                            if option1 in zonelist:
                                clean()
                                print(20*'-'+'QUANTITIES/ZONE ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                                zone=option1
                                for lists in lv:
                                    if lists[3] ==zone:
                                        sumQuantities+=lists[6]
                                print(f'The zone: {zone}, has a total of {sumQuantities} items sold!')
                                print('\n')
                            elif option1==1:# summary quantities zones
                                clean()
                                print(20*'-'+'QUANTITIES/ZONE ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                                zoneSales=[]
                                sumQuantities=0
                                for lists in lv:
                                    if lists[3] not in zoneSales:
                                        zoneSales.append(lists[3]) 
                                        zoneSales.append(lists[6]) 
                                    else:
                                        index= zoneSales.index(lists[3])
                                        sumQuantities = lists[6]+zoneSales[index+1] 
                                        zoneSales[index+1]=sumQuantities
                                for i in range(0,len(zoneSales),2):
                                    print(f'The total quantities per zone {zoneSales[i]} is: {round(zoneSales[i+1],2)} units')
                                print('\n')
                            elif option1==0:# Main Menu
                                clean()
                                break
                            else:
                                clean()
                                print(20*'-'+'QUANTITIES/ZONE ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                                print('Zone or option is not valid')
# ----------------------------------------------------------------------------------------------------                                   
                    elif option==4: # quantities per product
                        clean()
                        while True:
                            print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/product'+20*'-'+'\n'+'\n') 
                            option1=input('Enter:\nThe product ref (ex:XPT123)\n(1)-summary of quantities per product\n(0)-Back to the previous menu!')
                            clean()
                            # treatment of input options
                            if len(option1)>6:
                                print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/product'+20*'-'+'\n'+'\n') 
                                print('Code or option not valid!')
                            else:
                                if  option1.isdigit():
                                    option1=int(option1)
                                else:
                                    option1=option1.upper()
                            if option1 in productList:
                                clean()
                                print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/product'+20*'-'+'\n'+'\n') 
                                sumQuantities=0
                                product= option1
                                for lists in lv:
                                    if lists[5] ==product:
                                        sumQuantities+=lists[6]
                                print(f'{sumQuantities} units of product {product} were sold!')
                                print('\n')
                            elif option1==0:
                                clean()
                                break
                            elif option1==1:# Total Sales and Quantities/product
                                clean()
                                print(20*'-'+'QUANTITIES ANALYSIS SYSTEM/product'+20*'-'+'\n'+'\n') 
                                sumQuantities=0
                                productSales=[]
                                for lists in lv:
                                    if lists[5] not in productSales:
                                        productSales.append(lists[5]) 
                                        productSales.append(lists[6]) 
                                    else:
                                        index= productSales.index(lists[5])
                                        sumQuantities = lists[6]+productSales[index+1] 
                                        productSales[index+1]=sumQuantities
                                for i in range(0,len(productSales),2):
                                    print(f'The total quantities per product :{productSales[i]} is: {round(productSales[i+1],2)} units') 
                                print('\n') 
                            else:
                                clean()
                                print(20*'-'+'SYSTEM ANALYSIS QUANTITIES/product'+20*'-'+'\n'+'\n') 
                                print('Product or option is not valid')    
                    elif option==0: #main menu
                        clean()
                        break    
                    else:
                        clean()
                        print(20*'-'+'QUANTITY ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                        print('Option not valid!')      
                except:
                    clean()
                    print(20*'-'+'QUANTITY ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
                    print('Option not valid!')
        else:
            clean()
            print(20*'-'+'ANALYSIS SYSTEM'+20*'-'+'\n'+'\n') 
            print(f'Option {opc2} is not valid in the menu!')
    except:
        clean()
        print(20*'-'+'ANALYSIS SYSTEM'+20*'-'+'\n'+'\n')
        print(f'Invalid value entered')