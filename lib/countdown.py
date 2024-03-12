import time
def countdown(n):
    n=int(n)
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    print('HAPPY NEW YEAR!')
def countdown_with_sleep(n):
    n=int(n)
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')