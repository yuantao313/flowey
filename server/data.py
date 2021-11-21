import sqlite3

config = {
    "dbfilepath": "./db.sqlite"
}


class Data:
    conn=None
    cursor=None
    def __init__(self, config):
        if self.conn is None:
            self.conn = sqlite3.connect(config["dbfilepath"])
        if self.cursor == None:
            self.cursor = self.conn.cursor()
    def execute(self,sql:str,*params):
        return self.cursor.execute(sql,params)

d=Data(config)
