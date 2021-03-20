#future value of simple ordinary annuity
#PMT= regular periodic payment
#i = interest rate per period
#n = total number of conversion period
def OSA(PMT,i,n):
    FV = PMT * ((((1+i) ** n) - 1) / i)
    return FV

#print("present value of simple ordinary annuity: ",OSA(36000,0.03,80))

#Future value of Ordinary General annuity
def OGA(PMT,i2,n):
    FV = PMT * ((((1 + i2) ** n) - 1) / i2)
    return FV

#print("Ordinary General annuity: ",OGA(100,0.008165,12))

#constant growth annuity
def CGA(PMT,i,k,n1):
    FV1 = PMT * (((1+i) ** n1) - ((1+k) ** n1) / (i - k))
    return FV1

#print("constant growth annuity: ",CGA(2000,0.03,0.05,5))

