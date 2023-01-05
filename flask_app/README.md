# TODOS - MongoDB by Alon Itzhaky

The following project is a ToDo Management Application, helping you keep track of all the important missions you have to do in your day-to-day life.

# Technologies Used
- Python3
- Flask
- Jinja2
- MongoDB

# Pre-requisites

Please make sure you have Python and 'pip' installed on your OS. 
Additionally, you must install MongoDB Community and MongoDB Compass.
If it is not installed, please refer to the link below and follow the steps: **The proccess is identical between Windows and Mac.**

[Link to Python Installation](https://www.python.org/downloads/)
<br>

[Link to GeeksForGeeks - pip installation](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

[Link to MongoDB - Installation of Database](https://www.mongodb.com/docs/manual/administration/install-community/)

# Step-by-step Tutorial

1. Once all pre-requisites are compeleted, please run the following command in your VSCode / PyCharm Terminal in order to install 'virtualenv': 
```bash
python -m pip install virtualenv
```

2. Once 'virtualenv' is installed, we will now create a virtual environment to isolate the OS' current state, in order to not affect any existing data: 

### Mac
```bash
virtualenv env
```
### Windows
```bash
python -m virtualenv env
```

3. Next step will be activating the newly created virtual environment, by typing the next command into Terminal: 

### Mac
```bash
source env/bin/activate
```
### Windows
```bash
.\env\Scripts\activate
```

4. Once all the previous steps were completed, install the 'requirements.txt' in the main directory to make sure all required packages for this code exist: 
```bash
pip install -r requirements.txt
```

5. Run MongoDB Compass with this link: 
```
mongodb://localhost:27017
```

6. Activate the MongoDB Community Server by entering the next command into a new Terminal / PowerShell window: 
```bash
(env) mongosh
```

7. Run the application using the play icon in your VSCode / PyCharm environment, or by entering the command below:

### Mac
```bash
(env) $ python app.py
```
### Windows
```bash
(env) $ py app.py
```

8. Once code is active, go to your desired browser and type "http://127.0.0.1:5000". 

9. In order to check if the task has been added to your database, on your mongosh shell Terminal window, enter the following commands: 
```bash
$ test> use flask_db
$ flask_db> db.todos.find()
```
# Existing Features

- Add a To-Do (mark importance)
- Delete a To-Do

## Authors

- [Alon Itzhaky](https:/www.instagram.com/alon.itzhaky)

## Creators

![Credits](https://img.shields.io/badge/Creator-Alon%20Itzhaky-informational)



