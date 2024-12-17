budget=input('Enter your budget')
workers=input('Enter amount of workers')
while True:
    try:
        budget=int(budget)
        workers=int(workers)
        total=budget/workers
        print(total)
        break
