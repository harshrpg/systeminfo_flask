# -*- coding: utf-8 -*-

"""Top-level package for Hello World Flask."""

__author__ = """Harsh Gupta"""
__email__ = 'harsh.gupta@ucdconnect.ie'
__version__ = '0.1.0'
import click
from flask import Flask
app = Flask(__name__)
app.debug=False
from app import views