from flask import Flask, request, make_response

app = Flask(__name__)


# Set cookie endpoint (POST request)
@app.route('/setcookies', methods=['POST'])
def set_cookie():
    # Get the 'name' from the incoming JSON body
    user_name = request.json.get('name', 'Natsu Dragneel')

    # Create a response
    resp = make_response(f'Cookie has been set with your name: {user_name}')

    # Set the cookie (cookie will expire in 30 days)
    resp.set_cookie('username', user_name, max_age=30 * 24 * 60 * 60)  # max_age in seconds

    return resp


# Get cookie endpoint (GET request)
@app.route('/getcookies', methods=['GET'])
def get_cookie():
    # Retrieve the 'username' cookie
    username = request.cookies.get('username')

    if username:
        return f'Hello, {username}!'
    else:
        return 'No cookie found!'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
