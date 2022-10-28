from flask import Flask, render_template, request, redirect, url_for
from model.models import ConectandoBD

app = Flask(__name__, static_folder=f"../views/static", template_folder=f"../views/templates")


@app.route('/', methods=["POST", "GET"])
def verificargeral():
    pagina = 'index.html'
    return render_template(pagina)


@app.route('/email', methods=["POST", "GET"])
def email():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            bd = ConectandoBD()
            bd.criarTabelas()
            bd.adicionarEmail(email)
            return redirect(url_for('verificargeral'))
        except:
            return redirect(url_for('verificargeral'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
