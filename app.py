from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from forms import (AdminLoginForm, AdminSignupForm, AboutContentForm, 
                   DeforestationDataForm, CountryMetadataForm, BiodiversityStatusForm, CountryForm)
from models import db, Admin, Contact, AboutContent, DeforestationData, CountryMetadata, Country, BiodiversityStatus
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bawalsabihin123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final_project_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ========== PUBLIC ROUTES ==========

# Home page
@app.route('/')
def home():
    return render_template("home.html")

# About page – displays project objectives and background
@app.route('/about')
def about():
    content = AboutContent.query.first()
    if not content:
        content = AboutContent(
            general_objective="The primary objective of ForesToFuture is to raise nationwide awareness about Deforestation and Biodiversity Loss in the Philippines.",
            background_info="The Philippines is one of Earth's richest biodiversity hotspots, yet it faces one of the fastest rates of forest decline."
        )
        db.session.add(content)
        db.session.commit()
    return render_template("about.html", content=content)

# Contact page – handles contact form submissions
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    text = "If any case have a problem about this website, just contact us!"
    
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        
        flash("Message sent successfully!", "success")
        return redirect(url_for('contact'))
    
    return render_template("contact.html", text=text)

# Gallery page
@app.route('/gallery')
def gallery():
    p = "Welcome to gallery page!"
    return render_template("gallery.html", p=p)

# Articles page
@app.route('/articles')
def articles():
    a = "Welcome to Articles page!"
    return render_template("articles.html", a=a)

# ========== DEFORESTATION ROUTES ==========

# Deforestation visualization page
@app.route('/deforestation')
def deforestation():
    return render_template("deforestation.html")

