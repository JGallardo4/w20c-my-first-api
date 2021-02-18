from flask import Flask, request, Response, jsonify
import json
import mariadb
import db

app = Flask(__name__)

@app.route("/animals", methods=["GET", "POST", "PATCH", "DELETE"])
def get_animals():
    if(request.method == "GET"):
        if(request.form):
            try:
                _id = request.form["id"]
                if _id:
                    return Response(
                        json.dumps(db.getAnimal(_id), default=str),
                        mimetype="application/json",
                        status = 200
                    )                
            except Exception as e:
                print(e)
                return Response (
                    "Bad Request",
                    mimetype="application/json",
                    status = 400
                )
        else:
            return Response (
                json.dumps(db.getAnimals(), default=str),
                mimetype="application/json",
                status = 200
            )            
    elif(request.method == "POST"):
        _common_name = request.form["common_name"]
        _scientific_name = request.form["scientific_name"]

        db.createAnimal(_common_name, _scientific_name)

        return Response(
            json.dumps({'success':True}),
            mimetype = "application/json",
            status = 200
        )
    elif(request.method == "PATCH"):
        print(request)

        _id = request.form.get("id")
        _common_name = request.form.get("common_name")
        _scientific_name = request.form.get("scientific_name")        

        db.updateAnimal(_id, _common_name, _scientific_name)

        # return Response(
        #     "Login Form",
        #     mimetype = "text/html",
        #     status = 200
        # )

    elif(request.method == "DELETE"):
        print(request)

        db.deleteAnimal(request.form.get("id"))

        # return Response(
        #     "Login Form",
        #     mimetype = "text/html",
        #     status = 200
        # )