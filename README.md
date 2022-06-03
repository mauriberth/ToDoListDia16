# To Do List Django's Project

This repo is for create a list for to do, you can add new tasks and create users

## Prerequisites
Install python
```zsh
sudo apt-get install python3
```

Then you can install a virtual environment
```zsh
pip install virtualenv
```

## Installation
1. clone the repository
2. Go to folder in your terminal 
3. Run the command
```zsh
python3 -m venv venv
```
4. Activates the virtual environment
```zsh
source venv/bin/activate
```
5. Run migrations
```zsh
python manage.py migrate
```
6. Start app base
```zsh
python manage.py startapp base
```

7. Now you can start the server
```zsh
python manage.py runserver
```
