from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html', erro=False)

@app.route('/index', methods=['post'])
def index():
    dici = {'UCL':['ADMIN','UCL123'],
            'JP':['PROF','123']}
    usuario = request.form.get('username')
    senha = request.form.get('password')
    validacao = dici.get(usuario,['ERRO','AUTH'])

    if validacao[1]==senha:
        return render_template('index.html', dados=[usuario, validacao[0]])
    else:
        return render_template('login.html', erro=True)

if __name__ == '__main__':
    app.run()
