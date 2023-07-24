from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class Bikes(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)
    price = db.Column(db.Numeric(9, 2))
    make = db.Column(db.String)
    bike_model = db.Column(db.String)
    year = db.Column(db.Integer)
    img = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self,title,rating,price,make,bike_model,year,img):
        self.title = title
        self.rating = rating
        self.price = price
        self.make = make
        self.bike_model = bike_model
        self.year = year
        self.img = img
   

    def save_bike(self):
        db.session.add(self)
        db.session.commit()
        

    def save_chnages(self):
        db.session.commit()


    def to_dic(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'rating' : self.rating,
            'price' : self.price,
            'make' : self.make,
            'model' : self.bike_model,
            'year' : self.year,
            'img' : self.img
                
        }


  
