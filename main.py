from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': 'El Quijote', 'author': 'Cervantes '}
]

app = Flask(__name__)


@app.route('/')
def home():
    return 'Nasa kniznica'


@app.route('/knihy/', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.route('/knihy/', methods=['POST'])
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201


@app.route('/knihy/<int:id>', methods=['GET'])
def get_book(id_kniha):
    for book in books:
        if book['id_kniha'] == id_kniha:
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run()
