from flask import Flask, request, jsonify
from .auth_handler import AuthHandler

class FlaskServer:
    """
    Routes
    /login
    JSON:
    {'token': 'token_val'}
    {
     'username': 'username_val',
     'password': 'password_val',
     'remember_me', 'remember_me_bool'
     }

     /logout
     {'token': 'token_val'}
    
    """
    def __init__(self):
        self.app = Flask(__name__)
        self.auth_handler = AuthHandler()

        self._setup_routes()

    def _setup_routes(self):
        @self.app.post("/submit")
        def submit():
            data = request.get_json(silent=True) or request.form.to_dict()
            return jsonify(status="received", data=data)
        
        @self.app.post("/login")
        def login():
            data = request.get_json(silent=True) or request.form.to_dict()
            success = self.auth_handler.loginAtempt(data)
            return jsonify(status="received", data=data)

    def run(self, host="0.0.0.0", port=8080, debug=False):
        self.app.run(host=host, port=port, debug=debug)

