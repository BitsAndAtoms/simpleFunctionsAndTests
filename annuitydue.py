#simple annuity due

def SAD(PMT,i,n):
    FVn_due = PMT * ((((1+i) ** n) - 1) / i) * (1+i)
    return FVn_due
#print(SAD(200,0.02,5))

def SAD1(PMT,i,n):
    PVn_due = PMT * ((1 - (1 +i) ** -n) / i) * (1 + i)
    return PVn_due

#print(SAD1(200,0.02,5))