def kthBitTest(num, k):
    return num//(2**k) & 1

def test():
    assert kthBitTest(6,2) == 1, 'Oops'
    assert kthBitTest(3,1) == 1, 'Oops'
    print("Nice")

test()