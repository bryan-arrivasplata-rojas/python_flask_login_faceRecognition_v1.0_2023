import cv2
from flask import Response
from src.Models.model import get_user_recognition,get_login_facial

def getGenerateFrame(session_data,video_started):
    cap = cv2.VideoCapture(0)
    #dataPath = 'static/Fotos'
    result = get_user_recognition()
    imagePaths = [item[1] for item in result]
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('static/Recognition/modeloLBPHFace.xml')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while video_started:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()
            faces = faceClassif.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                rostro = auxFrame[y:y + h, x:x + w]
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                result = recognizer.predict(rostro)
                response_data = {}
                if result[1] < 85:
                    cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
                    cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    #print(imagePaths[result[0]])
                    video_started=False
                    session_data['detected_codigo'] = imagePaths[result[0]]
                else:
                    if result[1] <100:
                        cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)
                        cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    else:
                        None
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            if(video_started) == False:
                break
    cap.release()
def getResponseFrame(session_data,video_started):
    return Response(getGenerateFrame(session_data,video_started), mimetype='multipart/x-mixed-replace; boundary=frame')