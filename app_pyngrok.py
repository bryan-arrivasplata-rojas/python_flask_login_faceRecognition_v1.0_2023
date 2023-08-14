import ssl
from flask import Flask, render_template,redirect,url_for
from src.Routes.recognition import recognitionRoute
from src.Routes.login import loginRoute
from pyngrok import ngrok
ssl._create_default_https_context = ssl._create_unverified_context
ngrok.set_auth_token('2Txzsdw5kwdYAQN0Un9RU7lYQ5g_6UYKSB2PLcGDe6WDgamP3')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f5a8e2e9c7e093b96d6ef32c55d251c3'
@app.route('/')
def index():
    return render_template('index.html', video=False,welcome=False)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

recognitionRoute(app)
loginRoute(app)

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    # Obtener la URL pública generada por Ngrok
    public_url_str = str(public_url)
    print('URL pública de Ngrok:', public_url_str)
    app.run()

'''if __name__ == '__main__':
    app.run(debug=True)'''
