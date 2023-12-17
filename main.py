from flask import Flask, request, jsonify, session


app=Flask(__name__)

books_list = [
    {
        "id": 0,
        "author": "J Rowling",
        "language": "English",
        "title": "Harry Potter",
        "genre": "Fantasy",
    },
    {
        "id": 1,
        "author": "Cao Xueqin",
        "language": "Chinese",
        "title": "Dream of the Red Chamber",
        "genre": "Family Saga"
    },
    {
        "id": 2,
        "author": "Agatha Christie",
        "language": "English",
        "title": "And Then There Were none",
        "genre": "Mystery",
    },
    {
        "id": 3,
        "author": "Paulo Coelho",
        "language": "English",
        "title": "The Alchemist",
        "genre": "Fantasy",
    },
    {
        "id": 4,
        "author": "Umberto Eco",
        "language": "Italian",
        "title": "The Name of the Rose",
        "genre": "Mystery",
    },
    {
        "id": 5,
        "author": "Beatrix Potter",
        "language": "English",
        "title": "The Tale of Peter Rabbit",
        "genre": "Children Literature",
    },
    {
        "id": 6,
        "author": "Richard Adams",
        "language": "English",
        "title": "Watership Down",
        "genre": "Fantasy",
    },
]

@app.route('/books',methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Nothing Found',404
            
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        new_genre = request.form['genre']
        iD = books_list[-1]['id']+1
        
        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title,
            'genre': new_genre
        }
        books_list.append(new_obj)
        return jsonify(books_list),201

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']
                book['genre'] = request.form['genre']
                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title'],
                    'genre': book['genre']
                }
                return jsonify(updated_book)
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)       
                
        
    
if __name__ == '__main__':
    app.run(debug=True)