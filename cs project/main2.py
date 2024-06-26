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
    cursor.execute('select password from logindata where username={}'.fotmat(login_username_in))
    data_pass=cursor.fetchone()
  else:
    print('You have not yet registered with us!')
    return

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
  connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
  cursor=sql.cursor()

  cursor.execute('select username from logindata')
  data_username=cursor.fetchall()

  register_username=input("Enter a USERNAME:- ")
  register_pass=input("Enter a PASSWORD:- ")
  if register_username in data_username:
    print('This Username already exists.....')
    connect.close()
    return before_login()
  else: 
    register_mob=int(input('Enter your mob. no:- '))
    register_add=input('Enter your address:- ')
    register_email=input('Enter your E-mail id:- ')
    print('Registered Successfully!!')
    cursor.execute('insert into logindata(username,password,mob,address,email) values({},{},{},{},{},{})').format(register_username,register_pass,register_mob,register_add,register_email)
    connect_new=sql.connect(host='localhost',user='root',passwd='',database='')
    connect.commit()
    cursor=connect_new.cursor()
    cursor.execute('create table {} (srno. int AUTO_INCREMENT , date_of_purchase date,products varchar(75000000),category varchar(1500000000),quantity int)').format(register_username)
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
  connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
  cursor=sql.cursor()
  cursor.execute('select mob from logindata where username={}'.format(login_username_in))
  cur_mob=cursor.fetchone()
  cursor.execute('select add from logindata where username={}'.format(login_username_in))
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
  print('1. To make another order.')
  print('2. To visit Your orders.')
  print('3. LOGOUT ("Your information is safe with us with 64bit special encryption technology").')
  pay_responce=input('\nEnter your responce:- ')
  if pay_responce==1:
    return my_orders()
  elif pay_responce==2:
    return 
  elif pay_responce==3:
    print('You are sucessfully logged out!!!')
    return

def change_pass():
  print('Your current password is:- ')
  print(data_pass)
  pass_change=input('Enter your new password which you want to have:- ')
  pass_change_confirm=input('Enter your new password again:- ')
  if pass_change==pass_change_confirm:
    connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
    cursor=sql.cursor()
    cursor.execute('update login_info set password={} where username={}'.format(pass_change_confirm,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nPassword changed successfully!')
    return
  else:
    change_pass()

def before_login():
  print('\n1. To go to login window.')
  print('2. To go to register window.')
  before_login_responce=input('Enter your responce:- ')
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
    connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
    cursor=sql.cursor()
    cursor.execute('update login_info set mob={} where username={}'.format(mob_change_confirm,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nMob no. changed successfully!')
    return
  else:
    change_mob()

def change_email():
  print('Your current email-id is:- ')
  print(cur_email)
  email_change=input('Enter your new email-id which you want to have:- ')
  email_change_confirm=input('Enter your new email-id again:- ')
  if email_change==email_change_confirm:
    connect=sql.connect(host='localhost',user='root',passwd='',database='login_info')
    cursor=sql.cursor()
    cursor.execute('update login_info set email={} where username={}'.format(email_change_confirm,login_username_in))
    connect.commit()
    connect.close()
    print('\n\nEmail-id. changed successfully!')
    return
  else:
    change_email()

def del_cart():
  print('\n\nThis is a menu to delete items from your cart....')
  del_ans=='y'
  while del_ans=='y' or del_ans=='Y':
    del_product=input('Enter the name of product which you want to delete:- ')
    product_list.pop(product_list.index(del_product))
    print('\n\nItem Deleted Successfully.....')
    del_ans=input('Do You want to delete anymore? [Y/N]:- ')
  return 

  