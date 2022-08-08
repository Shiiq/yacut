from flask import flash, redirect, render_template
from sqlalchemy.sql.expression import exists


from . import app, db
from .constants import BASE_URL
from .forms import ConvertURLForm
from .models import URL_map, get_unique_id


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id_view():
    """
    Функция для обработки страницы с генератором коротких ссылок.
    """
    form = ConvertURLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        # Если идентификатор не был введен, то генерируем сами
        if not form.custom_id.data:
            id = get_unique_id()
        # Если идентификатор был введен, то проверяем его уникальность
        else:
            id = form.custom_id.data
            if db.session.query(
                    exists().where(URL_map.short == id)
            ).scalar():
                flash(f'Имя {id} уже занято!', 'Fault')
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
def redirect_to_original_view(id):
    """
    Функция для редиректа с короткой ссылки на исходную.
    """
    url_map = URL_map.query.filter_by(short=id).first_or_404()
    original_link = url_map.original
    return redirect(original_link)
