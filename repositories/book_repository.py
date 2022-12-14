from db.run_sql import run_sql

import repositories.author_repository as author_repository
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING * "
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def view_all():
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    books = []
    for book in results:
        author_id = book['author_id']
        author = author_repository.select(author_id)
        created_book = Book(book['id'], book['title'], author)
        books.append(created_book)
    return books