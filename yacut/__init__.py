import os

from flask import Flask, Response, flash, redirect, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from settings import Config

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .forms import ConvertURLForm
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/')
def page_view():
    return Response('MAIN PAGE ARRRWW')


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    form = ConvertURLForm()
    if form.validate_on_submit():
        original_link = form.original.data
        print(50 * '-')
        print(not form.short.data)
        print(50 * '-')
        print(URL_map.query.filter_by(short=form.short.data).exn)
        # if not form.short.data:
        #     short_id = get_unique_short_id()
        # else:
        #     short_id = form.short.data
        # if URL_map.query.filter_by(short=form.short.data).first():
        #     flash('Такой идентификатор уже есть в базе! Придумайте другой.')
        #     return render_template('main.html', form=form)
        # url_map = URL_map(
        #     original=original_link,
        #     short=short_id
        # )
        # db.session.add(url_map)
        # db.session.commit()
        # return redirect('/')
    return render_template('main.html', form=form)
