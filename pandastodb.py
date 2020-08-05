import sqlalchemy as db
import pandas as pd
import pandas.io.sql
import json
import flask_jsonpify


class JsonSelect():

    def __init__(self):
        engine = db.create_engine("postgresql://postgres:12345@localhost/covid")
        connection = engine.connect()
        results = engine.execute('SELECT * FROM daily')
        query = 'SELECT * FROM daily'
        n_rows = results.fetchall()
        print(len(n_rows), type(n_rows))
        print(n_rows[0])
        index = 0
        self.json_format = {}
        for entry in n_rows:
            self.json_format[index] = entry
            index += 1
