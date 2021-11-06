from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Não pense que é capaz. Saiba que é. - Matrix"

if __name__ == '__main__':
    app.run()