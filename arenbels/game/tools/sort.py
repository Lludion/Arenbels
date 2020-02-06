

def unhappyfirst(L):
    K = L.copy()
    K.sort(key = lambda x: x.happy)
    return K

def happyfirst(L):
    K = L.copy()
    K.sort(key = lambda x: x.happy, reverse = True)
    return K