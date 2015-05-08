
======================
Leonardo Site Template
======================


Installation
============

.. code-block:: bash

    virtualenv -p /usr/bin/python2.7 leonardo_venv
    cd leonardo_venv
    source bin/activate

    pip install django-leonardo

    django-admin startproject --template=https://github.com/django-leonardo/site-template/archive/master.zip myproject

    cd myproject

    manage.py makemigrations --noinput
    manage.py migrate --noinput

    manage.py runserver 0.0.0.0:80