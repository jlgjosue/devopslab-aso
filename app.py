from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)  

@app.route("/")
def pagina_inicial():
    return "Não pense que é capaz. Saiba que é. - Matrix"
   

if __name__ == '__main__':
    app.run()