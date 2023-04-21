from scipy import fft

def strtolist(x):
    ans = []
    for i in reversed(x):
        ans.append(int(i))
    return ans

def fill(n , m):
    if len(n) < m:
        for _ in range(m-len(n)):
            n.append(0)
    return n
    


        
    

def Product(n , m):
    if not isinstance(n , (int , float)):
        raise Exception("Invalid Input n should be int")
    if not isinstance(m , (int , float)):
        raise Exception("Invalid Input m should be int")
    
    neg1 , neg2 = 0 , 0
    if n < 0:
        neg1 = 1
    if m < m:
        neg2= 1

    n = strtolist(str(abs(n)))
    m = strtolist(str(abs(m)))
    
    exp_digits = len(n) + len(m)

    n = fill( n , exp_digits)
    m = fill(m , exp_digits)

    fft_n = fft.fft(n)
    fft_m = fft.fft(m)


    prod = fft_m * fft_n

    prod = fft.ifft(prod)

    ans, ex = 0, 0
    for i in prod:
        ans += (i.real) * (10**ex)
        ex += 1
    if (neg1 + neg2) % 2 == 0:
        print(f"Product of two number is {int(ans)}")
    else:
        print(f"Product of two number is -{int(ans)}")






if __name__ == "__main__":
    n = 12345678999999999999999999999999999999999999999999999999999
    m = 987654321
    Product(n , m)
    print(f"actual product is {n*m}")
