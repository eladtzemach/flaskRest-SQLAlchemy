from db import db


# create a mapping between the database and the Client model
class clientModel(db.Model):

    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    postalcode = db.Column(db.String)
    country = db.Column(db.String)

    def __init__(self, id, name, email, phone, address, city, postalcode, country):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.country = country

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'phone': self.phone, \
                'address': self.address, 'city': self.city, 'postalcode': self.postalcode, 'country': self.country}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # the session (collection of objects) to be added to the db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # the session (collection of objects) to be deleted to the db
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()