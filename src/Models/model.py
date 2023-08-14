from Connection.connection import get

def get_login(codigo,password):
    query = f"SELECT idUser,codigo,password,name FROM user where codigo ='{codigo}' and password='{password}'"
    response = get(query)
    return response

def get_login_facial(codigo):
    query = f"SELECT idUser,codigo,password,name FROM user where codigo ='{codigo}'"
    response = get(query)
    return response

def get_user_recognition():
    query = f"SELECT idUser,codigo,password,name FROM user where recognition = 1 ORDER BY codigo ASC"
    response = get(query)
    return response