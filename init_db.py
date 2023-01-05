"""
The purpose of this file is for the database to be populated with preset information.
Please do not tamper with this file and its contents in order to prevent malfunctioning code.
"""

import datetime
from app import Customers, Books, Loans, app, db

print('The database has been populated.')

# ---------- Customers:
customer_1 = Customers(customer_name = "Kenya Norton", customer_age = 22, customer_city = "New York")
customer_2 = Customers(customer_name = "Duncan Suaerez" , customer_age = 44, customer_city = "Miami")
customer_3 = Customers(customer_name = "Nikki Kirkpatrick", customer_age = 76, customer_city = "Hollywood")
customer_4 = Customers(customer_name = "Sandra Ferrell", customer_age = 12, customer_city = "New Jersey")
customer_5 = Customers(customer_name = "Hanan Shaffer", customer_age = 52, customer_city = "Louisville")

# ---------- Books:
book_1 = Books(book_name = "Phantom Of Sorrow", book_author = "Darragh Alcock", published = "2008", book_type = 1)
book_2 = Books(book_name = "Agent With Gold", book_author = "Gaia Hatfield", published = "2002", book_type = 2)
book_3 = Books(book_name = "Creators With Strength", book_author = "Eduardo Middleton", published = "2010", book_type = 3)
book_4 = Books(book_name = "Bandits Of Greatness", book_author = "Harlen Sharpe", published = "2006", book_type = 1)
book_5 = Books(book_name = "Pilots And Rebels", book_author = "Dolcie Sweeney", published = "2004", book_type = 2)

# # ---------- Loans:
loan_1 = Loans(customer_id = 1, book_id = 1, loan_date = datetime.datetime.strptime('2022-10-26', '%Y-%m-%d'), return_date = datetime.datetime.strptime('2022-10-28', '%Y-%m-%d'))
loan_2 = Loans(customer_id = 2, book_id = 2, loan_date = datetime.datetime.strptime('2022-10-08', '%Y-%m-%d'), return_date = datetime.datetime.strptime('2022-10-13', '%Y-%m-%d'))
loan_3 = Loans(customer_id = 3, book_id = 3, loan_date = datetime.datetime.strptime('2022-10-15', '%Y-%m-%d'), return_date = datetime.datetime.strptime('2022-10-17', '%Y-%m-%d'))
loan_4 = Loans(customer_id = 4, book_id = 4, loan_date = datetime.datetime.strptime('2022-10-20', '%Y-%m-%d'), return_date = datetime.datetime.strptime('2022-10-30', '%Y-%m-%d'))
loan_5 = Loans(customer_id = 5, book_id = 5, loan_date = datetime.datetime.strptime('2022-11-02', '%Y-%m-%d'), return_date = datetime.datetime.strptime('2022-11-07', '%Y-%m-%d'))

with app.app_context():
    db.session.add_all([customer_1, customer_2, customer_3, customer_4, customer_5])
    db.session.add_all([book_1, book_2, book_3, book_4, book_5])
    db.session.add_all([loan_1, loan_2, loan_3, loan_4, loan_5])
    db.session.commit()