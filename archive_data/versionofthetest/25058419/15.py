for A in range(0,999):

    ERROR = False
    for x in range(0,999):
        for y in range(0, 999):
            if( x<= 19 )or (y< 2*x + A -50) or (y > 17): # y< 2*x + A -50 - здесь нужны ли скобки?
                None
            else:
                ERROR = True
    if not(ERROR):
        print(A)
        exit()
#28