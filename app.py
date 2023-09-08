from flask import Flask, request, render_template, redirect
from models import db, connect_db, Pet

from forms import AddPetForm
from forms import EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """renders home page"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def get_add_form():
    """render add pet form and handel addition of pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:id>')
def get_pet_info(id):
    """show pet information and edit button"""
    pet = Pet.query.get_or_404(id)
    return render_template('pet_details.html', pet=pet)

@app.route('/<int:id>/edit', methods=['GET','POST'])
def edit_pet_form(id):
    """edit pet information form"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{id}')
    else:
        print(form.errors)
        return render_template('edit_pet.html', pet=pet, form=form)