# API endpoint – returns deforestation data for a specific country
@app.route('/api/deforestation/<country>')
def get_deforestation_data(country):
    try:
        data = DeforestationData.query.filter_by(country=country).order_by(DeforestationData.year).all()
        metadata = CountryMetadata.query.filter_by(country=country).first()
        
        if not data:
            return jsonify({'error': 'Country not found'}), 404
        
        response = {
            'country': country,
            'years': [d.year for d in data],
            'percentages': [d.deforestation_percentage for d in data],
            'hectares': [d.forest_loss_hectares for d in data],
            'metadata': {
                'total_loss': metadata.total_forest_loss_2015_2025 if metadata else 0,
                'avg_rate': metadata.avg_annual_loss_rate if metadata else 0,
                'description': metadata.description if metadata else ''
            }
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API endpoint – returns list of available countries with deforestation data
@app.route('/api/deforestation/countries')
def get_countries():
    try:
        countries = db.session.query(DeforestationData.country).distinct().all()
        return jsonify({'countries': [c[0] for c in countries]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ========== BIODIVERSITY ROUTES ==========

# Biodiversity page – shows dropdown of countries
@app.route('/biodiversity')
def biodiversity():
    countries = [c.name for c in Country.query.order_by(Country.name).all()]
    return render_template('biodiversity.html', countries=countries)

# API endpoint – returns biodiversity data for a country
@app.route("/api/biodiversity/<country>")
def biodiversity_api(country):
    rows = BiodiversityStatus.query.join(Country)\
        .filter(Country.name == country)\
        .order_by(BiodiversityStatus.year).all()

    if not rows:
        return jsonify({"error": "No data found for this country"}), 404

    return jsonify({
        "years": [r.year for r in rows],
        "affected_species": [r.affected_species for r in rows],
        "ecosystem_health_index": [r.ecosystem_health_index for r in rows]
    })

# ========== ADMIN ROUTES ==========

# Admin signup page
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

# Admin login page
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

# Admin dashboard – overview of system data
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        flash("Please log in to access the admin dashboard.", "error")
        return redirect(url_for('admin_login'))
    
    admin = Admin.query.get(session['admin_id'])
    contacts = Contact.query.all()
    about_content = AboutContent.query.first()
    
    total_countries = db.session.query(DeforestationData.country).distinct().count()
    total_records = DeforestationData.query.count()
    total_biodiversity = BiodiversityStatus.query.count()
    total_biodiversity_countries = Country.query.count()
    
    return render_template('admin_dashboard.html', 
                         admin=admin, 
                         contacts=contacts, 
                         about_content=about_content,
                         deforestation_countries=total_countries,
                         deforestation_records=total_records,
                         biodiversity_records=total_biodiversity,
                         biodiversity_countries=total_biodiversity_countries)

# Admin logout route
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    flash("Logged out successfully!", "success")
    return redirect(url_for('admin_login'))

# Admin edit about route – edit the About page content (objective and background)
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

# Admin delete contact route – delete a contact message submitted by a user
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

# ========== ADMIN DEFORESTATION DATA MANAGEMENT ==========

# Admin deforestation route – view all deforestation records and metadata
@app.route('/admin/deforestation')
def admin_deforestation():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    data_records = DeforestationData.query.order_by(DeforestationData.country, DeforestationData.year).all()
    metadata_records = CountryMetadata.query.order_by(CountryMetadata.country).all()
    
    return render_template('admin_deforestation.html', 
                         data_records=data_records,
                         metadata_records=metadata_records)

# Admin deforestation add route – add new deforestation data
@app.route('/admin/deforestation/add', methods=['GET', 'POST'])
def admin_add_deforestation():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    form = DeforestationDataForm()
    
    if form.validate_on_submit():
        existing = DeforestationData.query.filter_by(
            country=form.country.data,
            year=form.year.data
        ).first()
        
        if existing:
            flash("Data for this country and year already exists!", "error")
            return redirect(url_for('admin_add_deforestation'))
        
        new_data = DeforestationData(
            country=form.country.data,
            year=form.year.data,
            deforestation_percentage=form.deforestation_percentage.data,
            forest_loss_hectares=form.forest_loss_hectares.data,
            notes=form.notes.data
        )
        
        db.session.add(new_data)
        db.session.commit()
        
        flash("Deforestation data added successfully!", "success")
        return redirect(url_for('admin_deforestation'))
    
    return render_template('admin_deforestation_form.html', form=form, action='Add')

# Admin deforestaion edit route – edit existing deforestation data
@app.route('/admin/deforestation/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit_deforestation(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    data = DeforestationData.query.get_or_404(id)
    form = DeforestationDataForm(obj=data)
    
    if form.validate_on_submit():
        data.country = form.country.data
        data.year = form.year.data
        data.deforestation_percentage = form.deforestation_percentage.data
        data.forest_loss_hectares = form.forest_loss_hectares.data
        data.notes = form.notes.data
        
        db.session.commit()
        
        flash("Deforestation data updated successfully!", "success")
        return redirect(url_for('admin_deforestation'))
    
    return render_template('admin_deforestation_form.html', form=form, action='Edit')

# Admin deforestation delete route – delete a deforestation record
@app.route('/admin/deforestation/delete/<int:id>')
def admin_delete_deforestation(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    data = DeforestationData.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    
    flash("Deforestation data deleted successfully!", "success")
    return redirect(url_for('admin_deforestation'))

# Admin metadata route – add metadata for a country
@app.route('/admin/metadata/add', methods=['GET', 'POST'])
def admin_add_metadata():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    form = CountryMetadataForm()
    
    if form.validate_on_submit():
        existing = CountryMetadata.query.filter_by(country=form.country.data).first()
        
        if existing:
            flash("Metadata for this country already exists!", "error")
            return redirect(url_for('admin_add_metadata'))
        
        new_metadata = CountryMetadata(
            country=form.country.data,
            total_forest_loss_2015_2025=form.total_forest_loss_2015_2025.data,
            avg_annual_loss_rate=form.avg_annual_loss_rate.data,
            description=form.description.data
        )
        
        db.session.add(new_metadata)
        db.session.commit()
        
        flash("Country metadata added successfully!", "success")
        return redirect(url_for('admin_deforestation'))
    
    return render_template('admin_metadata_form.html', form=form, action='Add')

# Admin metadata edit route – edit country metadata
@app.route('/admin/metadata/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit_metadata(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    metadata = CountryMetadata.query.get_or_404(id)
    form = CountryMetadataForm(obj=metadata)
    
    if form.validate_on_submit():
        metadata.country = form.country.data
        metadata.total_forest_loss_2015_2025 = form.total_forest_loss_2015_2025.data
        metadata.avg_annual_loss_rate = form.avg_annual_loss_rate.data
        metadata.description = form.description.data
        
        db.session.commit()
        
        flash("Country metadata updated successfully!", "success")
        return redirect(url_for('admin_deforestation'))
    
    return render_template('admin_metadata_form.html', form=form, action='Edit')

# Admin metadata delete route – delete country metadata
@app.route('/admin/metadata/delete/<int:id>')
def admin_delete_metadata(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    metadata = CountryMetadata.query.get_or_404(id)
    db.session.delete(metadata)
    db.session.commit()
    
    flash("Country metadata deleted successfully!", "success")
    return redirect(url_for('admin_deforestation'))

# ========== ADMIN BIODIVERSITY DATA MANAGEMENT ==========

# Admin biodiversity route – view all biodiversity records
@app.route('/admin/biodiversity')
def admin_biodiversity():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    biodiversity_records = BiodiversityStatus.query.join(Country).order_by(
        Country.name, BiodiversityStatus.year
    ).all()
    
    countries = Country.query.order_by(Country.name).all()
    
    return render_template('admin_biodiversity.html', 
                         biodiversity_records=biodiversity_records,
                         countries=countries)

# Admin biodiversity add route – add new biodiversity data
@app.route('/admin/biodiversity/add', methods=['GET', 'POST'])
def admin_add_biodiversity():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    form = BiodiversityStatusForm()
    
    if form.validate_on_submit():

        country = Country.query.filter_by(name=form.country_name.data).first()
        
        if not country:
            country = Country(name=form.country_name.data)
            db.session.add(country)
            db.session.flush()  
        
        existing = BiodiversityStatus.query.filter_by(
            country_id=country.id,
            year=form.year.data
        ).first()
        
        if existing:
            flash("Data for this country and year already exists!", "error")
            return redirect(url_for('admin_add_biodiversity'))
        
        new_data = BiodiversityStatus(
            country_id=country.id,
            country_name=form.country_name.data,
            year=form.year.data,
            affected_species=form.affected_species.data,
            ecosystem_health_index=form.ecosystem_health_index.data
        )
        
        db.session.add(new_data)
        db.session.commit()
        
        flash("Biodiversity data added successfully!", "success")
        return redirect(url_for('admin_biodiversity'))
    
    return render_template('admin_biodiversity_form.html', form=form, action='Add')

# Admin biodiversity edit route – edit biodiversity data
@app.route('/admin/biodiversity/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit_biodiversity(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    data = BiodiversityStatus.query.get_or_404(id)
    form = BiodiversityStatusForm(obj=data)
    
    if form.validate_on_submit():

        country = Country.query.filter_by(name=form.country_name.data).first()
        
        if not country:
            country = Country(name=form.country_name.data)
            db.session.add(country)
            db.session.flush()
        
        data.country_id = country.id
        data.country_name = form.country_name.data
        data.year = form.year.data
        data.affected_species = form.affected_species.data
        data.ecosystem_health_index = form.ecosystem_health_index.data
        
        db.session.commit()
        
        flash("Biodiversity data updated successfully!", "success")
        return redirect(url_for('admin_biodiversity'))
    
    return render_template('admin_biodiversity_form.html', form=form, action='Edit')

# Admin biodiversity delete route – delete a biodiversity record
@app.route('/admin/biodiversity/delete/<int:id>')
def admin_delete_biodiversity(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    data = BiodiversityStatus.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    
    flash("Biodiversity data deleted successfully!", "success")
    return redirect(url_for('admin_biodiversity'))

# ========== ADMIN COUNTRY MANAGEMENT ==========


# Admin countries route – view all countries
@app.route('/admin/countries')
def admin_countries():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    countries = Country.query.order_by(Country.name).all()
    return render_template('admin_countries.html', countries=countries)


# Admin country add route – add a new country
@app.route('/admin/countries/add', methods=['GET', 'POST'])
def admin_add_country():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    form = CountryForm()
    
    if form.validate_on_submit():
        existing = Country.query.filter_by(name=form.name.data).first()
        
        if existing:
            flash("Country already exists!", "error")
            return redirect(url_for('admin_add_country'))
        
        new_country = Country(name=form.name.data)
        db.session.add(new_country)
        db.session.commit()
        
        flash(f"Country '{form.name.data}' added successfully!", "success")
        return redirect(url_for('admin_countries'))
    
    return render_template('admin_country_form.html', form=form, action='Add')

# Admin country edit route – edit an existing country
@app.route('/admin/countries/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit_country(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    country = Country.query.get_or_404(id)
    form = CountryForm(obj=country)
    
    if form.validate_on_submit():
        existing = Country.query.filter(Country.name == form.name.data, Country.id != id).first()
        
        if existing:
            flash("Country name already exists!", "error")
            return redirect(url_for('admin_edit_country', id=id))
        
        country.name = form.name.data
        db.session.commit()
        
        flash(f"Country updated successfully!", "success")
        return redirect(url_for('admin_countries'))
    
    return render_template('admin_country_form.html', form=form, action='Edit')

# Admin country delete route – delete a country (only if no biodiversity records exist)
@app.route('/admin/countries/delete/<int:id>')
def admin_delete_country(id):
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    country = Country.query.get_or_404(id)

    biodiversity_count = BiodiversityStatus.query.filter_by(country_id=id).count()
    
    if biodiversity_count > 0:
        flash(f"Cannot delete '{country.name}' - it has {biodiversity_count} biodiversity record(s). Delete those first.", "error")
        return redirect(url_for('admin_countries'))
    
    db.session.delete(country)
    db.session.commit()
    
    flash(f"Country '{country.name}' deleted successfully!", "success")
    return redirect(url_for('admin_countries'))

# Test route – used to verify database data
@app.route('/test-data')
def test_data():
    countries = db.session.query(DeforestationData.country).distinct().all()
    count = DeforestationData.query.count()
    metadata_count = CountryMetadata.query.count()
    
    return f"""
    <h2>Database Test</h2>
    <p>Total deforestation records: {count}</p>
    <p>Total country metadata: {metadata_count}</p>
    <p>Countries: {[c[0] for c in countries]}</p>
    """

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)