from waitress import serve
from flask import Flask,request,Response,jsonify,Blueprint

from flask_sqlalchemy import SQLAlchemy

import settings
from api.endpoints.standing import ns as standingNS
from api.endpoints.artefact import ns as artefactNS
from api.endpoints.render import ns as renderNS


from api.endpoints.standing import api
from api.endpoints.ui import *
from api.database import db

app = Flask(__name__)

pageUIMapping = [ [UIHandler,"/"],
                  [UIHandler,"/ui"] , 
                  [UIHandler,"/ui/"],
                  [ArtefactListUIHandler,"/ui/artefacts"],
                  [ArtefactUIHandler,"/ui/artefact"],
                  [AFSUIHandler,"/ui/AFS"],
                  [ATSUIHandler,"/ui/ATS"],
                  [ADTUIHandler,"/ui/ADT"],
                  [AFTUIHandler,"/ui/AFT"],
                  [ProcessUIHandler,"/ui/process"],
                  [LoadPlanUIHandler, "/ui/loadplan"],
                  [ProcessWrapperUIHandler, "/ui/workflows"],
                  [MonitoringUIHandler, "/ui/monitoring"]
                ]

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__)

    api.init_app(blueprint)
    api.add_namespace(standingNS)
    api.add_namespace(artefactNS)
    api.add_namespace(renderNS)
    
    for pm in pageUIMapping:
        handler = pm[0]
        path = pm[1]
        api.add_resource(handler,path)

    flask_app.register_blueprint(blueprint)
    db.app = flask_app
    db.init_app(flask_app)


initialize_app(app)


def main():
    serve(app, listen='0.0.0.0:5010')
    #app.run(debug=settings.FLASK_DEBUG,port=5010)

if __name__ == "__main__":
    main()
