# Part I

# Import all functions defined in the 'Functions.py' file
from Functions import *
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------
# Part 1 program
while True:
    opc= menu() # import visual menu with user input validation
    if opc == 0:
        clean()
        print('Application shut down!')
        break
    elif opc == 1: # insert record
        clean()
        print(20*'-'+'Chose option 1-Insert'+20*'-')
        print('\n')
        while True: # cycle of the record insertion process, validating each entry and presenting the entries to the user
            print(20*'-'+'Enter:'+20*'-') 
#------------sellerNumber--------------------------------------------------------------------
            sellerCode= sellerNumber('The Seller code (ex: 100) \n (0)-Cancel registration!')
            if sellerCode==0:
                clean()
                break
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nSeller code: {sellerCode}!')
            print(20*'-'+'Enter:'+20*'-') 
#------------custumerNumber--------------------------------------------------------------------
            customer= customerNumber('(number) of the client\n(0)-Cancel registration!')
            customer=str(customer)
            if customer=='0':
                clean()
                break
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nSeller Code: {sellerCode}!\nCustomer Code: {customer}!')
            print(20*'-'+'Enter:'+20*'-')
#------------custumerZone--------------------------------------------------------------------
            zone=customerZone('Customer zone:\nNorth(“N”)\nCenter(“C”)\nSouth(“S”)\nIslands(“I”)\n(0)-Cancel registration!')
            if zone=='0':
                clean()
                break
            clean()
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nSeller Code: {sellerCode}!\nCustomer Code: {customer}\nCustomer Zone: {zone}!')
            print(20*'-'+'Enter:'+20*'-')
#------------date--------------------------------------------------------------------
            date= valDate('The date of sale in the format:dd/mm/yyyy\n(0)-Calcel record!')
            if date=='0':
                break
            clean()
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nSeller Code: {sellerCode}!\nCustomer Code: {customer}\nCustomer zone: {zone}!\nDate of sale: {date}!')
            print(20*'-'+'Enter:'+20*'-')
#------------productCode--------------------------------------------------------------------
            productCode= valProduct('Product code\n(0)-Calcel registration!')
            if productCode=='0':
                break
            clean()
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nSeller Code: {sellerCode}!\nCustomer Code: {customer}'
            f'\nCustomer zone: {zone}!\nDate of sale: {date}!\nProduct code: {productCode}')
            print(20*'-'+'Enter:'+20*'-')
#------------quantity--------------------------------------------------------------------
            quantity=valQuantity('The quantity\n(0)-Calcel record!')
            if quantity==0:
                break
            clean()
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nCode of seller: {sellerCode}!\nCode of customer: {customer}'
            f'\nCustomer zone: {zone}!\nSale date: {date}!\nProduct code: {productCode}'
            f'\nQuantity: {quantity}')
            print(20*'-'+'Introduza:'+20*'-')
#------------salevalue--------------------------------------------------------------------
            saleValue= valSaleValue('The value of the sale\n(0)-Calcel record!')
            if saleValue==0:
                break
            clean()
            print(20*'-'+'Chose option 1-Insert'+20*'-')
            print(f'INSERTED:\nSeller Code: {sellerCode}!\nCustomer Code: {customer}'
            f'\nCustomer zone: {zone}!\nSale date: {date}!\nProduct code: {productCode}'
            f'\nQuantity: {quantity} uni\nSale value {saleValue} €')
#------------write record to csv--------------------------------------------------------------------
            salesId= lv[-1][0]+1
            sale=[salesId, sellerCode,'Customer:'+ customer,zone, date, productCode, quantity,saleValue]
            lv.append(sale)
            file=open("07-Data/SalesRecords.csv","w") # open file for writing
            file.write(f"SalesNumber;SallerCode;NumberCustomer;Zone;Date;ProductCode;Quantity;Price;\n") # write field headers
            for i in range(len(lv)):
                file.write(f"{lv[i][0]};{lv[i][1]};{lv[i][2]};{lv[i][3]};{lv[i][4]};{lv[i][5]};{lv[i][6]};{lv[i][7]};\n") 
            file.close()
            print(f'Sales record no.: {salesId}, successfully completed!')
            break  
