from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.secret_key = 'dev-secret-123'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a real secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example with SQLite, change to your database URI
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='posts')

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def valid_invite(invite_code):
    try:
        with open('invites.txt', 'r') as file:
            valid_invites = file.readlines()
            # Strip any leading/trailing whitespaces and check if the code is valid
            valid_invites = [invite.strip() for invite in valid_invites]
            return invite_code in valid_invites
    except FileNotFoundError:
        # If the invites file doesn't exist, return False or handle as needed
        flash("Invite file not found.")
        return False


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
        if not valid_invite(invite):  # You'll need to implement valid_invite
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
    new_post = Post(content=content, user_id=current_user.id)  # ✅ Use user_id
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('feed'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)  # Listen on all network interfaces

