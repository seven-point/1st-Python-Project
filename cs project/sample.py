def address():
    print('\n\nThis is the portal to enter your shipment address')
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
        address()
address()
