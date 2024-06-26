import mysql.connector as sql
product_list=[]
another='y'

def login_sql():
  connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
  cursor=sql.cursor()
  
  cursor.execute('select username from logindata')
  data_username=cursor.fetchall()
  
  login_username_in=input("Enter your USERNAME:- ")
  pass_pass_in=input("Enter the PASSWORD:- ")
  if login_username_in in data_username:
    cursor.execute('select password from logindata where username={}'.format(login_username_in))
    data_pass=cursor.fetchone()
  else:
    print('You have not yet registered with us!')
    return

  if login_username_in in data_username and pass_pass_in==data_pass:
    print('Login Success!! ')
    return afterlogin()
  else:
    print('Wrong password!!')
    print('Please try again...\n\n')
    login_sql()

def register():
  connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
  cursor=sql.cursor()

  register_username=input("Enter a USERNAME:- ")
  register_pass=input("Enter a PASSWORD:- ")
  if register_username in login_username:
    print('This Username already exists.....')
    return register()
  else: 
    print('Registered Successfully!!')
    cursor.execute('insert into logindata(username,password) values({},{})'.format(register_username,register_pass))
    connect.commit()

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
    cursor.execute('Select srno from products')
    data=cursor.fetchall()
    print('\n 1. To enter the product serial no.:- ')
    print('\n 2. To enter the product name:- ')
    order_2_input=int(input('Enter your response:- '))
    if order_2_input==1:
          cursor.execute('Select srno. from products')
          data=cursor.fetchall()
          while another=='y' or another=='Y':
            product_no_input=input('Enter the product no.:- ')
            if product_no_input=='CANCEL':
                return afterlogin()
            if product_no_input in data:
              product_list=product_list + [product_no_input]
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
    order_2_input=int(input('Enter your response:- '))
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
          print('You have entered the product name as ',product_name_input)
          another=input('Do you want to add some more products[Y/N]? :- ')
        if product_name_input=='CANCEL':
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
  order_2_input=int(input('Enter your response:- '))
  if order_2_input==1:
    cursor.execute('Select srno. from products')
    data=cursor.fetchall()
    while another=='y' or another=='Y':
      product_no_input=input('Enter the product no.:- ')
      if product_no_input=='CANCEL':
            return afterlogin()
      if product_no_input in data:
        product_list=product_list + [product_no_input]
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

def afterlogin():
  print('\n\n1. To check your previous orders')
  print('2. To check the current cart value')
  print('3. To proceed for purchasing')
  afterlogin_response=input('Enter your choice:- ')
  if afterlogin_response==1:
  elif afterlogin_response==2:
  elif afterlogin_response==3:
    my_orders()

def payment():
  print('For the time being we are only available with Payment on Delivery!! ....')
  print('Your product will reach to you within a specified time period.....')
  print('You will get regular update on your mobile no.')
  print('\n\nTHANK YOU FOR CHOOSING AS YOUR SHOPPING PARTNER.....\n\n')
  print('1. To make another order.')
  print('2. To visit Your orders.')
  print('3. LOGOUT ("Your information is safe with us with 64bit special encryption technology").')
  pay_response=input('\nEnter your response:- ')
  if pay_response==1:
    return my_orders()
  elif pay_response==2:
    return 
  elif pay_response==3:
    print('You are sucessfully logged out!!!')
    return

