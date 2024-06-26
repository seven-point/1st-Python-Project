 import mysql.connector as m
import matplotlib.pylab as plt
import numpy as n
con=m.connect(host="localhost",user="root",passwd="suraj",database="user")
if con.is_connected()==False:
    print("error")
cursor=con.cursor()
cursor.execute("select item from {}".format(login_username_in))
x=cursor.fetchall()
cursor.execute("select item_quantity from user.{}, ip.shoppe where item=name; ".format(login_username_in))
y=cursor.fetchall()
cursor.execute("select category from user.{}, ip.shoppe where item=name; ".format(login_username_in))
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
    
