
asignaturas = [
"Probabilidad y Estadística",
"Electrónica para IDC Física",
"Conexión de redes WAN",
"Administración de servidores I",
"Programación de Redes",
"Inglés IV"
]

notas_unidad_i = {}

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de la unidad I para {asignatura}: "))
    notas_unidad_i[asignatura] = nota

for asignatura, nota in notas_unidad_i.items():
    print(f"En {asignatura} ha sacado {nota}")

