from flask import Flask, render_template, redirect, url_for, request, flash,session
from forms import AdminLoginForm, AdminSignupForm
from models import db, Admin, Contact
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bawalsabihin123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final_project_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/admin/signup', methods=['GET', 'POST'])
def admin_signup():
    form = AdminSignupForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()

        if len(username) < 4 or len(password) < 6:
            flash("Username must be 4 or more characters. Password must be 6 or more characters. Please, try again")
            return redirect(url_for('admin_signup'))
        
        if Admin.query.filter_by(username=username).first():
            flash("Username already exists.")
            return redirect(url_for('admin_signup'))
        
        new_admin = Admin(username=username)
        new_admin.set_password(password)

        db.session.add(new_admin)
        db.session.commit()
        return redirect(url_for('admin_login'))
    return render_template('admin_signup.html', form=form)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and check_password_hash(admin.password_hash, form.password.data):
            session['admin_id'] = admin.id
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid username or password. Try again.")
    return render_template('admin_login.html', form=form)

@app.route('/admin/dashboard')
def admin_dashboard():

    if 'admin_id' not in session:
        flash("Please log in to access the admin dashboard.")
        return redirect(url_for('admin_login'))

    # Query admin info if needed
    admin = Admin.query.get(session['admin_id'])

    return render_template('admin_dashboard.html', admin=admin)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    flash("Logged out successfully!")
    return redirect(url_for('admin_login'))


@app.route('/about')
def about():
    info = "Flask is a simple microframework for Python"
    return render_template("about.html", info=info)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    text = "If any case have a problem about this website, just contact us!"

    if request.method == 'POST':
        # Extract data from form
        name = request.form.get("fullname")
        email = request.form.get("email")
        message = request.form.get("message")


    return render_template("contact.html", text=text)

@app.route('/gallery')
def gallery():
    p = "Welcome to gallery page!"
    return render_template("gallery.html", p=p)

@app.route('/articles')
def articles():
    a = "Welcome to Articles page!"
    return render_template("articles.html", a=a)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
