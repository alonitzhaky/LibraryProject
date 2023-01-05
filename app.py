"""
WARNING:
DO NOT PREFORM ANY CHANGES IN THE CODE AFTER EXECUTING,
AS THIS WILL CORRUPT THE FULLY OPERATIONAL FINAL PROGRAM.
"""
# ~~~~~~~~~~~~~~ Imports ~~~~~~~~~~~~~~ #
import os
from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, date
import datetime
# ~~~~~~~~~~~~~~ Imports ~~~~~~~~~~~~~~ #

# ~~~~~~~~~ Flask Initialization ~~~~~~~~~ #
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TheLibrary.sqlite3'
app.config['SECRET_KEY'] = "The Library of Alon"
db = SQLAlchemy(app)
# ~~~~~~~~~ Flask Initialization ~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~ TheLibrary Build ~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~ Client Class ~~~~~~~~~~~~~~ #
class Customers(db.Model):
    id = db.Column('CustomerID', db.Integer, primary_key = True)
    customer_name = db.Column('CustomerName', db.String(50))
    customer_age = db.Column('CustomerAge', db.Integer)
    customer_city = db.Column('CustomerCity', db.String(25))
    loanlink = db.relationship("Loans", backref = "customers")

    def __init__(self, customer_name, customer_age, customer_city):
        self.customer_name = customer_name
        self.customer_age = customer_age
        self.customer_city = customer_city
# ~~~~~~~~~~~~~~ Client Class ~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~ Books Class ~~~~~~~~~~~~~~~ #
class Books(db.Model):
    id = db.Column('BookID', db.Integer, primary_key = True)
    book_name = db.Column('BookName', db.String(100))
    book_author = db.Column('BookAuthor', db.String(50))
    published = db.Column('PublishedDate', db.String(10))
    book_type = db.Column('BookType', db.Integer)
    loanlink = db.relationship("Loans", backref = "books")

    def __init__(self, book_name, book_author, published, book_type):
        self.book_name = book_name
        self.book_author = book_author
        self.published = published
        self.book_type = book_type
# ~~~~~~~~~~~~~~~ Books Class ~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~ Loans Class ~~~~~~~~~~~~~~~~ #
class Loans(db.Model):
    id = db.Column('LoanID', db.Integer, primary_key = True)
    customer_id = db.Column('CustomerID', db.Integer, db.ForeignKey("customers.CustomerID"))
    book_id = db.Column('BookID', db.Integer, db.ForeignKey("books.BookID"))
    loan_date = db.Column('LoanDate', db.Date)
    return_date = db.Column('ReturnDate', db.Date)
    returned = db.Column('ReturnedOn', db.Boolean)

    def __init__(self, customer_id, book_id, loan_date, return_date):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date
        self.returned = False
# ~~~~~~~~~~~~~~~~ Loans Class ~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~ Operator's Options ~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~ Customer Links ~~~~~~~~~~~~~~ #
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/Populate/', methods = ['POST'])
def population():
    """
    A button that will insert data, written in Python, labeled :ref:`init_db.py`. 
    Purposed to reflect data of Books, Customers, Active Loans and Late Loans.
    """
    data_population = os.system('py init_db.py' if os.name == 'nt' else 'python init_db.py')
    return render_template('index.html', data_populated = True)

@app.route('/Customers_Search', methods = ['POST'])
def search_customer():
    """
    This function requires to be given a full customer :ref:`name` in the search field as a parameter.
    Once given, the result will show. 
    """
    name = request.form ['customer_name']
    customers = Customers.query.filter(Customers.customer_name == name).first()
    if customers is None: 
        return redirect('/Customers/')
    return redirect(f'/Customers/{customers.id}')

@app.route('/Customers/', methods = ['GET', 'POST'])
@app.route('/Customers/<id>')
def all_customers(id = -1):
    """
    Present all existing customers using :ref:`'GET'` method - by checking 
    the customer :ref:`ID`. If this parameter doesn't exist, all customers will be returned,
    and inserts new data by using the :ref:`'POST'` method.
    """
    if request.method == 'GET':
        if int(id) == -1:
            return render_template('all_customers.html', customers = Customers.query.all())
        if int(id) > -1: 
            selected = Customers.query.get(int(id))
            return render_template('selected_customer.html', selected = selected)
    if request.method == 'POST':
        request_data = request.form
        customer_name = request_data ['Name']
        customer_age = request_data ['Age']
        customer_city = request_data ['City']

        newCustomer = Customers(customer_name, customer_age, customer_city)
        db.session.add(newCustomer)
        db.session.commit()
        return redirect("/Customers/")

@app.route('/NewCustomer/', methods = ['GET'])
def new_customer_page():
    """
    Redirects the user to a new page to insert a new customer into the database.
    """
    return render_template('new_customer.html')

@app.route('/Customers/Delete/<id>', methods = ['GET'])
def delete_customer(id):
    """
    This function deletes a customer, yet checks if the customer has an active :ref:`loan`,
    and will not remove it, unless returned.
    """
    customer = Customers.query.get(id)
    if customer: 
        loans = Loans.query.filter_by(returned = False)
        for loan in loans:
            if customer.id == loan.customer_id: # If customer has active loan
                return render_template('all_customers.html', customers = Customers.query.all(), active_loan = True) # FIXME: Add interpolation of "active loan" in all_customers.html
        db.session.delete(customer)
        db.session.commit()
        return render_template('all_customers.html', customers = Customers.query.all())
