#!/usr/bin/env python3.5
# -*- coding:utf-8 -*-
__author__ = 'hanyong'

from flask_bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flasky:123456@localhost:3306/flaskydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
manage = Manager(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.SmallInteger,primary_key = True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship('User',backref = 'role')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.SmallInteger,primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64),unique = True, index = True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.SmallInteger, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

db.drop_all()
db.create_all()
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(email='john@126.com', username='john',role=admin_role)
user_susan = User(email='susan@126.com', username='susan',role=user_role)
user_david = User(email='david@126.com', username='david',role=user_role)
db.session.add_all([admin_role,mod_role,user_role,user_john,user_susan,user_david])
db.session.commit()

@app.route('/',methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,
                           name=session.get('name'),
                           known=session.get('known', False))

if __name__ == '__main__':
    app.run()