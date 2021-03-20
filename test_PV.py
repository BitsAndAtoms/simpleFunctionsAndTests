import PV

def test_OSA():
    assert PV.OSA(36000,0.03,80) == 1087227.48404974

def test_OGA():
    assert PV.OGA(200,0.02,8) == 1716.5938100226572

def test_CGA():
    assert PV.CGA(40000,0.02,0.04,8) == 629140.2712791682