# ~~~~~~~~~~~~ Customer Links ~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~ Book Links ~~~~~~~~~~~~~~ #
@app.route('/Books/', methods = ['GET', 'POST'])
@app.route('/Books/<id>')
def show_all_books(id = -1):
    """
    Present all existing books using :ref:`'GET'` method - by checking 
    the book :ref:`ID`. If this parameter doesn't exist, all books will be returned,
    and inserts new data by using the :ref:`'POST'` method.
    """
    if request.method == 'GET':
        if int(id) == -1:
            return render_template('all_books.html', books = Books.query.all())
        if int(id) > -1:
            selected = Books.query.get(int(id))
            return render_template('selected_book.html', selected = selected)
    if request.method == 'POST': 
        request_data = request.form
        book_name = request_data ['Name']
        book_author = request_data ['Author']
        published = request_data ['Published']
        book_type = request_data ['Type']

        newBook = Books(book_name, book_author, published, book_type)
        db.session.add(newBook)
        db.session.commit()
        return redirect('/Books/')

@app.route('/NewBook/', methods = ['GET'])
def new_book_page():
    """
    Redirects the user to a new page to insert a new book into the database.
    """
    return render_template('new_book.html')

@app.route('/Books_Search', methods = ['POST'])
def search_book():
    """
    This function requires to be given a full book :ref:`name` in the search field as a parameter.
    Once given, the result will show. 
    """
    name = request.form ['book_name']
    books = Books.query.filter(Books.book_name == name).first()
    if books is None: 
        return redirect('/Books/')
    return redirect(f'/Books/{books.id}')

@app.route('/Books/Delete/<id>', methods = ['GET'])
def delete_book(id):
    """
    This function deletes a book, yet checks if the book is in a current loan,
    prior to removal.
    """
    book = Books.query.get(id)
    if book:
        loans = Loans.query.filter_by(returned = False)
        for loan in loans:
            if book.id == loan.book_id:
                return render_template('all_books.html', books = Books.query.all(), active_loan = True)
        db.session.delete(book)
        db.session.commit()
        return render_template('all_books.html', books = Books.query.all()) 
# ~~~~~~~~~~~~~~ Book Links ~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~ Loan Links ~~~~~~~~~~~~~~ # 
@app.route('/Loans/<id>')
@app.route('/Loans/', methods = ['GET', 'POST'])
def all_loans(id = 0):
    """
    Present all existing loans using :ref:`'GET'` method
    and inserts new data by using the :ref:`'POST'` method.
    """
    if request.method == 'GET':
        if int(id) > 0:
            return render_template('all_loans.html', loans = Loans.query.get(int(id)))
        if int(id) == -1:
            return render_template('all_loans.html', loans = Loans.query.filter_by(returned = True), returned = True)
        return render_template('all_loans.html', loans = Loans.query.filter_by(returned = False))
    if request.method == 'POST': 
        request_data = request.form
        customer_id = request_data ['CustomerID']
        book_id = request_data ['BookID'] 
        loan_date = (datetime.datetime.utcnow())
        
        book = Books.query.get(book_id)
        if book.book_type == 1: 
            return_date = date.today() + timedelta(days = 10)
        elif book.book_type == 2:
            return_date = date.today() + timedelta(days = 5)
        elif book.book_type == 3: 
            return_date = date.today() + timedelta(days = 2)
        new_loan = Loans(customer_id, book_id, loan_date, return_date)
        db.session.add(new_loan)
        db.session.commit()
        return render_template('all_loans.html', loans = Loans.query.filter_by(returned = False), action = "Loan successfully created!")

@app.route('/NewLoans/', methods = ['GET'])
def new_loan_page():
    """
    Redirects the user to a new page, where the existing books and customers are already inserted,
    thus preventing errors upon creation of new loans.
    """
    return render_template('new_loan.html', all_books = Books.query.all(), all_customers = Customers.query.all())

@app.route('/Loans/Return/<id>', methods = ['GET'])
def delete_loan(id): 
    """
    This function deletes a loan by returning a book to the library.
    """
    loan = Loans.query.get(id)
    loan.returned = True
    db.session.commit()
    return render_template('all_loans.html', loans = Loans.query.filter_by(returned = False), action = "Book successfully returned.")

@app.route('/Loans/Late/', methods = ['GET'])
def show_late_loans():
    """
    This function shows on the webpage all late loans, filtered by date.
    """
    late_loans = []
    active_loans = Loans.query.filter_by(returned= False)
    for loan in active_loans:
            if loan.return_date < datetime.date.today():
                late_loans.append(loan)
    return render_template ("late_loans.html", late_loans = late_loans)
# ~~~~~~~~~~~~~~ Loan Links ~~~~~~~~~~~~~~ #

# ~~~~~~~~~~ Operator's Options ~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~ TheLibrary Build ~~~~~~~~~~~~~~~~ #
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)