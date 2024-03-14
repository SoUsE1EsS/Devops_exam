from flask import Flask, render_template, request, flash
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import *

# Создание БД
create_models(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    incidents = db.session.execute(db.select(Incident)).scalars()
    incident_by_key = None

    if request.method == 'POST':
        key = request.form.get('key')
        incident_by_key = db.session.execute(db.select(Detailes).filter(Detailes.key == key)).scalar()
        if not incident_by_key:
            flash('Неизвестный ключ','warning')


    return render_template('index.html', incidents=incidents, incident_by_key=incident_by_key) 
