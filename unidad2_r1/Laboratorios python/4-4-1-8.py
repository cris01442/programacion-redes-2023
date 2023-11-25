"""
    Elaborado por:  Cristopher López Jiménez
    Descripción:    Laboratorios R1
"""
import os

def find(path, dir):
    if not os.path.exists(path):
        print("El directorio dado no existe.")
        return
    for root, dirs, files in os.walk(path):
        if dir in dirs:
            print(os.path.join(root, dir))

path = "./tree"
dir = "python"
find(path, dir)


