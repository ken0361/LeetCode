def isPalindrome(x):

    if x < 0:
        return False
    m = x
    z = 0
    while x > 0:
        y = x%10
        x = x//10
        z = z*10 + y
    
    if m == z:
        return True
    else:
        return False