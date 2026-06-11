from flask import Flask, jsonify, request

app = Flask(__name__)

# Store 5 books using a list of dictionaries
books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "price": 500
    },
    {
        "id": 2,
        "title": "Flask Development",
        "author": "James Brown",
        "price": 650
    },
    {
        "id": 3,
        "title": "Data Structures",
        "author": "Emma Wilson",
        "price": 700
    },
    {
        "id": 4,
        "title": "Machine Learning",
        "author": "David Lee",
        "price": 900
    },
    {
        "id": 5,
        "title": "Web Development",
        "author": "Sophia Taylor",
        "price": 750
    }
]

# Home Route
@app.route('/')
def home():
    return "Book Management API Running"


# Get All Books API
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Add Book API
@app.route('/add-book', methods=['POST'])
def add_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "price": data["price"]
    }
    books.append(new_book)
    return jsonify({
        "message": "Book Added Successfully"
    })


# Search Book API
@app.route('/search-book/<title>', methods=['GET'])
def search_book(title):

    for book in books:
        if book["title"].lower() == title.lower():
            return jsonify(book)
    return jsonify({
        "message": "Book not found"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)