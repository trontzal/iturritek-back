from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import request, jsonify
from dbConfig import get_db
import bcrypt
from flask_jwt_extended import JWTManager

# Configura la extensión Flask-JWT-Extended
jwt = JWTManager()

# Cuando se llama busca el usuario
def find_user_by_username(username):
    # Conecta a la base de datos
    db = get_db()
    cursor = db.cursor()

    # Busca al usuario por su nombre de usuario en la base de datos
    cursor.execute('SELECT username, password_hash FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()

    if user_data:
        # Si se encuentra al usuario, devuelve un diccionario con el nombre de usuario y el hash de la contraseña
        return {'username': user_data[0], 'password_hash': user_data[1]}
    else:
        # Si no se encuentra al usuario, devuelve None
        return None

# Función para verificar la contraseña de un usuario
def verify_password(user, password):
    # Verifica si la contraseña proporcionada coincide con el hash de contraseña almacenado en la base de datos
    return bcrypt.checkpw(password.encode('utf-8'), user['password_hash'])

def initialize_auth(app):
    app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'
    jwt.init_app(app)

@jwt_required
def protected_route():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)
