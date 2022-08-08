from flask import abort, flash, redirect, render_template
from sqlalchemy.sql.expression import exists

from . import app, db, get_unique_id
from .constants import BASE_URL
from .forms import ConvertURLForm
from .models import URL_map


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    form = ConvertURLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data

        if not form.custom_id.data:
            id = get_unique_id()

        else:
            id = form.custom_id.data
            if db.session.query(
                    exists().where(URL_map.short == id)
            ).scalar():
                flash(
                    'Такой идентификатор уже есть в базе! Придумайте другой.', 'Fault'
                )
                return render_template('main.html', form=form)

        url_map = URL_map(
            original=original_link,
            short=id
        )
        db.session.add(url_map)
        db.session.commit()

        # Вывод сообщения с готовой короткой ссылкой
        short_link = url_map.get_short_link(BASE_URL)
        flash(short_link, 'Success')

    return render_template('main.html', form=form)


@app.route('/<id>', methods=['GET'])
def redirect_to_original(id):
    url_map = URL_map.query.filter_by(short=id).first()
    if url_map is None:
        abort(404)
    original_link = url_map.original
    return redirect(original_link)
