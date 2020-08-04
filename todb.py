import sys
import psycopg2
import os
import pandas as pd
from main import app
import requests
import zipfile


class Todo:

    def __init__(self):

        params_dic = {
            "host": "localhost",
            "database": "covid",
            "user": "postgres",
            "password": "12345"

        }
        path = ''
        conn = self.connect(params_dic)
        result = os.listdir(app.config['UPLOAD_FOLDER'])
        for item in result:
            if item.endswith('.{}'.format(app.config['EXTENSION'])):
                path = os.path.join(app.config['UPLOAD_FOLDER'], item)

        if path == '':
            self.download_url(app.config['URL'], app.config['ZIP_FILE'])
            f = self.from_zip(app.config['ZIP_FILE'], app.config['UPLOAD_FOLDER'])
        else:
            os.remove(path)
            self.download_url(app.config['URL'], app.config['ZIP_FILE'])
            f = self.from_zip(app.config['ZIP_FILE'], app.config['UPLOAD_FOLDER'])

        complete_f = app.config['UPLOAD_FOLDER']+f
        #df = pd.read_csv(complete_f, encoding='latin_1', chunksize=10000000)
        self.create_table(conn)
        self.copy_from_file(conn, complete_f)

    def create_table(self, conn):
        cursor = conn.cursor()
        cursor.execute("""
                DROP TABLE IF EXISTS daily;
                CREATE UNLOGGED TABLE daily (
                    fecha_actualizacion  TEXT,
                    id_registro  TEXT,
                    origen  TEXT,
                    sector TEXT,
                    entidad_um TEXT,
                    sexo  TEXT,
                    entidad_nac TEXT,
                    entidad_res TEXT,
                    municipio_res TEXT,
                    tipo_paciente TEXT,
                    fecha_ingreso TEXT,
                    fecha_sintomas TEXT,
                    fecha_def TEXT,
                    intubado TEXT,
                    neumonia TEXT,
                    edad TEXT,
                    nacionalidad TEXT,
                    embarazo TEXT,
                    habla_lengua_indig TEXT,
                    diabetes TEXT,
                    epoc TEXT,
                    asma TEXT,
                    inmusupr TEXT,
                    hipertension TEXT,
                    otra_com TEXT,
                    cardiovascular TEXT,
                    obesidad TEXT,
                    renal_cronica TEXT,
                    tabaquismo TEXT,
                    otro_caso TEXT,
                    resultado TEXT,
                    migrante TEXT,
                    pais_nacionalidad TEXT,
                    pais_origen TEXT,
                    uci TEXT
                );
            """)
        conn.commit()
        #conn.close()

    def connect(self, params_dic):
        conn = None
        try:
            print('conecting to db')
            conn = psycopg2.connect(**params_dic)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit(1)

        return conn

    def copy_from_file(self, conn, path):
        f = open(path, 'r')
        cursor = conn.cursor()

        try:
            copy_sql = """
            COPY daily from stdin WITH CSV HEADER
            DELIMITER as ','
            """
            cursor.copy_expert(sql=copy_sql, file=f)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            #os.remove(path)
            print("Error: %s" % error)
            conn.rollback()
            cursor.close()
            return 1
        print("copy_from_file() done")
        cursor.close()

    def download_url(self, url, save_path, chunk_size=128):
        r = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def from_zip(self, _PATH, _DIRNAME):
        with zipfile.ZipFile(_PATH, "r") as zip_ref:
            zip_ref.extractall(_DIRNAME)
            name = zip_ref.namelist()
        return name[0]