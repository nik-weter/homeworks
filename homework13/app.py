from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config

#app = Flask(__name__, template_folder='templates')
#app.config.from_object(config)

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)

@app.route('/')
def home():
    from models import GuestBookItem
    from forms import GuestBookForm

    posts = GuestBookItem.query.all()
    print(posts)
    for post in posts:
        author = post.author
        content = post.content
    return render_template('home.txt', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def index():
    from models import GuestBookItem
    from forms import GuestBookForm

    if request.method == 'POST':
        print(request.form)
        form = GuestBookForm(request.form)

        if form.validate():
            item = GuestBookItem(**form.data)
            db.session.add(item)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = GuestBookItem.query.all()
    for post in posts:
        author = post.author
        content = post.content
    return '{} {}'.format(author, content)

def populate_db():
    print('Creating default user')
    # Creating new ones:
    item = GuestBookItem(author='Ivan', content ='U-ha-ha!')

    db.session.add(item)
    db.session.commit()  # note

if __name__ == '__main__':
    from models import *
    db.create_all()

    if GuestBookItem.query.count() == 0:
        populate_db()

    print('App runs!')

    # Running app:
    app.run()