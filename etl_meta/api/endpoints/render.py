from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..database.models import *
from ..handlers.artefact import *
from flask_restplus import abort
import traceback

from flask_restplus import Api

api = Api(version='1.0', title='ETL MEta',doc='/doc/',description='ETL Meta API')


ns = api.namespace('render', description='Render Files')

@ns.route('/standing_js')
class StandingJS(Resource):
    def get(self):      
        
        render_template("/js/app.js")