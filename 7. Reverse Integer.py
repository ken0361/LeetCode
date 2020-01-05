def reverse(x):

    if x > 0:
        x = int(str(x)[::-1])
    else:
        x = int(str(abs(x))[::-1])*(-1)
    
    if x<2**31 and x>=(-1)*(2**31):
        return x
    else:
        return 0
