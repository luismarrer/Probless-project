### Entorno de desarrollo
## Entorno virtual
Para el entorno virtual se utilizará pipenv.
- pipenv=2024.0.3
Documentación: https://pipenv.pypa.io/en/latest/
Documentación en español: https://pipenv-es.readthedocs.io/es/latest/
La instalación es:
```
$ pip install --user pipenv
```
## Resto de herramientas
- Visual Studio Code (Versión más actualizada)
- Python=3.10
- pip=24.2
- django=5.1.1
- django-ckeditor=6.7.1
- pillow=10.4.0
- pylint=3.3.1
- pylint-django=2.5.5
- pylint-celery=0.3
```
$ pipenv install django django-ckeditor Pillow pylint pylint-django pylint-celery
```
## Configuración de VSC para Django
[Configurar VSC para Django (Actualizado 03/2024)](https://gist.github.com/hcosta/6e4066ad1b938c888546c5f0a9616c48)
## Inicializar Django
```
$ pipenv run django-admin startproject probless
```
## Jerarquía del proyecto
```
probless-backend/
    manage.py
    probless/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Configurar base de datos
En `probless/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE':
        'django.db.backends.mysql',
        'NAME': '***',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': '***',
        'PORT': '***'
    }
}
```
Correr servidor es `runserver`
Sincronización inicial de la base de datos: `python manage.py migrate`
En producción `DEBUG = False`

