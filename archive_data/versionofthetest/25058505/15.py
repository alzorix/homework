def P(inter):
    return 15<= inter<=40
def Q(inter):
    return 21<= inter<=63

def check(inter):
    return A<=inter<=A1
GOOD = None

A_ = list()
for A in range(100):
    for A1 in range(A+1,100):
      F = True
      x = 0


      while x !=100.0:

        if (P(x))<= (((Q(x)) and (not(check(x))))  <= (not(P(x)))      ):
            None
        else:
            F = False
            break

        x +=0.5
      if F:
          A_.append(A1- A)




print(min(A_))

