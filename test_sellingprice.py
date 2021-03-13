import selling_price

def test_selling_price():
    if selling_price.selling_price(0,1,1) == 0:
        print("error")
    assert selling_price.selling_price(100,100,1) == 0.0
    assert selling_price.selling_price(100,10,1) == 9

    
 

