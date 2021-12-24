def andGate(a, b):
    assert a == 0 or b == 0 or a == 1 or b == 1, "Invalid input"
    return a * b

def orGate(a, b):
    assert a == 0 or b == 0 or a == 1 or b == 1, "Invalid input"
    return max(a,b)

def notGate(a):
    assert a == 0 or a == 1, "Invalid input"
    return 1 - a

def xorGate(a, b):
    assert a == 0 or b == 0 or a == 1 or b == 1, "Invalid input"
    return a + b - 2 * a * b

def nandGate(a, b):
    assert a == 0 or b == 0 or a == 1 or b == 1, "Invalid input"
    return not (a * b)

