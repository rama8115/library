from flask import Flask
from flask_restx import Api
from routes import book_routes, member_routes
from auth import auth_routes

app = Flask(__name__)

# Initialize Flask-RESTx API
api = Api(
    app,
    title="Library Management System API",
    description="A simple API for managing books and members.",
)

# Add namespaces to the API
api.add_namespace(book_routes, path="/books")
api.add_namespace(member_routes, path="/members")
api.add_namespace(auth_routes, path="/auth")

if __name__ == "__main__":
    app.run(debug=True)
