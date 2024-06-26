import mysql.connector as sql
product_list=[]
another='y'
import matplotlib.pylab as plt
import numpy as n

def login_sql():
  connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
  cursor=sql.cursor()
  
  cursor.execute('select name from register')
  data_username=cursor.fetchall()
  
  login_username_in=input("Enter your USERNAME:- ")
  pass_pass_in=input("Enter the PASSWORD:- ")
  if login_username_in in data_username:
    cursor.execute('select password from register where name={}'.format(login_username_in))
    data_pass=cursor.fetchone()
  else:
    print('You have not yet registered with us!')
    return before_login()

  if login_username_in in data_username and pass_pass_in==data_pass:
    print('Login Success!! ')
    connect.close()
    return afterlogin()
  else:
    print('Wrong password!!')
    print('Please try again...\n\n')
    connect.close()
    login_sql()

def register():
  connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
  cursor=sql.cursor()

  cursor.execute('select name from register')
  data_username=cursor.fetchall()

  register_username=input("Enter a USERNAME:- ")
  register_pass=input("Enter a PASSWORD:- ")
  if register_username in data_username:
    print('This Username already exists.....')
    connect.close()
    return before_login()
  else:
    address()
    mobile()
    register_email=input('Enter your E-mail id:- ')
    print('Registered Successfully!!')
    cursor.execute('insert into register(name,password,mob,address,email) values({},{},{},{},{})').format(register_username,register_pass,user_mob,user_address,register_email)
    connect_new=sql.connect(host='localhost',user='root',passwd='',database='')
    connect.commit()
    cursor=connect_new.cursor()
    cursor.execute('create table {} (srno. int AUTO_INCREMENT , date_of_purchase date,products varchar(75000000),category varchar(1500000000))').format(register_username)
    connect_new.commit()
    connect.close()

def my_orders():
  print('Anytime if you want to get back to main menu please type "CANCEL"')
  connect=sql.connect(host='localhost',user='root',passwd='',database='products')
  cursor=sql.cursor()
  print('\nThis is the menu to select what to buy!!')
  print('\n\n1.To directly type the name of the product you want.')
  print('2.To show all the categories of product available with us.')
  print('3.To show all the products available with us.')
  x=int(input('Enter your response:- '))
  if x==1:
    cursor.execute('Select srno. from products')
    data=cursor.fetchall()
    print('\n 1. To enter the product serial no.:- ')
    print('\n 2. To enter the product name:- ')
    order_2_input=int(input('Enter your responce:- '))
    if order_2_input==1:
      cursor.execute('Select srno. from products')
      data=cursor.fetchall()
      while another=='y' or another=='Y':
        product_no_input=input('Enter the product no.:- ')
        if product_no_input=='CANCEL':
            return afterlogin()
        if product_no_input in data:
          cursor.execute('Select name from products where srno={}'.format(product_no_input))
          product_name=cursor.fetchall()
          product_list=product_list + [product_name]
          print('You have entered the product no. as ',product_no_input)
          another=input('Do you want to add some more products[Y/N]? :- ')
        else:
          print('Wrong input!!\n\n')
          continue
    elif order_2_input==2:
      cursor.execute('Select name from products')
      data=cursor.fetchall()
      while another=='y' or another=='Y':
        product_name_input=input('Enter the product name.:- ')
        if product_name_input=='CANCEL':
            return afterlogin()
        if product_name_input in data:
          product_list=product_list + [product_name_input]
          print('You have entered the product name as ',product_name_input)
          another=input('Do you want to add some more products[Y/N]? :- ')
        else:
          print('Wrong product name!!')
          continue
    elif order_2_input=='CANCEL':
      return afterlogin()
    else:
      print('Invalid input')

  elif x==2:
    cat_ans='y'
    while cat_ans=='y' or cat_ans=='Y':
      cat_select()
      cat_ans=input('Do you want to select any other category[Y/N]:- ')

  elif x==3:
    data=cursor.fetchall()
    for e in data:
      print(e)
    print('\n 1. To enter the product serial no.:- ')
    print('\n 2. To enter the product name:- ')
    order_2_input=int(input('Enter your responce:- '))
    if order_2_input==1:
      cursor.execute('Select srno. from products')
      data=cursor.fetchall()
      while another=='y' or another=='Y':
        product_no_input=input('Enter the product no.:- ')
        if product_no_input in data:
          product_list=product_list + [product_no_input]
          print('You have entered the product no. as ',product_no_input)
          another=input('Do you want to add some more products[Y/N]? :- ')
        elif product_no_input=='CANCEL':
            return afterlogin()
        else:
          print('Wrong input!!\n\n')
          continue
    elif order_2_input==2:
      cursor.execute('Select name from products')
      data=cursor.fetchall()
      while another=='y' or another=='Y':
        product_name_input=input('Enter the product name.:- ')
        if product_name_input in data:
          product_list=product_list + [product_name_input]
          extractorder2()
          print('You have entered the product name as ',product_name_input)
          another=input('Do you want to add some more products[Y/N]? :- ')
        elif product_name_input=='CANCEL':
            return afterlogin()
        else:
          print('Wrong product name!!')
          continue
    elif order_2_input=='CANCEL':
      return afterlogin()
    else:
      print('Invalid input')

