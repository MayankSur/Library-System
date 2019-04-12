#Flask Server Application using variety of HTTP request methods - PUT, PATCH, POST and DELETE
from flask import Flask, jsonify, request, Response
import json
from bookmodel import *
from settings import *

#Any app.routes not defined are automatically defined as a GET request
#This can be defined as the main page
@app.route('/')
def hello_world():
    return 'Welcome to the Local Library!'

#Defined as the books resource page / catalog
@app.route('/books')
def get_books():
    return jsonify({'Books' : Book.get_all_books()})

#Specific book Search
@app.route('/books/<int:isbn>')
def get_by_isbn(isbn):
    return jsonify(Book.get_book(isbn))

#METHOD TO ADD BOOKS TO THE STORE
@app.route('/books', methods =['POST'])
def add_book():
    #Converts input into JSON.
    bookObject = request.get_json()
    #Test if the book is valid
    test = validBookObject(bookObject)

    if (test):

        Book.add_book(bookObject['name'], bookObject['price'], bookObject['isbn'])
        #Response constructor to respond to the user with a more useful response
        response = Response("",201,mimetype='application/json')
        #Creates a response header to allow the client to understand the location which is being updated
        response.headers["Location"] = "/books/" + str(bookObject['isbn'])
        return response
    else:
        #Create a useful error for the client to be able to see what he did wrong
        error_msg={
        "error":" Invalid book object was passed in request",
        "helpString":" Data must be passed in a particular manner: {name, price, isbn}"
        }
        #Response constructor
        response = Response(json.dumps(error_msg),400,mimetype='application/json')
        #Creates a response header to allow the client to understand the location which is being updated
        return response

#Need to check if the object send it actually a valid book
def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

# Need to check if the object send it actually a valid book - specific for patch requests
def validBookObjectSpecific(bookObject):
    if ("name" in bookObject and "price" in bookObject):
        return True
    else:
        return False

#METHOD TO EDIT BOOKS IN THE STORE

#A put request in essence forces you to change the whole entity and it's vital to comply by these policies
#Alternatively you can use a patch request to alter one specific part of information
@app.route("/books/<int:isbn>", methods=['PUT'])
def reqlaceBook(isbn):
    #Gets the request body the client creates
    request_change = request.get_json()

    test = validBookObjectSpecific(request_change)

    if (test):

        Book.replace_book(isbn, request_change['name'], request_change['price'])
        #Add a corresponding error message
        response = Response("The books were updated", 204)
        return response
    else:
        #Create a useful error for the client to be able to see what he did wrong
        error_msg={
        "error":" Invalid object details were passed in request",
        "helpString":" Data must be passed in a particular manner: {name, price}"
        }
        response = Response(json.dumps(error_msg),400,mimetype='application/json')
        return response

#Patch version
@app.route("/books/<int:isbn>", methods=['PATCH'])
def updateBook_patch(isbn):
    #Gets the request body the client creates
    request_change = request.get_json()

    updatedEntry = {}

    if ('name' in request_change):
        Book.update_book_name(isbn, request_change['name'])
    if ('price' in request_change):
        Book.update_book_price(isbn, request_change['price'])

    #Add a corresponding error message
    response = Response("The books were updated", 204)
    response.headers["Location"] = "/books/" + str(isbn)
    return response

#Deleting Entries
@app.route("/books/<int:isbn>", methods=['DELETE'])
def removeBook(isbn):
    #First we want to identify books that agree
    if (Book.delete_book(isbn)):
        response = Response("",204,mimetype='application/json')
        return response
    else:
        response = Response("",404,mimetype='application/json')
        return response

app.run(port = 5000)
