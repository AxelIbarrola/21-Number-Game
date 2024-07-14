def validate_numbers():
    
    while True:
        try:
            
            amount_of_numbers = int(input('How many numbers do you wish to enter?: '))
        
            if  amount_of_numbers <= 0 or amount_of_numbers > 21:
                print('The number must be between 1-21')
            else:
                break
            
        except ValueError:
            print('The value must be a number.')
    
    return amount_of_numbers

