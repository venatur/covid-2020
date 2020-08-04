import psycopg2
import json

class Prueba():
    def __init__(self):
        params_dic = {
            "host": "localhost",
            "database": "covid",
            "user": "postgres",
            "password": "12345"

        }
        conn = psycopg2.connect(**params_dic)
        self.rows = self.enlistar(conn)
        self.json_output = json.dumps(self.rows)

    def enlistar(self, conn):
        rows = []
        try:

            cur = conn.cursor()
            cur.execute("select * from daily")
            row_headers = [x[0] for x in cur.description]
            rows = cur.fetchall()
            json_data = []
            for result in rows:
                json_data.append(dict(zip(row_headers,result)))
                print (result)
            # rows = [dict((cur.description[i][0], value) \
            #           for i, value in enumerate(row)) for row in cur.fetchall()]
            print("the number of parts: ", cur.rowcount)
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return json.dumps(json_data)