numbers = []
from random import randint
from validations import validate_numbers

def main():
    
    numbers = [0]
    user_win = False
    
        
    print('\nPlayer 2 is Computer.\n')
    print('MENU'.center(50, '-'))
     
    while True:   
        option = input('''
    1. Take the first chance.
    2. Take the second chance.
    Select an option: ''')
            
        match option:
            case '1':
                while not 21 in numbers:
                    amount_of_numbers = validate_numbers()
                    
                    for i in range(amount_of_numbers):
                        numbers.append(numbers[-1] + 1)
                    
                    print('\nOrder of inputs after your turn is: ')
                    print(numbers[1:])
                    
                    amount_of_numbers_pc = randint(1, 5)
                    
                    for i in range(amount_of_numbers_pc):
                        numbers.append(numbers[-1] + 1)
                    
                    print('\nOrder of inputs after computer\'s turn is: ')
                    print(numbers[1:])
                    
                    if 21 in numbers:
                        user_win = True
                break
            
            case '2':
                while not 21 in numbers:
                    amount_of_numbers_pc = randint(1, 5)
                    
                    for i in range(amount_of_numbers_pc):
                        numbers.append(numbers[-1] + 1)
                    
                    print('\nOrder of inputs after computer\'s turn is: ')
                    print(numbers[1:])
                    
                    if 21 in numbers:
                        user_win = True
                    
                    amount_of_numbers = validate_numbers()
                    
                    for i in range(amount_of_numbers):
                        numbers.append(numbers[-1] + 1)
                    
                    print('\nOrder of inputs after your turn is: ')
                    print(numbers[1:])
                break
            
            case _:
                print('Invalid option, try again')
                  
    
    if user_win:
        print(
'''CONGRATULATIONS!!!
YOU WON!''')
    
    else:
        print('The computer won.')
        
        

main()