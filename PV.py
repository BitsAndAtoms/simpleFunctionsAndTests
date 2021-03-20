
#present value of ordinary simple annuity

def OSA(PMT,i,n):
    PVn = PMT * ((1 -((1+i) ** -n)) / i)
    return PVn

#print(OSA(36000,0.03,80))

#ordinary general annuity

def OGA(PMT,p,n):
    PVg = PMT * ((((1 + p) ** n) - 1) / p)
    return PVg
#print(OGA(200,0.02,8))
#constant growth annuity
def CGA(PMT,i,k,n):
    PV = PMT * (((1 - ((1+k) ** n)) * ((1+i) ** -n)) / (i - k))
    return PV

#print(CGA(40000,0.02,0.04,8))