#-----------------------------------------------------------------------------------------------------              
# Option2 : consult records with the insertion of the sale number and error validation
    elif opc ==2:
        # create two lists with sales and void sales 
        listCanceledSales=[]
        ListSales=[]
        for l in lv:
            ListSales.append(l[0])
        for i in range(1,lv[-1][0],1):
            if i not in ListSales:
                listCanceledSales.append(i)
        clean()
        while True:     
            print(20*'-'+'You chose option 2-Consult'+20*'-')
            try:
                search =valPositiveInteger('Indicate:\n(No.) of the sale you want to consult!\n(0)-Back to the main menu!')
                if search==0:
                        clean()
                        break
                elif search > lv[-1][0]:# sales number does not exist
                    clean()
                    print(20*'-'+'You chose option 2-Consult'+20*'-')
                    print(f'Sale {search} does not exist!')
                elif search in ListSales:# view of selected sale
                    for l in lv:
                        if l[0]==search:
                            clean()
                            print(20*'-'+'You chose option 2-Consult'+20*'-')
                            print(f'Sales query no.:{search}\n{header}')
                            print(l)
                elif  (lv[-1][0]>search) and (search in range(1,lv[-1][0],1)):# canceled sales
                    clean()
                    print(20*'-'+'You chose option 2-Consult'+20*'-')
                    print(f'Sale : {search} has been voided!')
                    while True:# option to view voided sales
                        try:
                            annulled = valPositiveInteger(f'To see the list of canceled sales\n'
                            f'Insert:\n(1)-Sales cancelled\n(0)-Back to the previous menu!')
                            if annulled==0:
                                clean()
                                break
                            elif annulled ==1:
                                clean()
                                print(20*'-'+'Canceled sales list'+20*'-')
                                print(f'Canceled sales are:\n')
                                print(listCanceledSales) 
                                break 
                            else:
                                print(f'Option {annulled} is not valid')
                        except:
                            print('ERROR')                              
            except Exception: 
                print('ERROR')
#-----------------------------------------------------------------------------------------------------
# List all records in a single listing   
    elif opc == 3 :
        print(20*'-'+'You chose option 3-List'+20*'-')
        count=0
        for i in lv:
            count+=1
            print(i)
        print(f'\nThe existing {count} sales have been successfully listed!\n')
#----------------------------------------------------------------------------------------------------- 
# change: we define new variables that receive user input, validated by the created function
    elif opc == 4:
        clean()
        print( 20*'-'+'You chose option 4-Change'+20*'-'+'\n')
        # create two lists with sales and void sales 
        listCanceledSales=[]
        ListSales=[]
        for l in lv:
            ListSales.append(l[0])
        for i in  range(1,lv[-1][0],1):
            if i not in ListSales:
                listCanceledSales.append(i)
        # Loop
        while True:
            try:
                print(20*'-'+'Enter:'+20*'-') 
                change= valPositiveInteger('The sales number to change !\n(0)-return to main menu!')
                if change==0: # back to previous menu
                    clean()
                    break
                elif change>lv[-1][0]:# sales number does not exist
                    clean()
                    print( 20*'-'+'You chose option 4-Change'+20*'-'+'\n')
                    print(f'\nThe sale entered {change}, does not exist!\n')
                elif change in listCanceledSales:# sale deleted
                    clean()
                    print( 20*'-'+'You chose option 4-Change'+20*'-'+'\n')
                    print(f'\nThe sale entered {change}, does not exist has been deleted!\n')
                for i in lv:# existing sale change
                    if i[0]== change:
                        index=lv.index(i) # sale to change corresponds to the index of the list with 1 element = change
                        clean()
                        sallerCode=lv[index][1]
                        print(f'You chose to change sale: {change}!\n')
                        print(f'{header[0]}')
                        print(lv[index])
#----------------------------------------------------------------------------------------------------- 
                        print(20*'-'+'Enter:'+20*'-'+'\n') 
                        # Insert a new seller
                        newSallerCode=sellerNumber('(No.) of seller!\n(0)-Back to previous menu!')
                        clean()
                        if newSallerCode==0:# cancel change and return to previous menu
                            break
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{[change,newSallerCode]}')
                        print(f'SALE CHANGE {change}:\nSeller code: {sallerCode} has been replaced by {newSallerCode}!')
