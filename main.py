from flask_jsonpify import jsonify
from flask_marshmallow import Marshmallow
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import os



app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object('config.ProductionConfig')
ma = Marshmallow(app)
import models
from todb import Todo


class Data(db.Model):
    __tablename__ = 'daily'
    #index = db.Column(db.Integer, primary_key=True)
    fecha_actualizacion = db.Column(db.String(40))
    id_registro = db.Column(db.String(40), primary_key=True)
    origen = db.Column(db.Integer)
    sector = db.Column(db.Integer)
    entidad_um = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    entidad_nac = db.Column(db.Integer)
    entidad_res = db.Column(db.Integer)
    municipio_res = db.Column(db.Integer)
    tipo_paciente = db.Column(db.Integer)
    fecha_ingreso = db.Column(db.String(40))
    fecha_sintomas = db.Column(db.String(40))
    fecha_def = db.Column(db.String(40))
    intubado = db.Column(db.Integer)
    neumonia = db.Column(db.Integer)
    edad = db.Column(db.Integer)
    nacionalidad = db.Column(db.Integer)
    embarazo = db.Column(db.Integer)
    habla_lengua_indig = db.Column(db.Integer)
    diabetes = db.Column(db.Integer)
    epoc = db.Column(db.Integer)
    asma = db.Column(db.Integer)
    inmusupr = db.Column(db.Integer)
    hipertension = db.Column(db.Integer)
    otra_com = db.Column(db.Integer)
    cardiovascular = db.Column(db.Integer)
    obesidad = db.Column(db.Integer)
    renal_cronica = db.Column(db.Integer)
    tabaquismo = db.Column(db.Integer)
    otro_caso = db.Column(db.Integer)
    resultado = db.Column(db.Integer)
    migrante = db.Column(db.Integer)
    pais_nacionalidad = db.Column(db.String(40))
    pais_origen = db.Column(db.String(40))
    uci = db.Column(db.Integer)






def create_dir():
    if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
    return 'done'

@app.route('/')
def hola_mundo():
    create_dir()
    return 'Hola mundo Covid'


@app.route('/download')
def download():
    cosa = Todo()
    print('funciona')
    return 'hecho'
    return 'downloaded'


@app.route('/reszip', methods=['GET', 'POST'])
def rezip():
    result = os.listdir(app.config['UPLOAD_FOLDER'])
    ext = 'csv'
    for item in result:
        if item.endswith('.{}'.format(ext)):
            path = os.path.join(app.config['UPLOAD_FOLDER'], item)
    return \
        send_from_directory(app.config['UPLOAD_FOLDER'], item, as_attachment=True)



@app.route('/storedb')
def storedb():
    result = os.listdir(app.config['DB_FOLDER'])
    ext = 'sqlite3'
    for item in result:
        if item.endswith('.{}'.format(ext)):
            path = os.path.join(app.config['DB_FOLDER'], item)
    return \
        send_from_directory(app.config['DB_FOLDER'], item, as_attachment=True)

@app.route('/query')
def query_db():
    covid = Data.query.all()
    return print(covid)


@app.route('/pruebas')
def pruebas():
    from pruebas import Prueba
    cosa = Prueba()
    return cosa.json_output




if __name__ == '__main__':
    app.run(debug=True)
