
def CI(P,i,n):
    FV = P * ((1 + i) ** n)
    return FV

print(CI(200,0.02,8))


def CI1(FV,i,n):
    PV = FV * ((1+i) ** -n)
    return PV

print(CI1(200,0.02,8))