#-----------------------------------------------------------------------------------------------------                        
                        print(20*'-'+'Enter:'+20*'-')
                        # Insert a new Customer 
                        newCustomer=customerNumber('(No) customer!\n(0)-Back to previous menu!')
                        newCustomer=str(newCustomer)
                        clean()
                        if newCustomer=='0':# cancel change and return to previous menu
                            break
                        customerCode=lv[index][2]
                        newCustomer='Customer:'+newCustomer
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{[change,newSallerCode,newCustomer]}')
                        print(f'SALE CHANGE {change}:\nSeller Code: {sallerCode} has been replaced by {newSallerCode}!\n'
                        f'Code: {customerCode} has been replaced by Customer: {newCustomer}!')
#----------------------------------------------------------------------------------------------------- 
                        print(20*'-'+'Enter:'+20*'-')
                        # insert new zone
                        newZone=customerZone('Indicate the zone\n(0)-Back to the previous menu!')
                        clean()
                        if newZone=='0': # cancel change and return to previous menu
                            break
                        zone=lv[index][3]
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{change},{newSallerCode},Customer:{newCustomer},{newZone}')
                        print(f'SALE CHANGE {change}:\nSeller Code: {sallerCode} has been replaced by {newSallerCode}!\n'
                        f'Code: {customerCode} has been replaced by Customer: {newCustomer}!\n'
                        f'Zone: {zone} has been replaced by :{newZone}!')
#----------------------------------------------------------------------------------------------------- 
                        print(20*'-'+'Enter:'+20*'-')
                        # insert new date
                        newDate= valDate('The date!\n(0)-Back to the previous menu!')
                        if newDate=='0':# cancel change and return to previous menu
                            break
                        date=lv[index][4]
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{change},{newSallerCode},{newCustomer},{newZone},{newDate}')
                        print(f'SALE CHANGE {change}:\nSeller Code: {sallerCode} has been replaced by {newSallerCode}!\n'
                        f'Code: {customerCode} has been replaced by Customer: {newCustomer}!\n'
                        f'Zone: {zone} has been replaced by :{newZone}!\n'
                        f'Date: {date} has been replaced by :{newDate}!\n')
#----------------------------------------------------------------------------------------------------- 
                        print(20*'-'+'Enter:'+20*'-')
                        # Insert a new product
                        newProductCode= valProduct('The product code\n(0)-Go back to the previous menu!')
                        if newProductCode=='0':# cancel change and return to previous menu
                            break
                        productCode=lv[index][5]
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{change},{newSallerCode},{newCustomer},{newZone},{newDate},{newProductCode}')
                        print(f'SALE CHANGE {change}:\nSeller Code: {sallerCode} has been replaced by {newSallerCode}!\n'
                        f'Code: {customerCode} has been replaced by Customer: {newCustomer}!\n'
                        f'Zone: {zone} has been replaced by :{newZone}!\n'
                        f'Date: {date} has been replaced by :{newDate}!\n'
                        f'Product Code: {productCode} has been replaced by  :{newProductCode}!')
#----------------------------------------------------------------------------------------------------- 
                        print(20*'-'+'Enter:'+20*'-')
                        # insert new quantity
                        newQuantity=valQuantity('The quantity\n(0)-Back to the previous menu!')
                        if newQuantity==0:# cancel change and return to previous menu
                            break
                        quantity=lv[index][6]
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{change},{newSallerCode},{newCustomer},{newZone},{newDate},{newProductCode},{newQuantity}')
                        print(f'SALE CHANGE {change}:\nSeller Code: {sallerCode} has been replaced by {newSallerCode}!\n'
                        f'Code: {customerCode} has been replaced by Customer: {newCustomer}!\n'
                        f'Zone: {zone} has been replaced by :{newZone}!\n'
                        f'Date: {date} has been replaced by :{newDate}!\n'
                        f'Product Code: {productCode} has been replaced by  :{newProductCode}!'
                        f'Quantity: {quantity} has been replaced by :{newQuantity}!\n')
