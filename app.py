from flask import Flask, render_template, jsonify
from utils.monitoramento import obter_dispositivos_conectados, obter_status_dispositivos, dispositivos_inativos
import threading
import time

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dispositivos')
def dispositivos():
    return render_template('dispositivos.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/api/dispositivos')
def api_dispositivos():
    dispositivos = obter_dispositivos_conectados()
    return jsonify({'dispositivos': dispositivos})

@app.route('/api/status')
def api_status():
    dispositivos = obter_dispositivos_conectados()
    status = obter_status_dispositivos(dispositivos)
    dispositivos_inativos_lista = list(dispositivos_inativos.values())
    return jsonify({'status': status, 'dispositivos_inativos': dispositivos_inativos_lista})

def atualizacao_continua():
    while True:
        obter_dispositivos_conectados()
        time.sleep(10)

if __name__ == '__main__':
    threading.Thread(target=atualizacao_continua, daemon=True).start()
    app.run(debug=True, host='0.0.0.0')
