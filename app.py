from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

password = '1234'
PG_DSN = f'postgresql://flask:{password}@127.0.0.1:5432/db_flask'
app = Flask('my_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AnnouncementModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Header = db.Column(db.String(128), index=True, unique=True)
    Description = db.Column(db.String(128))
    Create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    Owner = db.Column(db.String(128), index=True)

class AnnouncementView(MethodView):

    def get(self, id):
        announcement = AnnouncementModel.query.get(int(id))
        if announcement is not None:
            return jsonify({'Header': announcement.Header, 'Create_date': announcement.Create_date})
        else:
            response = jsonify({'error': 'not found'})
            response.status_code = 404
            return response

    def post(self):
        new_announcement = AnnouncementModel(**request.json)
        db.session.add(new_announcement)
        db.session.commit()
        return jsonify(
            {
                'id': new_announcement.id,
                'Create_date': new_announcement.Create_date
            }
        )

    def delete(self, id):
        delete_announcement = AnnouncementModel.query.get(int(id))
        db.session.delete(delete_announcement)
        db.session.commit()
        return


app.add_url_rule('/announcement', view_func=AnnouncementView.as_view('announcement_create'), methods=['POST'])
app.add_url_rule('/announcement/<int:id>', view_func=AnnouncementView.as_view('announcement_get'), methods=['GET'])
app.add_url_rule('/announcement/<int:id>/delete', view_func=AnnouncementView.as_view('announcement_delete'), methods=['DELETE'])
app.run(host='0.0.0.0', port=8080)