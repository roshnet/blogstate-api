from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flaskext.mysql import MySQL
from werkzeug.security import check_password_hash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(11)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aaaaa'
app.config['MYSQL_DATABASE_DB'] = 'blogstate'

mysql = MySQL()
mysql.init_app(app)

cur = mysql.connect().cursor()


@app.route('/')
@app.route('/api')
def index():
    return 'HTTP default response'


@app.route('/api/login', methods=['POST'])
def login():
    """
    :param: u: Username
    :param: p: Password

    BRIEF:
        Returns a response with header 'auth-status' = 0`
        when login details are invalid.

        Returns a response with header 'auth-status' = 1`
        when login details are valid.

    DETAILED:
        Checks first if username exists.
        If username does not exist in the database:
            Returns a response with header 'auth-status' = 0`

        If username exists, extracts the hash, and compares against
        the current hash.

        If hashes match,
            Returns a response with header 'auth-status' = 1`
        If hashes do not match,
            Returns a response with header 'auth-status' = 0`

    """
    request_data = request.get_json()
    '''
    For `request_data` to be a dictionary, the `request.post(...)` in
    calling the API should have `json=info` as an argument,
    and not `data=info`, where `info` is a dictionary.

    However, the `json` argument only works in recent versions of `requests`.
    '''
    username, passwd = request_data['u'], request_data['p']

    # String sanitation to be applied...
    q = "SELECT user_id,hash FROM `credentials` WHERE username='{}'"

    print('==================================', username)
    cur.execute(q.format(username))
    match = cur.fetchone()

    if match is None:
        # Username not found.
        response = make_response()
        response.headers['auth-status'] = 0
        return response

    if check_password_hash(match[1], passwd):
        # Case of correct credentials
        response = make_response()
        response.headers['auth-status'] = 1
        return response

    # Incorrect password
    response = make_response()
    response.headers['auth-status'] = 0
    return response


@app.route('/api/signin')



if __name__ == '__main__':
    app.run(debug=True)
