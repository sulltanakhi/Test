budget=input('Enter your budget')
workers=input('Enter amount of workers')
while True:
    try:
        budget=int(budget)
        workers=int(workers)
        total=budget/workers
        print(total)
        break
    except ZeroDivisionError:
        print('can not divide by zero')
        workers=input('Enter amount of workers')

    except:
        workers=input('Enter amount of workers as number') 
        budget=input('Enter your budget as number')  
