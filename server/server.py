from flask import Flask, request
from data import Data
import os
import random

app = Flask(__name__)


@app.route("/")
def _():
    return "hello"


@app.route("/getCanteen")
def getCanteen():
    return {"data": [{
        "name": "一食堂一层",
        "id": 11,
        "interest": 1500
    },
        {
            "name": "一食堂二层",
            "id": 12,
            "interest": 1000
        },
        {
            "name": "一食堂三层",
            "id": 13,
            "interest": 3000
        },
        {
            "name": "二食堂一层",
            "id": 21,
            "interest": 2000
        },
        {
            "name": "二食堂二层",
            "id": 22,
            "interest": 2500
        },
        {
            "name": "咖咖西餐厅",
            "id": 31,
            "interest": 4000
        }
    ]}


@app.route("/getRecommendation")
def getRecommendation():
    response = {"data": []}
    d = Data({"dbfilepath": os.getcwd() + "\\server\\db.sqlite"})
    result = d.execute("SELECT * FROM 'dish'")
    for i in result:
        response["data"].append({
            "id": i[1],
            "name": i[3],
            "info": i[4],
            "imgsrc": i[5]
        })
    response["data"] = random.sample(response["data"], 10)
    random.shuffle(response["data"])
    return response


@app.route("/getRestaurantByCid")
def getRestaurantByCid():
    d = Data({"dbfilepath": os.getcwd() + "\\server\\db.sqlite"})
    cid = request.args["id"]
    response = {"restaurants": [], "canteen": None, "status": "success"}
    result = d.execute("SELECT * FROM 'canteen' WHERE `cid`=" + str(cid)).fetchone()
    response["canteen"] = {
        "id": result[1],
        "name": result[2],
        "info": result[3],
        "imgsrc": "666"
    }
    result = d.execute("SELECT * FROM 'restaurant' WHERE `cid`= " + str(cid)).fetchall()
    for i in result:
        response["restaurants"].append({
            "id": i[1],
            "name": i[3],
            "info": "canteen_name",
            "imgsrc": i[5]
        })
    if len(response["restaurants"]) == 0:
        return {"status": "failure"}
    return response


@app.route("/getDishByRid")
def getDishByRid():
    d = Data({"dbfilepath": os.getcwd() + "\\server\\db.sqlite"})
    rid = request.args["id"]
    response = {"dishes": [], "restaurant": None, "status": "success"}
    result = d.execute("SELECT * FROM 'restaurant' WHERE `rid`=" + str(rid)).fetchone()
    response["restaurant"] = {
        "id": result[1],
        "name": result[3],
        "info": result[4],
        "imgsrc": result[5]
    }
    result = d.execute("SELECT * FROM 'dish' WHERE `rid`= " + str(rid)).fetchall()
    for i in result:
        response["dishes"].append({
            "id": i[1],
            "name": i[3],
            "info": "canteen_name",
            "imgsrc": i[5]
        })
    if len(response["dishes"]) == 0:
        return {"status": "failure"}
    return response


@app.route('/getDetailInfo')
def getDetailInfo():
    d = Data({"dbfilepath": os.getcwd() + "\\server\\db.sqlite"})
    id = request.args["id"]
    if int(id) < 100:
        sql = "SELECT * FROM 'canteen' WHERE `cid`=" + id
    elif int(id) < 10000:
        sql = "SELECT * FROM 'restaurant' WHERE `rid`=" + id
    else:
        sql = "SELECT * FROM 'dish' WHERE `did`=" + id
    response = {"status": "success", "target": {}, "comments": []}
    result = d.execute(sql).fetchone()
    response["target"] = {
        "id": result[1],
        "name": result[3],
        "info": result[4],
        "imgsrc": result[5]
    }
    id = 110101
    sql = "SELECT * FROM 'comment' WHERE related=" + str(id)
    result = d.execute(sql).fetchall()
    for i in result:
        response["comments"].append({
            "id": i[1],
            "value": i[3],
            "like": i[4]
        })
    random.shuffle(response["comments"])
    response["comments"]=response["comments"][:10]

    return response


if __name__ == "__main__":
    app.run()
