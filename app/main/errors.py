#!/usr/bin/env python 3.5
# -*- coding:utf-8 -*-
__author__ = 'hanyong'

from flask import render_template, request, jsonify
from . import main

def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response

@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error':'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error':'not found'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500
