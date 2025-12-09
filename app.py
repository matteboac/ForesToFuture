from flask import Flask, render_template, redirect, url_for, request, flash, session
from forms import AdminLoginForm, AdminSignupForm, AboutContentForm
from models import db, Admin, Contact, AboutContent
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bawalsabihin123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final_project_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ========== PUBLIC ROUTES ==========

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    # Fetch dynamic content from database
    content = AboutContent.query.first()
    if not content:
        # Create default content if none exists
        content = AboutContent(
            general_objective="The primary objective of ForesToFuture is to raise nationwide awareness about Deforestation and Biodiversity Loss in the Philippines.",
            background_info="The Philippines is one of Earth's richest biodiversity hotspots, yet it faces one of the fastest rates of forest decline."
        )
        db.session.add(content)
        db.session.commit()
    return render_template("about.html", content=content)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    text = "If any case have a problem about this website, just contact us!"
    
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Save to database
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        
        flash("Message sent successfully!", "success")
        return redirect(url_for('contact'))
    
    return render_template("contact.html", text=text)

@app.route('/gallery')
def gallery():
    p = "Welcome to gallery page!"
    return render_template("gallery.html", p=p)

@app.route('/articles')
def articles():
    a = "Welcome to Articles page!"
    return render_template("articles.html", a=a)

# ========== ADMIN ROUTES ==========

@app.route('/admin/signup', methods=['GET', 'POST'])
def admin_signup():
    form = AdminSignupForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()

        if len(username) < 4 or len(password) < 6:
            flash("Username must be 4 or more characters. Password must be 6 or more characters.", "error")
            return redirect(url_for('admin_signup'))
        
        if Admin.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect(url_for('admin_signup'))
        
        new_admin = Admin(username=username)
        new_admin.set_password(password)
        
        db.session.add(new_admin)
        db.session.commit()
        
        flash("Admin account created successfully!", "success")
        return redirect(url_for('admin_login'))
    
    return render_template('admin_signup.html', form=form)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin and admin.check_password(form.password.data):
            session['admin_id'] = admin.id
            flash("Login successful!", "success")
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid username or password. Try again.", "error")
    return render_template('admin_login.html', form=form)

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        flash("Please log in to access the admin dashboard.", "error")
        return redirect(url_for('admin_login'))
    
    admin = Admin.query.get(session['admin_id'])
    contacts = Contact.query.all()
    about_content = AboutContent.query.first()
    
    return render_template('admin_dashboard.html', admin=admin, contacts=contacts, about_content=about_content)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    flash("Logged out successfully!", "success")
    return redirect(url_for('admin_login'))

@app.route('/admin/edit-about', methods=['GET', 'POST'])
def admin_edit_about():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    content = AboutContent.query.first()
    form = AboutContentForm(obj=content)
    
    if form.validate_on_submit():
        if not content:
            content = AboutContent()
            db.session.add(content)
        
        content.general_objective = form.general_objective.data
        content.background_info = form.background_info.data
        
        db.session.commit()
        flash("About page content updated successfully!", "success")
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin_edit_about.html', form=form)

@app.route('/admin/delete-contact/<int:contact_id>')
def admin_delete_contact(contact_id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    
    flash("Contact message deleted successfully!", "success")
    return redirect(url_for('admin_dashboard'))

# ========== MAIN ==========

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)