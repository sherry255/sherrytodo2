from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import sql


app = Flask(__name__)
app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    __tabelname__ ='todos'

    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(200))
    # set default time
    timestamp = db.Column(db.DateTime(timezone=True),default=sql.func.now())

    def __repr__(self):
        # str.format() is much better than '%()'
        return u'<Todo {0} {1}'.format(self.id, self.task)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    print('rebuild database')

