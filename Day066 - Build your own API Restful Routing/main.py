import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
API_KEY = "TopSecretAPIKey"
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()

def to_dict(self):
    # Method1
    dictionary = {}
    for column in self.__table__.columns:
        # Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self,column.name)
    return dictionary

    #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    return {column.name: getattr(self.colunm.name) for column in self.__table__.columns}



@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods = ['GET'])
def random_cafe():
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
        random_cafe = random.choice(all_cafes)
        """
        return jsonify(cafe={
            #Omit the id
            #id = random_cafe.id
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            #Put some propretis in a sub category
            "amenities": {
                "seats": random_cafe.seats,
                "has_toilet": random_cafe.has_toilet,
                "has_wifi": random_cafe.has_wifi,
                "has_sockets": random_cafe.has_sockets,
                "can_take_calls":random_cafe.can_take_calls,
                "coffee_price": random_cafe.coffee_price
            }
        })
        """
        # Simply convert the random_cafe data record to a dictionary of key-value pairs.
        return jsonify(to_dict(random_cafe))

## HTTP GET - All cafes
@app.route("/all", methods = ['GET'])
def all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])

## HTTP GET - All cafes
@app.route("/search", methods = ['GET'])
def search_cafe():
    cafe_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[to_dict(cafe) for cafe in all_cafes])
    else:
        return jsonify({
            "error": "Sorry, we don't have a cafe at that location."
        }), 404


## HTTP POST - Create Record
@app.route("/add", methods = ['POST'])
def add_cafe():
    new_cafe= Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({
            "response": {
                "sucess": "Successfully added the new cafe"
            }
        })



## HTTP PUT/PATCH - Update Record
## HTTP GET - All cafes
@app.route("/update-price/<int:cafe_id>", methods = ['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(respose={"success": "Successfully updated price"})
    except Exception as e:
        return jsonify({
            "error":
            {
                "Not Found": "Sorry a cafe with that id was not found in our database."
            }
        }), 404



## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        cafe_to_close = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe_to_close:
            db.session.delete(cafe_to_close)
            db.session.commit()
            return jsonify(resopnse={"Success": "Successfully deleted."}), 200
        else:
            return jsonify(error={"error": "Sorry, cafe with that id was not found in the database."}), 404
    else:
        return jsonify(response={"Forbidden": "Sorry, that's not allowed, make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
