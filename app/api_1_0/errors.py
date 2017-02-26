#!/usr/bin/env python 3.5
# -*- coding:utf-8 -*-
__author__ = 'hanyong'

from flask import render_template, request, jsonify
from . import api

def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response

def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response

def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response
