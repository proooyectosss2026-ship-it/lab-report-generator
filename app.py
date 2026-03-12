import tkinter as tk

def generar_informe():
    experimento = entry_experimento.get()
    estudiante = entry_estudiante.get()
    fecha = entry_fecha.get()

    report = f"""
LAB REPORT

Experimento: {experimento}
Estudiante: {estudiante}
Fecha: {fecha}

INTRODUCCIÓN
Este informe describe el experimento realizado para analizar el comportamiento del sistema estudiado.

METODOLOGÍA
El experimento se realizó siguiendo el procedimiento establecido en el laboratorio.

RESULTADOS
Los resultados obtenidos permiten analizar el comportamiento del sistema.

CONCLUSIÓN
El experimento permitió comprender mejor el fenómeno estudiado.
"""

    with open("lab_report.txt", "w") as file:
        file.write(report)

    resultado_label.config(text="Informe generado y guardado.")

ventana = tk.Tk()
ventana.title("Lab Report Generator")

tk.Label(ventana, text="Experimento").pack()
entry_experimento = tk.Entry(ventana)
entry_experimento.pack()

tk.Label(ventana, text="Estudiante").pack()
entry_estudiante = tk.Entry(ventana)
entry_estudiante.pack()

tk.Label(ventana, text="Fecha").pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()

tk.Button(ventana, text="Generar informe", command=generar_informe).pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()