try: 
    num = int(input('Enter a number : '))
    result = 10 / num
    print(result)
except ValueError:
    print('Please enter a valid number !')
except ZeroDivisionError : 
    print('Cannot divide by zero !')
except Exception as e: 
    print(f'Something went wrong : {e}')
else :
    print('No error occured !')
finally:
    print('Always runs')
