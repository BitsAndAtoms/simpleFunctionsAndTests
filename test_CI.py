import CI

def test_CI():
    assert CI.CI(200,0.02,8) == 234.33187620045314

def test_CI1():
    assert CI.CI1(200,0.02,8) == 170.6980742380223