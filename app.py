# enter your python code here
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app, version='1.0', title='Medication Data API',
          description='API to save medication data in Postgres database')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/db_name'
db = SQLAlchemy(app)

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(100), nullable=False)
   
    column1 = db.Column(db.String(100), nullable=True)
    column2 = db.Column(db.String(100), nullable=True)

@api.route('/medications')
class MedicationList(Resource):
    medication_model = api.model('Medication', {
        'id': fields.Integer(readOnly=True, description='The medication unique identifier'),
        'product_name': fields.String(required=True, description='The product name'),
        'name': fields.String(description='The name of the medication'),
        'type': fields.String(description='The type of the medication'),
        'quantity': fields.String(description='The quantity of the medication'),
        'column1': fields.String(description='Column 1'),
        'column2': fields.String(description='Column 2'),
    })

    @api.expect(medication_model)
    def post(self):
        data = request.get_json()
        product_name = data['product_name']
        name, type, quantity = product_name.split(' ', 2)
        medication = Medication(product_name=product_name, name=name, type=type, quantity=quantity, **data)
        db.session.add(medication)
        db.session.commit()
        return {'message': 'Medication data saved successfully'}, 201

    @api.marshal_list_with(medication_model)
    def get(self):
        medications = Medication.query.all()
        return medications

if __name__ == '__main__':
    app.run(debug=True)
