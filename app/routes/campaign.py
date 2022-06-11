from flask import jsonify, request
from app import app, response
from app.controller import CampaignController

# Read and add campaigns
@app.route('/campaigns', methods = ['GET','POST'])
def campaign():
    if request.method == 'GET':
        return CampaignController.index()
    else :
        return CampaignController.addCampaign()

# CRUD campaign
@app.route('/campaigns/<int:id>', methods = ['GET','PUT', 'DELETE'])
def campaigns(id):
    if request.method == 'PUT':
        return CampaignController.updateCampaign(id)
    if request.method == 'DELETE':
        return CampaignController.deleteCampaign(id)
    else :
        return CampaignController.show(id)
    
@app.route('/campaigns/<int:id>/change_active', methods = ['PUT'])
def change_active(id):
    return CampaignController.changeActive(id)

@app.route('/campaigns/apply-campaign', methods=['PUT'])
def apply_campaign():
    return CampaignController.applyCampaign()