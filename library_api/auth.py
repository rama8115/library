from flask_restx import Namespace, Resource, fields

auth_routes = Namespace("auth", description="Authentication operations")

# Mock token storage
tokens = {"test_user": "secure_token_123"}

# Model for login
login_model = auth_routes.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)

@auth_routes.route("/login")
class Login(Resource):
    @auth_routes.expect(login_model)
    @auth_routes.doc("login_user")
    def post(self):
        """Login and get a token"""
        data = auth_routes.payload
        if data["username"] in tokens:
            return {"token": tokens[data["username"]]}, 200
        return {"error": "Invalid credentials"}, 401
