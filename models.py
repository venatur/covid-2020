from main import db


class Data(db.Model):
    #__tablename__ = 'daily'
    index = db.Column(db.Integer, primary_key=True)
    fecha_actualizacion = db.Column(db.String(40))
    id_registro = db.Column(db.String(40))
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


class Cars(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())