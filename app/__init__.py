from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.template_filter('time_badge_sm')
def time_badge_sm(h):
    if 5 <= h < 21:
        return 1
    else:
        return 2


app.jinja_env.filters['time_badge_sm'] = time_badge_sm


from app import views, models