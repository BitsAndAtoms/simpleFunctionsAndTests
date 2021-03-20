#ordinary simple perpetuity

def OSP(PMT,i):
    PV = PMT / i
    return PV

#ordinary general perpetuity

def OGP(PMT,i,c):
    PVg = PMT / ((1 + i) ** c) - 1
    return PVg

#simple perpetuity due
def SPD(PMT,i):
    PV_due = PMT + PMT / i
    return PV_due

#General perpetuity due
def GPD():
    PVg_due = PMT + PMT / ((1 + i) ** c) - 1
    return PVg_due