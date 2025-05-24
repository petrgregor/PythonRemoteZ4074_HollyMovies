# Projekt HollyMovies

## Django
### Instalace
```bash
pip install django
```
```bash
pip freeze > requirements.txt
```

### Vytvoření projektu
```bash
django-admin startproject <nazev_projektu> .
```

## .env soubor
```bash
pip install python-dotenv
```
Vytvořím soubor `.env` v kořenovém adresáři projektu,
vložím do tohoto souboru `SECRET_KEY`, ale bez mezer a uvozovek.

Do souboru `settings.py` importujeme modul `dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-)si+fpno3#)=7__vx-4%ni^&n1wvaz9bju1e+s8*i!e9qt!@f)')
```

### Vytvoření aplikace 
```bash
python manage.py startapp <nazev_aplikace>
```

> [!WARNING]
> Nesmíme zapomenout zaregistrovat aplikaci do souboru `settings.py`:
> ```python
> INSTALLED_APPS = [
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
>     
>     'viewer',
> ]
> ```

### Vytvoření databáze
```bash
python manage.py migrate
```

### Vytvoření superuser účtu
```bash
python manage.py createsuperuser
```