def cat_select():
  cursor.execute('select distinct category from products')
  data=cursor.fetchall()
    
  print('Following are the categories of products available with us:--  ')
  for v in data:
    print(v)
  category_select=input('Enter the category you want to select:- ')
    
  print('\nAll the products avaiable with us within',category_select,'category are:-')
  cursor.execute("select * from products where category={}".format(category_select))
  data2=cursor.fetchall()
  for i in data2:
    print(i)
  
  print('\n 1. To enter the product serial no.:- ')
  print('\n 2. To enter the product name:- ')
  order_2_input=int(input('Enter your responce:- '))
  if order_2_input==1:
    cursor.execute('Select srno. from products')
    data=cursor.fetchall()
    while another=='y' or another=='Y':
      product_no_input=input('Enter the product no.:- ')
      if product_no_input=='CANCEL':
            return afterlogin()
      if product_no_input in data:
        product_list=product_list + [product_no_input]
        extractorder1()
        print('You have entered the product no. as ',product_no_input)
        another=input('Do you want to add some more products[Y/N]? :- ')
      else:
        print('Wrong input!!\n\n')
        continue
  elif order_2_input==2:
    cursor.execute('Select name from products')
    data=cursor.fetchall()
    while another=='y' or another=='Y':
      product_name_input=input('Enter the product name.:- ')
      if product_name_input=='CANCEL':
            return afterlogin()
      if product_name_input in data:
        product_list=product_list + [product_name_input]
        extractorder2()
        print('You have entered the product name as ',product_name_input)
        another=input('Do you want to add some more products[Y/N]? :- ')
      else:
        print('Wrong product name!!')
        continue

def afterlogin():
  connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
  cursor=sql.cursor()
  cursor.execute('select mob from register where name={}'.format(login_username_in))
  cur_mob=cursor.fetchone()
  cursor.execute('select add from register where name={}'.format(login_username_in))
  cur_add=cursor.fetchone()
  connect.close()
  print('Your current mob no. is:- ',cur_mob)
  print('Your current address with us is:- ',cur_add)
  print('\n\n1. To check your previous orders')
  print('2. To change the password for login.')
  print('3. To change your address registered with us.')
  print('4. To change your current Mob no. registered with us.')
  print('5. To change your current email-id registered with us.')
  print('6. To proceed for purchasing')
  afterlogin_responce=input('Enter your choice:- ')
  if afterlogin_responce==1:
    prevorders()
  elif afterlogin_responce==2:
    change_pass()
  elif afterlogin_responce==3:
    change_add()
  elif afterlogin_responce==4:
    change_mob()
  elif afterlogin_responce==5:
    change_email()
  elif afterlogin_responce==6:
    my_orders()
  else:
    print('Wrong Input...')
    return afterlogin()

def payment():
  print('For the time being we are only available with Payment on Deliery!! ....')
  print('Your product will reach to you within some specified time period.....')
  print('You will get regular update on your mobile no.')
  print('\n\nTHANK YOU FOR CHOOSING AS YOUR SHOPPING PARTNER.....\n\n')
  print('1. To visit your homepage.')
  print('2. LOGOUT ("Your information is safe with us with 64bit special encryption technology").')
  pay_responce=input('\nEnter your responce:- ')
  if pay_responce==1:
    return afterlogin()
  elif pay_responce==2:
    print('You are sucessfully logged out!!!')
    return before_login()
    
