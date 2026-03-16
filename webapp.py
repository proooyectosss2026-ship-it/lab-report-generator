from flask import Flask, request, send_file, make_response
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<html>
<head>

<title>Instant Lab Report Generator</title>

<style>

body {
    font-family: Arial;
    background-color: #f2f2f2;
}

.container {
    width: 400px;
    margin: 100px auto;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px gray;
}

h1 {
    text-align: center;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 15px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
}

button:hover {
    background-color: #0056b3;
}

.features{
    margin-top:30px;
    font-size:14px;
}

.footer{
    margin-top:30px;
    text-align:center;
    color:gray;
    font-size:12px;
}

</style>

</head>

<body>

<div class="container">

<h1>Instant Lab Report Generator</h1>

<div class="subtitle">
Generate a complete laboratory report in seconds
</div>

<form method="post" action="/generate" enctype="multipart/form-data">

Experimento:<br>
<input name="experiment"><br>

Estudiante:<br>
<input name="student"><br>

Fecha:<br>
<input name="date"><br>

Medición 1:<br>
<input name="m1"><br>

Medición 2:<br>
<input name="m2"><br>

Medición 3:<br>
<input name="m3"><br>

Subir datos (CSV):<br>
<input type="file" name="file"><br>

<button type="submit">Generar informe</button>

</form>

<div class="features">

<b>Features</b><br><br>

• Automatic PDF report<br>
• CSV data support<br>
• Scientific format<br>
• Ready for lab submission

</div>

<div class="footer">
Generated automatically with Lab Report Generator
</div>

</div>

</body>
</html>
"""


@app.route("/generate", methods=["POST"])
def generate():

    # comprobar si ya usó el informe gratuito
    if request.cookies.get("free_used") == "yes":
        return """
        <html>

        <body style="font-family:Arial;text-align:center;margin-top:100px">

        <h1>Free report already used</h1>

        <p>You have already generated your free report.</p>

        <p>Upgrade to premium to generate unlimited reports.</p>

        <p>Premium users can generate unlimited laboratory reports.</p>

        <button style="padding:15px;font-size:16px;background:#28a745;color:white;border:none;border-radius:5px">
        Upgrade to Premium – 5€
        </button>

        </body>

        </html>
        """

    experiment = request.form["experiment"]
    student = request.form["student"]
    date = request.form["date"]

    file = request.files["file"]

    # decidir si usar CSV o mediciones manuales
    if file and file.filename != "":
        data = pd.read_csv(file)
        values = data.iloc[:,0].tolist()

    else:
        m1 = float(request.form["m1"])
        m2 = float(request.form["m2"])
        m3 = float(request.form["m3"])
        values = [m1, m2, m3]

    # crear gráfica
    plt.figure(figsize=(6,4))
    plt.plot(values)
    plt.title("Resultados experimentales")
    plt.xlabel("Medición")
    plt.ylabel("Valor")

    plt.savefig("graph.png")
    plt.close()

    # nombre del archivo
    safe_experiment = experiment.replace(" ","_")
    file_name = f"lab_report_{safe_experiment}.pdf"

    # crear PDF
    c = canvas.Canvas(file_name)

    c.drawString(100,750,"LAB REPORT")
    c.drawString(100,720,f"Experimento: {experiment}")
    c.drawString(100,700,f"Estudiante: {student}")
    c.drawString(100,680,f"Fecha: {date}")

    c.drawString(100,640,"Introducción")
    c.drawString(100,620,"Este informe describe el experimento realizado.")

    c.drawString(100,580,"Conclusión")
    c.drawString(100,560,"El experimento permitió comprender mejor el fenómeno.")

    # insertar gráfica
    c.drawImage("graph.png",100,350,width=400,height=200)

    c.save()

    # enviar PDF y marcar cookie
    response = make_response(send_file(file_name, as_attachment=True))
    response.set_cookie("free_used","yes")

    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)