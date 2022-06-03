# ToDoList con DJango. 

This repo is for create a list for to do, you can add new tasks and create users

## Pre-requisitos
Instalar Python.
```zsh
sudo apt-get install python3
```

Instalar el entorno virtual.
```zsh
pip install virtualenv
```

## Instalación.
1. Clonar el repositorio.
2. Abra el folder de la carpeta.
3. Corra el compando:
```zsh
python3 -m venv venv
```
4. Active el entorno virtual (LINUX):
```zsh
source venv/bin/activate
```
4.1 Active el entorno virtual (WINDOWS):
```zsh
venv/Scripts/activate
```
5.Cree las migaciones:
```zsh
python manage.py makemigrations
```
6. Ejecute las migraciones.
```zsh
python manage.py migrate
```
7. Inicie la app base.
```zsh
python manage.py startapp base
```

8. Inicie el servidor.
```zsh
python manage.py runserver
```
