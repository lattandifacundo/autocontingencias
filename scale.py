'''
    0 = formaciones de lluvia
    1 = lluvias debiles en precipitación
    2 = lluvias moderadas en precipitación
    3 = formaciones de granizo y lluvias moderadas
    4 = precipicación de granizo y lluvias graves
'''

base = {
    (211, 211, 211): 4,  #j = 87
    (190, 190, 190): 4,  #j = 111
    (253,  52,  28): 4,  #j = 133
    (254,  95,   5): 4,  #j = 161
    (254, 154,  88): 3,  #j = 187
    (253, 249,  15): 3,  #j = 210
    (250, 196,  49): 3,  #j = 234
    (210, 136,  59): 3,  #j = 260
    (192, 100, 135): 3,  #j = 285
    (200,  15, 134): 2,  #j = 310
    (110,  13, 198): 2,  #j = 335
    ( 28,  71, 232): 1,  #j = 361
    (  8, 127, 219): 1,  #j = 385
    (  0, 112,   0): 0,  #j = 415
    (  0,  90,   0): 0,  #j = 435
    ( 72,  61, 139): 0,  #j = 460
}

def compute(key):
    value = base.get(key)
    if(value != None):
        return value
    else:
        return -1