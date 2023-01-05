
![Logo](./static/library.png)

# The Library by Alon Itzhaky

The following code is a representation of a librarian's view, as a project given to me by John Bryce Training, as part of my Python course assignments. 

# Pre-requisites
- Please make sure you have Python and 'pip' installed on your OS. 
If it is not installed, please refer to the link below and follow the steps: **The proccess is identical between Windows and Mac.**

[Link to Python Installation](https://www.python.org/downloads/)
<br>

[Link to GeeksForGeeks - pip installation](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

# Step-by-step Tutorial

1. Once all pre-requisites are compeleted, please run the following command in your VSCode / PyCharm Terminal in order to install 'virtualenv': 
```bash
python -m pip install virtualenv
```

2. Once 'virtualenv' is installed, we will now create a virtual environment to isolate the OS' current state, in order to not affect any existing data: 

### Mac
```bash
virtualenv venv
```
### Windows
```bash
python -m virtualenv venv
```

4. Next step will be activating the newly created virtual environment, by typing the next command into Terminal: 

### Mac
```bash
source venv/bin/activate
```
### Windows
```bash
.\venv\Scripts\activate
```

3. Once all the previous steps were completed, install the 'requirements.txt' in the main directory to make sure all required packages for this code exist: 
```bash
pip install -r requirements.txt
```

4. Run the application using the play icon in your VSCode / PyCharm environment:

### Mac
```bash
python Project1.py
```
### Windows
```bash
py Project1.py
```

5. Once code is active, go to your desired browser and type "http://127.0.0.1:5000". 

# Existing Features
- Database population on mainpage
- Adding a new customer
- Adding a new book
- Loan a book
- Return a book
- Display all books
- Display all customers
- Display all loans
- Display late loans
- Find a book by name
- Find a customer by name
- Delete a book
- Delete a customer

## Authors

- [Alon Itzhaky](https:/www.instagram.com/alon.itzhaky)

## Creators

![Credits](https://img.shields.io/badge/Creator-Alon%20Itzhaky-informational)



