import cv2
from flask import request,jsonify,Response,render_template,session
#from src.Controllers.recognitionController import getGenerateFrame,getResponseFrame
from src.Models.model import get_user_recognition,get_login_facial

def recognitionRoute (app):    
    @app.route('/start_video')
    def start_video():
        return render_template('index.html',video=True,welcome=False)
    
    @app.route('/stop_video')
    def stop_video():
        return render_template('index.html',video=False,welcome=False)