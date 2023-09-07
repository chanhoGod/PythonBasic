is_this_prime_number = 3

def is_prime_number(num: int):
    if num > 1:
        is_divisible = True
        for n in range(2, num):
            if num % n == 0:
                is_divisible = False
                print(f"{num}은 소수가 아님")
                break
        
        if is_divisible:
            print(f"{num}은 소수임")
        else:
            print(f"{num}은 소수가 아님")
    else:
        print(f"{num}은 소수가 아님")
        

is_prime_number(4)