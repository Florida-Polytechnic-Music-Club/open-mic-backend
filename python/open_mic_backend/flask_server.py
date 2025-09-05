from flask import Flask, request, jsonify
from .auth_handler import AuthHandler

class FlaskServer:
    """
    Routes
    /sumbit
    {
      'email': 'email_val',
      'performance_name': 'performance_name_val',
      'performance_description': 'performance_description',
      'performance_details': 'performance_details'
    }

    /login
    JSON:
    {'email': 'email_val'}

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
            success, rsp_data, rc = self.auth_handler.loginAtempt(data)
            return_json = {}
            if success:
                return_json["status"] = "success"
                return_json["data"] = rsp_data
                return jsonify(return_json), rc
            else:
                return_json["status"] = "error"
                return_json["error"] = rsp_data
                return jsonify(return_json), rc
                


    def run(self, host="0.0.0.0", port=8080, debug=False):
        self.app.run(host=host, port=port, debug=debug)

