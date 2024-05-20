from flask import Flask, render_template, request, redirect, url_for
from utils.monitoramento import obter_dispositivos_conectados, obter_status_dispositivos
from utils.alertas import verificar_alertas

app = Flask(__name__)

@app.route('/')
def index():
    dispositivos = obter_dispositivos_conectados()
    status = obter_status_dispositivos(dispositivos)
    alertas = verificar_alertas(status)
    return render_template('index.html', dispositivos=dispositivos, status=status, alertas=alertas)

@app.route('/status/<nome_dispositivo>')
def status_dispositivo(nome_dispositivo):
    dispositivos = obter_dispositivos_conectados()
    dispositivo = next((d for d in dispositivos if d['nome'] == nome_dispositivo), None)
    if dispositivo:
        status = obter_status_dispositivos([dispositivo])[0]
        return render_template('status_dispositivo.html', dispositivo=dispositivo, status=status)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
