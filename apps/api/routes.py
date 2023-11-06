from flask import jsonify, redirect, url_for

import apps.bbdd.sonar as consulta
from apps.api import api


@api.route("/historico/<project>")
def historico_project(project):
    data = {}
    scores = consulta.getHistoricobyAplicacion(project)
    data["project_name"] = [row[0] for row in scores]
    data["aplicacion"] = [row[1] for row in scores]
    data["data"] = [row[3] for row in scores]
    data["bugs"] = [row[4] for row in scores]
    data["vulnerabilities"] = [row[7] for row in scores]
    data["codesmells"] = [row[10] for row in scores]
    return jsonify(data)


@api.route("/historico/<project>/<name>")
def historico_name(project, name):
    data = {}
    scores = consulta.getHistoricobyRepo(project, name)
    data["project_name"] = [row[0] for row in scores]
    data["aplicacion"] = [row[1] for row in scores]
    data["data"] = [row[2] for row in scores]
    data["bugs"] = [row[3] for row in scores]
    data["vulnerabilities"] = [row[4] for row in scores]
    data["codesmells"] = [row[5] for row in scores]
    return jsonify(data)


@api.route("/show/historico/<project>/<name>")
def show_historico_name(project, name):
    return redirect(url_for("home.charts_test"))


@api.route("/charts_data")
def charts_data():
    data = {}
    scores = consulta.getRepositorios()
    labels = [row[0] for row in scores]
    values = [row[1] for row in scores]
    data["labels"] = labels
    data["values"] = values
    return jsonify(data)


@api.route("/rating/reliability/<proveedor>")
def rating(proveedor):
    data = {}
    scoresA = consulta.get_A_Reliability(proveedor)
    data["reliability_A"] = [row[0] for row in scoresA]
    data["reliability_A_relia"] = [row[1] for row in scoresA]

    scoresC = consulta.get_C_Reliability(proveedor)
    data["reliability_C"] = [row[0] for row in scoresC]
    data["reliability_C_relia"] = [row[1] for row in scoresC]

    scoresE = consulta.get_E_Reliability(proveedor)
    data["reliability_E"] = [row[0] for row in scoresE]
    data["reliability_E_relia"] = [row[1] for row in scoresE]

    return jsonify(data)


@api.route("/show/proveedores")
def show_proveedores():
    data = {}
    scores = consulta.getDistinctProveedor()
    data["proveedores"] = [row[0] for row in scores]
    return jsonify(data)


@api.route("/show/aplicaciones")
def show_aplicaciones():
    data = {}
    scores = consulta.getDistinctAplicaciones()
    data["aplicaciones"] = [row[0] for row in scores]
    return jsonify(data)
