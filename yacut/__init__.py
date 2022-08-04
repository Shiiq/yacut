import os

from flask import Flask, Response, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .forms import ConvertURLForm
# from models import URL_map
# from settings import Config

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


@app.route('/')
def page_view():
    return Response('TEST PAGE ARRRWW')


@app.route('/convert', methods=['GET', 'POST'])
def convert_url():
    form = ConvertURLForm()
    print('TERMINAL INPUT TEST')
    print(form.__dict__)
    if form.validate_on_submit():
        print(form.__dict__)
        print(form.original_link.data)
        print(form.short_link.data)
        return render_template('form.html', form=form)
    return render_template('form.html', form=form)
    # if form.validate_on_submit():
    #     original_link = form.original_link.data
    #     if form.short_link.data is None:
    #         pass
    #     else:
    #         short_link = form.short_link.data
    #         pass
    # # render_template()
    # pass



# @app.route('/api/opinions/<int:id>/', methods=['GET'])
# @app.route('/api/id/', methods=['POST'])
