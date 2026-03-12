print("===== LAB REPORT GENERATOR =====")

experiment = input("Nombre del experimento: ")
student = input("Nombre del estudiante: ")
date = input("Fecha: ")

print("\nTipo de experimento:")
print("1 - Mecánica")
print("2 - Termodinámica")
print("3 - Electricidad")

choice = input("Elige una opción (1/2/3): ")

if choice == "1":
    intro = "Este experimento analiza el comportamiento de un sistema mecánico."
elif choice == "2":
    intro = "Este experimento analiza un proceso termodinámico y la transferencia de energía."
elif choice == "3":
    intro = "Este experimento analiza el comportamiento de un circuito eléctrico."
else:
    intro = "Este experimento analiza el fenómeno estudiado en el laboratorio."

print("\nIntroduce tres mediciones del experimento")

m1 = float(input("Medición 1: "))
m2 = float(input("Medición 2: "))
m3 = float(input("Medición 3: "))

average = (m1 + m2 + m3) / 3

report = f"""
LAB REPORT

Experimento: {experiment}
Estudiante: {student}
Fecha: {date}

INTRODUCCIÓN
{intro}

METODOLOGÍA
Se realizaron tres mediciones experimentales para analizar el comportamiento del sistema.

RESULTADOS
Las mediciones obtenidas fueron: {m1}, {m2}, {m3}
El valor promedio calculado es: {average}

CONCLUSIÓN
Los resultados experimentales permiten analizar el fenómeno estudiado y comparar con el modelo teórico.
"""

print(report)

file = open("lab_report.txt", "w")
file.write(report)
file.close()

print("Informe guardado en lab_report.txt")