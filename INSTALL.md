# 👩🏼‍💻 🚀 Developer Environment Setup
## Prerequisites
1.  Python 3.6+
2.  VS Code (to make collaboration easier. We don't want to argue over tabs vs spaces!)
3.  MongoDB Cloud Account: After setting up your free account on [MongoDB](https://www.mongodb.com/cloud/atlas/register) cloud, you will have a username, password and the database connection string.
## Setup
1.  Clone this repository to your local machine.

2.  Change terminal to repository directory and create a new virtual environment using venv: `path/to/python -m venv .venv`

3.  Activate virtual environment:<br/>
Linux/MacOS:  `source .venv/bin/activate`<br/>
Windows:  `.venv/Scripts/activate`<br/>

4.  Install Python dependencies
```Text
pip install -r requirements.txt
```
5.  Add your MongoDB connection string and user credentials to the `config.yml` file in the repository root directory.

6.  Start the development server using the following commands 
```Text
python manage.py migrate
python manage.py runserver
```
