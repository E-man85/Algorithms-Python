# "clears" the console to be used throughout the program
def clean(): 
    print("\n" * 50)
# -----------------------------------------------------------------------------
# menu entry validation
def MenuEntryValue(msg):
    entMenu=0
    entok = False
    while not entok:
        try:
            entok=True
            entMenu= int(input(msg))
            if entMenu > 5 :
                print(f'The chosen {entMenu} option is not a Menu feature!')
                entok= False
            if entMenu < 0:
                print(f'The chosen {entMenu} option is not a Menu feature!')
                entok= False
        except:
            entok= False
            print('Option is not valid!')
    return entMenu
# -----------------------------------------------------------------------------
# Provided functions: Insert / Consult / List / Change / Delete
def menu():
    print(20*'-'+'WELCOME'+20*'-'+'\n')
    print(20*'-'+'Sales System'+20*'-'+'\n')
    print('1-Insert\n'+'2-Consult\n3-List\n4-Change\n5-Delete\n0-Out')
    return MenuEntryValue('Choose an option!')
# -----------------------------------------------------------------------------
# Date (string com formato “dd/mm/aaaa”)
def valDate(msg):
    dateok = False
    while not dateok:
        dateok=True
        try:
            date = input(msg)  
            if date=='0':
                clean()
                print('Registration cancelled!')
                break
            day, month, year = map(int, date.split('/'))
            if (day < 1):
                clean()
                print(f'The day {day} is not valid!')
                dateok=False
            elif year!=2022:
                clean()
                print(f'Year entered is not valid, only sales from the year 2022 are allowed!')
                dateok=False
            elif (month>12) or (month<1):
                clean()
                print(f'The month {month} is not valid!')
                dateok=False
            # Months with 31 days
            elif (month == 1 or month == 3 or month == 5 or month == 7 or  month == 8 or month == 10 or month == 12):
                if (day <= 31):
                    dateok = True
                else:
                    clean()
                    print(f'Invalid date: for the month {month}, the day {day}, is not valid!')
                    dateok = False
            # Months with 30 days
            elif (month == 4 or month == 6 or month == 9 or month == 11):
                if (day <= 30):
                    dateok = True
                else:
                    clean()
                    print(f'Invalid date: for the month {month}, the day {day}, is not valid!')
                    dateok = False
            # if the month is february, we need to know if the year is a leap year
            elif month == 2:
            # Test if it's leap year
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if (day <= 29):
                        dateok = True
                    elif (day <= 28):
                        dateok = True
                    else:
                        clean()
                        print('Invalid date!')
                        dateok = False
            else:
                clean()
                print('Invalid date!')
        except:
            clean()
            print('Date entered is not valid!\nEnter the date of sale in the format: dd/mm/yyyy')
            dateok= False
    return date
# -----------------------------------------------------------------------------
# function to validate customer number input
def customerNumber(msg):
    num=0
    numok=False
    while (not numok):
        numok=True
        try:
            num=int(input(msg))      
            if num<0:
                clean()
                print(f'Customer number {num} is not valid!')  
                numok=False    
        except:
            clean()
            print('Error: Invalid customer number!')
            numok=False
    return num
# -----------------------------------------------------------------------------
# function to validate on an integer
def valPositiveInteger(msg):
    num=0
    numok=False
    while (not numok):
        numok=True
        try:
            num=int(input(msg)) 
            if num<0:
                clean()
                print(f'Entered number: {num}, not valid!')  
                numok=False         
        except:
            clean()
            print("Error: re-enter the number!")
            numok=False
    return num
# -----------------------------------------------------------------------------
SellerCodeList=range(100,1000,100) # accepted seller codes
def sellerNumber(msg):
    sellerCode=1
    while (sellerCode!=0) and (sellerCode not in SellerCodeList):
        try:
            sellerCode= int(input(msg))
            if (sellerCode not in SellerCodeList) and (sellerCode!=0):
                clean()
                print(f'Seller {sellerCode} is not valid!') 
        except:
            clean()
            print('Wrong seller code, enter a 3-digit number! (eg: 100)')
    return sellerCode
# -----------------------------------------------------------------------------
def valProduct(msg):
    productok=False
    while not productok:
        productok=True
        try:
            countNumber=0
            countLetters=0
            productCode=input(msg).upper() 
            for i in productCode:
                if i.isdigit():
                    countNumber+=1
                elif i.isalpha():
                    countLetters+=1 
            if productCode=='0':
                clean()
                print('Registration cancelled!')
                break  
            elif (countLetters==3) and (countNumber==3):
                productok=True
            else:
                clean()
                print(f'Product code: {productCode} is not valid, the code supports 3 numbers and 3 letters!')
                productok=False
        except:
            clean()
            print('Product code is not valid!')
    return productCode
# -----------------------------------------------------------------------------
# Quantity (integer: 1 / 2 / 5 / 7 / …)
def valQuantity(msg):
    qutok= False
    while not qutok:
        qutok= True
        try:  
            qut=int(input(msg))
            if qut==0:
                print('Registration cancelled!')
                break
            elif qut < 1:
                clean()
                print(f'Quantity: {qut} is not valid !')
                qutok= False
        except:
            clean()
            print('Inserted value is not valid! Enter a number!')
            qutok= False
    return qut
# -----------------------------------------------------------------------------
# Sale Value (float €)
def valSaleValue(msg):
    vvok= False
    while not vvok:
        vvok= True
        try:  
            saleValue=float(input(msg))
            if saleValue==0:
                print('Registration cancelled!')
                break
            elif saleValue<1:
                clean()
                print(f'Inserted sales value: {saleValue}, not valid!')
                vvok= False
        except:
            clean()
            print('Value entered is not valid, enter a number!')
            vvok= False
    return saleValue
# -----------------------------------------------------------------------------
# Zone (string: North(“N”) / Center(“C”) / South(“S”) / Islands(“I”))
def customerZone(msg):
    zoneList= ['N','C','S','I']
    zoneok = False
    while not zoneok:   
        zone= input(msg)
        zone=zone.upper()   
        if zone  in zoneList:
            zoneok= True
        else:
            clean()
            print(f'Intruded zone {zone} is not valid!')
            zoneok= False
    return zone