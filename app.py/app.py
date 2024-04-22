from flask import Flask, render_template, redirect, url_for, request, send_from_directory

import os
###libreria web para python para poder redireccionar al index en el navegador#######
app = Flask(__name__)

registros = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarea = request.form['tarea']
        estado = request.form['estado']
        nuevo_registro = {'tarea': tarea, 'estado': estado}
        registros.append(nuevo_registro)
        return redirect(url_for('index'))
        
    else:
        return render_template('index.html', registros=registros)

@app.route('/actualizar_estado/<tarea>', methods=['POST'])
def actualizar_estado(tarea):
    nuevo_estado = request.form['estado']
    for registro in registros:
        if registro['tarea'] == tarea:
            registro['estado'] = nuevo_estado
            break
    return redirect(url_for('index'))

@app.route('/eliminar_tarea/<tarea>', methods=['POST'])
def eliminar_tarea(tarea):
    for registro in registros:
        if registro['tarea'] == tarea:
            registros.remove(registro)
            break
    return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
    app.run(host="0.0.0.0", port=port)