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