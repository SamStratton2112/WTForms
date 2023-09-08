from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__='pets'

    def __repr__(self):
        p = self
        return f'<Name={p.name}, ID={p.id}, Species={p.species}>'

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(30),
                    nullable=False)
    species = db.Column(db.String(30))
    photo_url = db.Column(db.String, default='https://www.maricopa-sbdc.com/wp-content/uploads/2020/11/image-coming-soon-placeholder.png')
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, default=True)

    
