from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change to a real secret key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

### Models ###
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

### Invite System ###
def valid_invite(code):
    if not os.path.exists('invites.txt'):
        return False
    with open('invites.txt') as f:
        invites = f.read().splitlines()
    if code in invites:
        invites.remove(code)
        with open('invites.txt', 'w') as f:
            f.write('\n'.join(invites))
        return True
    return False

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

### Routes ###
@app.route('/')
@login_required
def feed():
    posts = Post.query.order_by(Post.id.desc()).all()  # Fetch all posts
    return render_template("feed.html", posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        invite = request.form['invite']
        if not valid_invite(invite):
            flash("Invalid invite code.")
            return redirect(url_for('register'))
        if User.query.filter_by(username=username).first():
            flash("Username already taken.")
            return redirect(url_for('register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('feed'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('feed'))
        flash("Invalid credentials")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/post', methods=['POST'])
@login_required
def post():
    content = request.form['content']
    new_post = Post(content=content, author_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('feed'))

if __name__ == '__main__':
    db.create_all()  # Creates database tables if they don't exist yet
    app.run(debug=True)
