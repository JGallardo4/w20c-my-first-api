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
                        json.dumps(db.get_animal(_id), default=str),
                        mimetype="application/json",
                        status = 200
                    )                
            except Exception as e:
                print(e)
                return Response (
                    "Bad Request",
                    mimetype="text/plain",
                    status = 400
                )
        elif(db.get_animals()):
            return Response (
                json.dumps(db.get_animals(), default=str),
                mimetype="application/json",
                status = 200
            )
        else:
            return Response (
                "No content",
                mimetype="text/plain",
                status = 404
            )

    elif(request.method == "POST"):
        _common_name = request.form["common_name"]
        _scientific_name = request.form["scientific_name"]

        db.create_animal(_common_name, _scientific_name)

        return Response(
            "New animal added",
            mimetype = "text/plain",
            status = 200
        )

    elif(request.method == "PATCH"):
        _id = request.form["id"]
        _common_name = request.form["common_name"]
        _scientific_name = request.form["scientific_name"  ]     

        db.update_animal(_id, _common_name, _scientific_name)

        return Response(
            "Animal updated",
            mimetype = "text/plain",
            status = 200
        )

    elif(request.method == "DELETE"):
        _id = request.form["id"]
        db.delete_animal(_id)

        return Response(
            "Animal deleted",
            mimetype = "text/plain",
            status = 200
        )