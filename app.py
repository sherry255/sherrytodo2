from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import todo


app = Flask(__name__)


@app.route('/')
def index():
    todos = todo.Todo.query.all()
    return render_template("index.html",todos=todos)


@app.route('/add/',methods=['post'])
def add():
    t = request.form['todo']
    #use unicode(), not str(), for Chinese chars
    newTodo =todo.Todo(task=unicode(t))
    todo.db.session.add(newTodo)
    todo.db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<todo_id>/')
def delete(todo_id):
    t = todo.Todo.query.get(int(todo_id))
    todo.db.session.delete(t)
    todo.db.session.commit()

    return redirect(url_for('index'))


if __name__ =='__main__':
    app.run(debug=True)
