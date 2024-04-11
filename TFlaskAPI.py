from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta

def tflask_api(jwt_secret_key='super-secret', token_expiry_hours=1):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = jwt_secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=token_expiry_hours)
    jwt = JWTManager(app)

    users = {}  # Sample user data (replace with your own user authentication mechanism)

    @app.route('/api/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400

        if username in users:
            return jsonify({"message": "Username already exists"}), 400

        users[username] = password
        return jsonify({"message": "User registered successfully"}), 201

    @app.route('/api/auth', methods=['POST'])
    def authenticate():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username in users and users[username] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401

    @app.route('/api/profile', methods=['GET'])
    @jwt_required()
    def profile():
        current_user = get_jwt_identity()
        return jsonify({'username': current_user}), 200

    return app

if __name__ == '__main__':
    # Example usage
    app = tflask_api()
    app.run(debug=True)
