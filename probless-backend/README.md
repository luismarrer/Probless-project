# Entorno de desarrollo
## Entorno virtual
Para el entorno virtual se utilizará pipenv.
- Versión usada: `pipenv=2024.0.3`\
Documentación: https://pipenv.pypa.io/en/latest/ \
Documentación en español: https://pipenv-es.readthedocs.io/es/latest/ \
La instalación es:
```
$ pip install pipenv
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

Con el uso del Pipfile solo es necesario correr el siguiente comando para que se inicialize el entorno virtual con las dependencias:
```
$ pipenv install
```
## Configuración de VSC para Django
[Configurar VSC para Django (Actualizado 03/2024)](https://gist.github.com/hcosta/6e4066ad1b938c888546c5f0a9616c48)
[Django Template](https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-html)

## Inicializar proyecto de Django
```
$ pipenv run django-admin startproject probless
```
## Jerarquía del proyecto
```
probless-backend/
	account/
    manage.py
	core/
    probless/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
	workspace/
```

## Configurar base de datos
Para usar Mysql se debe cambiar la configuración por defecto en `probless/settings.py` por:
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

Correr servidor es `python manage.py runserver`\
Sincronización inicial de la base de datos: `python manage.py migrate`

## Sobre produción
En producción se debe configurar `DEBUG = False`. Se encuentra en `probless/settings.py`.
[Documentación sobre Deploy con Render](https://docs.render.com/deploy-django)
