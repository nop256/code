import random
def MillersTest(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False

    s = 0
    d = x - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(20):
        a = random.randint(2, x - 2)
        x0 = pow(a, d, x)
        if x0 == 1 or x0 == x - 1:
            continue
        for _ in range(s - 1):
            x0 = pow(x0, 2, x)
            if x0 == x - 1:
                break
        else:
            return False
    return True

def is_prime_standard(n):
    
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def make_dig_num(num):
    n = ''
    for i in range(num):
        if i == 0:
            n += str(random.randint(1,9))
        else:
            n += str(random.randint(0,9))
    return int(n)

def main():
    n = 3
    prime = 0
    while n < 1000000:
        if MillersTest(n) and is_prime_standard(n):
            prime += 1
        n += 1
            
    print(f'Prime Numbers from 3 - 1M: {prime}')
    
    print(f'Internet 200 Digit Number (Prime)): {MillersTest(76160531580539578272215259458243346429817650967517657358344277633701887061356757178944563951030068757588274100840106950722557642786309000379829787758539044970380917163726082032878235071559410586585403)}')
    
    print(f'Internet Generated 100 * 100 Digit Number (Not Prime): {MillersTest(9324303359159011168963314535729517449119914617877989955733298899762833147901943456500047482206930569 * 7183944682521116281144976370476422005663725538156933743494810382497151342657552529548302106536855729)}')

    n = make_dig_num(200)
    print(f'Self-Generated 200 Digit Number (Could be Prime...): {MillersTest(n)}')

    n = make_dig_num(100)
    m = make_dig_num(100)
    print(f'Self-Generated 100 * 100 Digit Number (Not Prime): {MillersTest(n * m)}')
    
main()
    