def change_pass():
  print('Your current password is:- ')
  print(data_pass)
  pass_change=input('Enter your new password which you want to have:- ')
  pass_change_confirm=input('Enter your new password again:- ')
  if pass_change==pass_change_confirm:
    connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
    cursor=sql.cursor()
    cursor.execute('update register set password={} where name={}'.format(pass_change_confirm,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nPassword changed successfully!')
    return afterlogin
  else:
    change_pass()

def before_login():
  print('\n1. To go to login window.')
  print('2. To go to register window.')
  before_login_responce=input('Enter your response:- ')
  if before_login_responce==1:
    login_sql()
  elif before_login_responce==2:
    register()
  else:
    print('Wrong input...')
    return before_login()

def change_mob():
  print('Your current mob no. is:- ')
  print(cur_mob)
  mob_change=input('Enter your new mob no. which you want to have:- ')
  mob_change_confirm=input('Enter your new mob no. again:- ')
  if mob_change==mob_change_confirm:
    connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
    cursor=sql.cursor()
    cursor.execute('update login_info set mob={} where name={}'.format(mob_change_confirm,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nMob no. changed successfully!')
    return afterlogin()
  else:
    change_mob()

def del_cart():
  print('\n\nThis is a menu to delete items from your cart....')
  del_ans=='y'
  while del_ans=='y' or del_ans=='Y':
    del_product=input('Enter the name of product which you want to delete:- ')
    product_list.pop(product_list.index(del_product))
    print('\n\nItem Deleted Successfully.....')
    del_ans=input('Do You want to delete anymore? [Y/N]:- ')
  return printbill()

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
      change_add2()

def change_email():
  print('Your current email-id is:- ')
  print(cur_email)
  email_change=input('Enter your new email-id which you want to have:- ')
  email_change_confirm=input('Enter your new email-id again:- ')
  if email_change==email_change_confirm:
    connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
    cursor=sql.cursor()
    cursor.execute('update login_info set email={} where name={}'.format(email_change_confirm,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nEmail-id. changed successfully!')
    return afterlogin()
  else:
    change_email()

def change_add():
  print('Your current shipment address is:- ')
  print(cur_add)
  user_address_1=input('Enter your flat number and building name: ')
  user_address_2=input('Enter your locality: ')
  user_address_3=input('Enter your town name: ')
  user_address_4=input('Enter your city name: ')
  user_address_5=input('Enter your state and pincode: ')
  user_address_6=input('Enter your landmark: ')
  user_address=user_address_1+' '+user_address_2+' '+user_address_3+' '+user_address_4+' '+user_address_5+' '+user_address_6
  print('I would like to repeat your address entered',user_address)
  c=input('Needed confirmation of address entered....(Y/N): ')
  if c=='Y' or c=='y':
    connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
    cursor=sql.cursor()
    cursor.execute('update login_info set address={} where name={}'.format(user_address,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nAddress changed successfully!')
    return afterlogin()
  else:
    change_add()
    
def change_add2():
  user_address_1=input('Enter your flat number and building name: ')
  user_address_2=input('Enter your locality: ')
  user_address_3=input('Enter your town name: ')
  user_address_4=input('Enter your city name: ')
  user_address_5=input('Enter your state and pincode: ')
  user_address_6=input('Enter your landmark: ')
  user_address=user_address_1+' '+user_address_2+' '+user_address_3+' '+user_address_4+' '+user_address_5+' '+user_address_6
  print('I would like to repeat your address entered',user_address)
  c=input('Needed confirmation of address entered....(Y/N): ')
  if c=='Y' or c=='y':
      print('Thank you for the confirmation')
      print('Lets proceed towards the next step')
  else:
      print('Sorry for the inconvenience caused :-( ')
      print('We would like you to enter your address again')
      change_add2()
  
def change_mob2():
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
      change_mob2()
  
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
      change_mob2()

def prevorders():
  print('To check your previous purchasings with us')
  connect=sql.connect(host='localhost',user='root',passwd='',database='user')
  cursor=sql.cursor()
  cursor.execute('select * from {}'.format(login_username_in))
  prev_data=cursor.fetchall()
  for i in prev_data:
      print(i)
  graph()

def extractorder():
  connect=sql.connect(host='localhost',user='root',passwd='',database='ip')
  cursor=sql.cursor()
  for i in product_list:
    cursor.execute('select name,price,category from products where name={}'.format(i))
    eodata=cursor.fetchall
    saveorder()
                   
def saveorder():
  connect=sql.connect(host='localhost',user='root',passwd='',database='user')
  cursor=sql.cursor()
  cursor.execute('insert into {}(item,price,category) values ({})'.format(login_username_in,eodata))

def printbill():
  total_price=0
  for i in product_list:
      connect=sql.connect(host='localhost',user='root',passwd='',database='user')
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
  print('\n\n 1.Delete an item from the cart')
  print('2.Add an item to the cart')
  print('3.Confirm the bill')
  bill_response=int(input('Enter your response: '))
  if bill_response==1:
    del_cart()
  if bill_response==2:
    my_orders()
  if bill_response==3:
    payment()
  extractorder()


def graph():
  con=sql.connect(host="localhost",user="root",passwd="suraj",database="user")
  if con.is_connected()==False:
    print("error")
  cursor=con.cursor()
  cursor.execute("select item from RK_Singh;")
  x=cursor.fetchall()
  cursor.execute("select item_quantity from user.RK_Singh, ip.shoppe where item=name; ")
  y=cursor.fetchall()
  cursor.execute("select category from user.RK_Singh, ip.shoppe where item=name; ")
  z=cursor.fetchall()
  def bar():
    plt.title("History Of Product")
    a=['Apples','amul butter','choco lava cake','alu bhujia','cornflakes']
    b=[6,2,1,3,5]
    plt.bar(a,b)
    plt.xlabel("Item Name")
    plt.ylabel("Item Quantity")
    plt.show()
  def pie():
    plt.title("Category")
    expl=[0.2,0,0,0,0]
    plt.pie(y,labels=x,explode=expl,autopct="%3d%%")
    plt.show()
  #__main__
  print("What type of graph you would like to see?")
  print("[1] Product")
  print("[2] Category")
  print("[3] Both")
  a=int(input("enter your choice {1,2,3}"))
  if a==1:
    bar()
  elif a==2:
    pie()
  elif a==3:
    bar()
    pie()
  else:
    print("sorry")
#__main__
print('                                ☺ WELCOME TO SSV SHOPPING SITE ☺                                       ')
print('                    ♦ YOUR ALL IN ONE GENERAL STORE AT YOUR FINGERTIPS ♦                        ')
before_login()
printbill()