#----------------------------------------------------------------------------------------------------- 
                        print(20*'-'+'Enter:'+20*'-')
                        # insert new purchase amount
                        newSalesValue= valSaleValue('The value of the sale\n(0)-Back to previous menu!')
                        if newSalesValue==0:# cancel change and return to previous menu
                            break
                        salesValue=lv[index][7]
                        print(f'You chose to change sale: {change}!\n')
                        print(header[0])
                        print(lv[index])
                        print(f'{change},{newSallerCode},{newCustomer},{newZone},{newDate},{newProductCode},{newQuantity},{newSalesValue}')
                        print(f'SALE CHANGE {change}:\nSeller Code: {sallerCode} has been replaced by {newSallerCode}!\n'
                        f'Code: {customerCode} has been replaced by Customer: {newCustomer}!\n'
                        f'Zone: {zone} has been replaced by :{newZone}!\n'
                        f'Date: {date} has been replaced by :{newDate}!\n'
                        f'Product Code: {productCode} has been replaced by  :{newProductCode}!'
                        f'Quantity: {quantity} has been replaced by :{newQuantity}!\n'
                        f'Sales Value: {salesValue} has been replaced by :{newSalesValue}!\n')
#----------------------------------------------------------------------------------------------------- 
#                       # insert the new record by the position of the index variable
                        newSalesId= change
                        newLv=[newSalesId, newSallerCode,newCustomer,newZone,newDate, newProductCode, newQuantity,newSalesValue]
                        lv[index]=newLv 
                        # open file for writing and rewrite the entire lv list 
                        file = open("07-Data/SalesRecords.csv", "w")
                        # write header
                        file.write(f"SalesNumber;SallerCode;NumberCustomer;Zone;Date;ProductCode;Quantity;Price;\n") 
                        for i in range(len(lv)): # go through the list
                            file.write(f"{lv[i][0]};{lv[i][1]};{lv[i][2]};{lv[i][3]};{lv[i][4]};{lv[i][5]};{lv[i][6]};{lv[i][7]};\n") 
                        file.close()
                        print(f'Sale nr :{change}, has been changed! successfully')
            except Exception: 
                print(20*'-'+'You chose option 4-Change'+20*'-')
                print('\nValue entered is not valid!\n')
#-----------------------------------------------------------------------------------------------------   
# delete the sale by its number
    elif opc == 5:
        clean()
        print(20*'-'+'You chose option 5-Delete'+20*'-')
        while True:
            try:
                remove= valPositiveInteger('Enter:\n(No.) of the sale to be deleted!\n(0)-return to the previous menu!')
                if remove==0:# back to previous menu
                    clean()
                    break
                elif lv[-1][0]<remove:# checks if the entered sales number is greater than the last sale
                    clean()
                    print(20*'-'+'You chose option 5-Delete'+20*'-')
                    print(f'Sale {remove} does not exist!')
                elif (lv[-1][0]>remove) and (remove in range(1,lv[-1][0],1)):# checks if the entered sales number is valid less than the last sale and if it has already been deleted
                    clean()
                    print(20*'-'+'You chose option 5-Delete'+20*'-')
                    print(f'Sale {remove}, has been deleted!') 
                for i in lv:
                    if i[0]==remove:# delete selected sale
                        index=lv.index(i)
                        clean()
                        print(20*'-'+'You chose option 5-Delete'+20*'-')
                        print(f'Selected the sale {remove}:\n{header}\n{lv[index]}\n')
                        try:# confirmation of deletion
                            confirmation=valPositiveInteger(f'Do you really want to delete sale nº{remove}?\n'
                            f'\nEnter (1) to confirm (0) to cancel!')
                            if confirmation==0:
                                print('Deletion has been cancelled!')
                                break
                            elif confirmation==1:
                                clean()
                                lv.pop(index)# removes the element from the position specified by the index
                                print(f'The record of the sale nº : {remove}, has been deleted!\n')
                                break            
                        except Exception:
                            print(f'Do you really want to delete the {remove} sale?\nEnter (1) to confirm (0) to cancel!') 
#----------------------------------------------------------------------------------------------------- 
                # Rewrite the entire list lv in the csv doc with the deletions made
                file = open("07-Data/SalesRecords.csv", "w")# open file for writing
                file.write(f"SalesNumber;SallerCode;NumberCustomer;Zone;Date;ProductCode;Quantity;Price;\n")  # write the field headers
                for i in range(len(lv)): # percorre a lista
                    file.write(f"{lv[i][0]};{lv[i][1]};{lv[i][2]};{lv[i][3]};{lv[i][4]};{lv[i][5]};{lv[i][6]};{lv[i][7]};\n") 
                file.close() 
            except Exception:
                print(f' Sale {remove}, not valid!')