================
systeminfo_flask
================


.. image:: https://img.shields.io/pypi/v/systeminfo_flask.svg
        :target: https://pypi.python.org/pypi/systeminfo_flask

.. image:: https://img.shields.io/travis/harshrpg/systeminfo_flask.svg
        :target: https://travis-ci.org/harshrpg/systeminfo_flask

.. image:: https://readthedocs.org/projects/systeminfo-flask/badge/?version=latest
        :target: https://systeminfo-flask.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




This is flask application which can be run as a console script that will provide the information of the system it is installed in. It uses a private module systeminfo that can installed from https://guthub.com/harshrpg/systeminfo


* Free software: MIT license
* Documentation: https://systeminfo-flask.readthedocs.io.


Features
--------


This application is developed on flask using a private package called ``systeminfo`` to display the information of the platform this app is installed on. To use this application simply follow the following steps:

Installation
-------------

This application uses private package called ``systeminfo``. This package is a prerequisite of this flask app. If you haven't installed it yet then please follow from Step 1 otherwise you can skip step 1 and continue from step 2:

1. Install ``systeminfo`` by executing the following command::
        
        pip install git+https://github.com/harshrpg/systeminfo.git



2. Install this app from this repository::

        pip install git+https://git@github.com/harshrpg/systeminfo_flask.git

3. Once installation is complete, simply execute the command ``getPlatformInfo``::  
      
        $ getPlatformInfo


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
