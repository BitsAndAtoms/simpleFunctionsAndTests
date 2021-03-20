import FV

def test_OSA():
    assert FV.OSA(36000,0.03,80) == 11569068.667716263

def test_OGA():
    assert FV.OGA(100,0.008165,12) == 1255.3829790582881

def test_CGA():
    assert FV.CGA(2000,0.03,0.05,5) == 129946.70439860002