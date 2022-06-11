from flask import jsonify, request
from app import app, response
from app.controller import PromoController

# Read and add promos
@app.route('/promos', methods = ['GET','POST'])
def promo():
    if request.method == 'GET':
        return PromoController.index()
    else :
        return PromoController.addPromo()

# CRUD promo
@app.route('/promos/<int:id>', methods = ['GET','PUT', 'DELETE'])
def promos(id):
    if request.method == 'PUT':
        return PromoController.updatePromo(id)
    if request.method == 'DELETE':
        return PromoController.deletePromo(id)
    else :
        return PromoController.show(id)