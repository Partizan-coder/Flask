from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_migrate import Migrate



PG_DSN = 'postgresql://postgres:y@ppizO9@127.0.0.1:5432/db_flask'
app = Flask('my_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Header = db.Column(db.String, index=True, unique=True)
    Description = db.Column(db.String)
    Create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    Owner = db.Column(db.String, index=True)

def check_health():
    return jsonify({
        'status': 'ok'
    })

def test():
    req = request
    print(req)
    return jsonify({})



app.add_url_rule('/health', view_func=check_health, methods=['GET'])
app.add_url_rule('/test', view_func=test, methods=['POST'])
app.run(host='0.0.0.0', port=8080)