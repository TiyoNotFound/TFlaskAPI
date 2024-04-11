<div align="center">
  <h1>TFlaskAPI</h1>
  <p>A simple Flask-based API with JWT authentication for user management</p>
</div>

---

## Features

| Feature              | Description                                          |
|----------------------|------------------------------------------------------|
| **User Registration**| Register new users with a username and password     |
| **User Authentication** | Authenticate users using their credentials        |
| **JWT Authentication**  | Protect endpoints using JSON Web Tokens           |
| **User Profile**    | Retrieve user profile information                   |

## Usage

### Server Side Script

```python
from TFlaskAPI import tflask_api

# Create the Flask app with default settings
app = tflask_api()

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)

```
### Client Side Script

You can use the API endpoints in your client-side scripts to interact with the server.

```python
import requests

# Base URL for the Flask API
base_url = 'http://localhost:5000/api'

# Function to register a new user
def register(username, password):
    url = f'{base_url}/register'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

# Function to authenticate a user
def authenticate(username, password):
    url = f'{base_url}/auth'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json()

# Function to access the user's profile
def profile(access_token):
    url = f'{base_url}/profile'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Example usage
if __name__ == '__main__':
    # Register a new user
    register_response = register('new_user', 'new_password')
    print('Register:', register_response)

    # Authenticate the user
    auth_response = authenticate('new_user', 'new_password')
    access_token = auth_response.get('access_token')
    print('Authenticate:', auth_response)

    # Access the user's profile
    if access_token:
        profile_response = profile(access_token)
        print('Profile:', profile_response)
    else:
        print('Authentication failed.')
```

## API Endpoints

| Endpoint             | Method | Description                                          |
|----------------------|--------|------------------------------------------------------|
| `/api/register`      | POST   | Register new users with username and password        |
| `/api/auth`          | POST   | Authenticate users using credentials                |
| `/api/profile`       | GET    | Retrieve user profile information (requires JWT)     |

## Configuration

You can customize the JWT secret key and token expiry time by passing arguments to the `tflask_api` function.

```python
from TFlaskAPI import tflask_api

app = tflask_api(jwt_secret_key='custom-secret-key', token_expiry_hours=2)
```

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
