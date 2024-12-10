from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Notes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    notes = Notes.query.all()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    text = request.form.get('text')
    new_note = Notes(text=text)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_note/<int:id>', methods=['POST'])
def delete_note(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)