from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..database.models import *
from ..handlers.monitoring import *
from flask_restplus import abort
import traceback

from flask_restplus import Api

api = Api(version='1.0', title='ETL MEta',doc='/doc/',description='ETL Meta API')


ns = api.namespace('api/monitoring', description='MOnitoring Data')


@ns.route('/monitoring')
class Artefact(Resource):
   
    def get(self):
        response,code = getAllArtefacts()
        return response, code

@ns.route('/artefact/<string:ArtefactID>')
class SingleArtefact(Resource):
    @api.expect(ArtefactRecord)
    def put(self,ArtefactID):
        response,code = updateSingleArtefact(ArtefactID,request)
        return response, code
    def get(self,ArtefactID):
        response,code = getSingleArtefact(ArtefactID)
        return response, code
    def delete(self,ArtefactID):
        response,code = deleteSingleArtefact(ArtefactID)
        return response, code
