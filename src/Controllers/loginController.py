from src.Models.model import get_login,get_login_facial
def loginController(codigo,password):
    response = get_login(codigo,password)
    return response

def loginControllerFacial(codigo):
    response = get_login_facial(codigo)
    return response