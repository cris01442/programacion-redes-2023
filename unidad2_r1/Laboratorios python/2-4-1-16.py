"""
    Elaborado por:  Cristopher López Jiménez
    Descripción:    Laboratorios R1
"""
dict1 = {

    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', '  #'),

}

number = input("Ingresa un numero: ")  
def seven_segment(number):
    for i in range(5):
        digits = [dict1[digit] for digit in str(number)]
        print("  ".join(segment[i] for segment in digits))
seven_segment(number)