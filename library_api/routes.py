from flask_restx import Namespace, Resource, fields
from models import books, members, book_id_counter, member_id_counter

# Namespace for Books
book_routes = Namespace("books", description="Operations related to books")

# Model for Books
book_model = book_routes.model(
    "Book",
    {
        "title": fields.String(required=True, description="The book title"),
        "author": fields.String(required=True, description="The book author"),
        "year": fields.Integer(required=True, description="The publication year"),
        "genre": fields.String(required=True, description="The book genre"),
    },
)

@book_routes.route("/")
class BookList(Resource):
    @book_routes.doc("list_books")
    def get(self):
        """List all books"""
        return list(books.values()), 200

    @book_routes.expect(book_model)
    @book_routes.doc("add_book")
    def post(self):
        """Add a new book"""
        global book_id_counter
        data = book_routes.payload
        books[book_id_counter] = {
            "title": data["title"],
            "author": data["author"],
            "year": data["year"],
            "genre": data["genre"],
        }
        response = {"message": "Book added", "id": book_id_counter}
        book_id_counter += 1
        return response, 201

@book_routes.route("/<int:book_id>")
class Book(Resource):
    @book_routes.doc("get_book")
    def get(self, book_id):
        """Get a book by its ID"""
        if book_id not in books:
            return {"error": "Book not found"}, 404
        return books[book_id], 200

    @book_routes.expect(book_model)
    @book_routes.doc("update_book")
    def put(self, book_id):
        """Update a book by its ID"""
        if book_id not in books:
            return {"error": "Book not found"}, 404
        data = book_routes.payload
        books[book_id].update(data)
        return {"message": "Book updated"}, 200

    @book_routes.doc("delete_book")
    def delete(self, book_id):
        """Delete a book by its ID"""
        if book_id not in books:
            return {"error": "Book not found"}, 404
        del books[book_id]
        return {"message": "Book deleted"}, 200

# Namespace for Members
member_routes = Namespace("members", description="Operations related to members")

# Model for Members
member_model = member_routes.model(
    "Member",
    {
        "name": fields.String(required=True, description="The member's name"),
        "email": fields.String(required=True, description="The member's email"),
        "membership_date": fields.String(required=True, description="The membership date"),
    },
)

@member_routes.route("/")
class MemberList(Resource):
    @member_routes.doc("list_members")
    def get(self):
        """List all members"""
        return list(members.values()), 200

    @member_routes.expect(member_model)
    @member_routes.doc("add_member")
    def post(self):
        """Add a new member"""
        global member_id_counter
        data = member_routes.payload
        members[member_id_counter] = {
            "name": data["name"],
            "email": data["email"],
            "membership_date": data["membership_date"],
        }
        response = {"message": "Member added", "id": member_id_counter}
        member_id_counter += 1
        return response, 201
