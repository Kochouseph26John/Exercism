def is_armstrong_number(number):
    n=number
    s=0
    l=len(str(number))
    while n!=0:
        s=s+((n%10)**l)
        n=n//10
    if s == number:
        return True
    return False