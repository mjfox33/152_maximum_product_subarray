import code_152_maximum_product_subarray as c

def test_example_1():
    s = c.Solution()
    assert s.maxProduct([2,3,-2,4]) == 6

def test_example_2():
    s = c.Solution()
    assert s.maxProduct([-2,0,-1]) == 0