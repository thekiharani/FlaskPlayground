from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.session import make_transient

# from .admin.routes import admin
# from .api.routes import api
# from .site.routes import site

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thekiharani:pass12345word!@127.0.0.1:5442/flask_dev'
db = SQLAlchemy(app)


# app.register_blueprint(admin)
# app.register_blueprint(api)
# app.register_blueprint(site)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.title


@app.route('/')
def index():
    # user = User(name='Jay Kiharani', location='Ruiru Bypass')
    # db.session.add(user)
    # db.session.commit()
    #
    # post1 = Post(user_id=user.id, title='Flask Model Cloning', body='We are doing amazing stuff here today...')
    # post2 = Post(user_id=user.id, title='Django Model Cloning', body='We started odd, now we are even...')
    # db.session.add(post1)
    # db.session.add(post2)
    # db.session.commit()
    users = User.query.all()
    posts = Post.query.all()

    for user in users:
        new_name = user.name + ' Updated'
        db.session.expunge(user)
        make_transient(user)
        user.name = new_name
        user.date_created = datetime.utcnow()
        user.id = None
        db.session.add(user)
        db.session.commit()

    for post in posts:
        new_title = post.title + ' Updated'
        db.session.expunge(post)
        make_transient(post)
        post.title = new_title
        post.date_created = datetime.utcnow()
        post.id = None
        db.session.add(post)
        db.session.commit()

    return 'New records created!'


if __name__ == '__main__':
    app.run(debug=True)
