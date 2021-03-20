import annuitydue

def test_SAD():
    assert annuitydue.SAD(200,0.02,5) == 1061.6241926400003

def test_SAD1():
    assert annuitydue.SAD1(200,0.02,5) == 961.5457397348586