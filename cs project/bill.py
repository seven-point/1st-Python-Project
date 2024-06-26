def address():
    print('\n\nThis is the portal to enter your shipment address')
    user_address_1=input('Enter your flat number and building name: ')
    user_address_2=input('Enter your locality: ')
    user_address_3=input('Enter your town name: ')
    user_address_4=input('Enter your city name: ')
    user_address_5=input('Enter your state and pincode: ')
    user_address_6=input('Enter your landmark: ')
    print('I would like to repeat your address entered',user_address_1,user_address_2,user_address_3,user_address_4,user_address_5,user_address_6)
    c=input('Needed confirmation of address entered....(Y/N): ')
    if c=='Y' or c=='y':
        print('Thank you for the confirmation')
        print('Lets proceed towards the next step')
    else:
        print('Sorry for the inconvenience caused :-( ')
        print('We would like you to enter your address again')
        address()

def mobile():
    print('\n\nWe need your mobile number for a healthier contact between us')
    user_country_code=int(input('Enter your country code: '))
    user_mobile_no=int(input('Enter your mobile number: '))
    user_mobile=user_country_code+user_mobile_no
    print('The mobile number entered by you is ',user_mobile)
    mobile_response=input('Is this your Number.....(Y/N): ')
    if mobile_response=='Y' or mobile_response=='y':
        print('Thank you for the confirmation')
        print('Now we will proceed to the purchasing')
    else:
        print('Sorry for the inconvenience caused :-( ')
        print('We would like you to enter your mobile number again')
        mobile()

def prevorders():
    print('To check your previous purchasings with us')
    connect=sql.connect(host='localhost',user='root',passwd='',database='users')
    cursor=sql.cursor()
    cursor.execute('select * from {}'.format(login_username_in))
    prev_data=cursor.fetchall()
    for i in prev_data:
        print(i)

def extractorder1():
    connect=sql.connect(host='localhost',user='root',passwd='',database='products')
    cursor=sql.cursor()
    cursor.execute('select * from products where srno={}'.format(product_no_input))
    eodata=cursor.fetchall()
    saveorder()

def extractorder2():
    connect=sql.connect(host='localhost',user='root',passwd='',database='products')
    cursor=sql.cursor()
    cursor.execute('select * from products where item={}'.format(product_name_input))
    eodata=cursor.fetchall
    saveorder()
                   
def saveorder():
  connect=sql.connect(host='localhost',user='root',passwd='',database='users')
  cursor=sql.cursor()
  cursor.execute('insert into {} values ({})'.format(login_username_in,eodata))

def printbill():
    total_price=0
    for i in product_list:
        connect=sql.connect(host='localhost',user='root',passwd='',database='users')
        cursor=sql.cursor()
        cursor.execute('select category from products where item={}'.format(i))
        catdata=cursor.fetchall()
        cursor.execute('select price from products where item={}'.format(i))
        pricedata=cursor.fetchall()
        for j in pricedata:
            total_price+=int(j)
        print(i,',',catdata,',',pricedata)
        print('/n')
    print('Your total amount to be paid is: ',total_price)
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------')

                 
