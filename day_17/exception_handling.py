names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']



*nordic_countries , es , ru = names



try:
    choice = int(input('Enter 1 for Nordic , 2 for Estonia , 3 for Russia: '))

    if choice == 1:
        print('Nordic Countries: ' , nordic_countries)
    elif choice == 2:
        print('Estonia: ' , es)
    elif choice == 3:
        print('Russia: ' , ru)    
    else:
        print('Only 1 , 2 and 3')    
        
except ValueError as e:
    print('Invalid input type')

else:
    print('Selection Successful')

finally:
    print('Thank you for using the program')

















