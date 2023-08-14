import cv2
from flask import request,jsonify,Response,render_template,session
from src.Controllers.loginController import loginController,loginControllerFacial
from src.Controllers.recognitionController import getGenerateFrame,getResponseFrame
from src.Models.model import get_user_recognition,get_login_facial

session_data = {}
video_started = True
def loginRoute (app):
    @app.route('/welcome', methods = [ 'POST', 'GET'])
    def welcome():
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            if codigo is not None and len(codigo) > 0:
                password = request.form.get('password')
                response = loginController(codigo,password)
                if len(response)>0:
                    return render_template('index.html', welcome=True,name=response[0][3])
                else:
                    return render_template('index.html', welcome=False, error="Contraseña incorrecta")
            else:
                global session_data
                codigo = session_data.get('detected_codigo', None)
                response = loginControllerFacial(codigo)
                if len(response)>0:
                    return render_template('index.html', welcome=True,name=response[0][3])
                else:
                    return render_template('index.html', welcome=False, error="Contraseña incorrecta")
        else:
            return render_template('index.html', welcome=False, error="Ingreso fraudulento")
    
    @app.route('/video_feed')
    def video_feed():
        global session_data
        global video_started
        return getResponseFrame(session_data,video_started)
    
    @app.route('/detener_camara', methods=['GET'])
    def detener_camara():
        global video_started  # Acceder a la variable global
        video_started = False
        return 'Cámara detenida exitosamente'

    @app.route('/iniciar_camara', methods=['GET'])
    def iniciar_camara():
        global video_started  # Acceder a la variable global
        video_started = True
        return 'Cámara iniciada exitosamente'

    @app.route('/logout', methods=['POST'])
    def logout():
        global video_started  # Acceder a la variable global
        global session_data
        video_started = False
        session_data = {}
        return render_template('index.html', welcome=False)
    
    