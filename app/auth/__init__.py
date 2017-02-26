#!/usr/bin/env python 3.5
# -*- coding:utf-8 -*-
__author__ = 'hanyong'

from flask import Blueprint
auth = Blueprint('auth',__name__)
from . import views