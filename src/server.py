from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus
from aiogram.utils import executor
from database import *
from telegram import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///id.db'
db = SQLAlchemy(app)


class Id(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Id %r>' % self.id


@app.route('/', methods=['GET'])
async def check_id():
    if request.method == 'GET':
        identifier = request.args.get('id')

        if identifier is None:
            return 'No identifier provided', HTTPStatus.BAD_REQUEST

        if identifier == '':
            return 'Empty identifier provided', HTTPStatus.BAD_REQUEST

        if check_id_in_database(identifier, Id):
            return 'Identifier found in database'
        else:
            await send_notification_to_telegram(f"Identifier {identifier} not found in database", identifier)
            return 'Identifier not found in database. Notification sent to Telegram'
    else:
        return 'Method not allowed', HTTPStatus.METHOD_NOT_ALLOWED


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
