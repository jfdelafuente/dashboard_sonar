from datetime import datetime

from flask import abort, render_template, request

import apps.bbdd.sonar as consulta
from apps.home import home


@home.route("/")
@home.route("/index")
def index():
    return render_template("home/index.html", scores=consulta.getMetricas())


@home.route("/layout-static")
def layout_static():
    return render_template("home/layout-static.html")


@home.route("/layout-sidenav-light")
def layout_sidenav_light():
    return render_template("home/layout-sidenav-light.html")


@home.route("/metricas")
def metricas():
    return render_template("home/metricas/metricas.html", scores=consulta.getMetricas())


@home.route("/historico", methods=("GET", "POST"))
def historico():
    apps = consulta.getDistinctAplicaciones()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/metricas/historico.html",
            apps=apps,
            scores=consulta.getHistoricobyAplicacion(project),
            proveedor=project,
        )
    else:
        return render_template("home/metricas/historico.html", apps=apps)


@home.route("/proveedores", methods=("GET", "POST"))
def proveedores():
    apps = consulta.getDistinctProveedor()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/metricas/proveedores.html",
            apps=apps,
            scores=consulta.getMetricasbyProveedor(project),
            proveedor=project,
        )
    else:
        return render_template("home/metricas/proveedores.html", apps=apps)


@home.route("/charts")
def charts():
    return render_template("home/charts/charts.html")


@home.route("/charts_test")
def charts_test():
    scores = consulta.getRepositorios()
    labels = [row[0] for row in scores]
    values = [row[1] for row in scores]
    return render_template(
        "home/charts/charts_test.html",
        labels=labels,
        values=values,
        date=datetime.now(),
    )


@home.route("/charts_historico", methods=("GET", "POST"))
def charts_historico():
    return render_template(
        "home/charts/charts_historico.html",
        apps=consulta.getDistinctAplicaciones(),
        date=datetime.now(),
    )


@home.route("/admin")
def admin():
    abort(404)


@home.route("/kpis")
def kpis():
    return render_template("home/kpis/kpis.html", scores=consulta.getKpis())


@home.route("/kpis_proveedores", methods=("GET", "POST"))
def kpis_proveedores():
    apps = consulta.getDistinctProveedor()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/kpis/kpis_proveedores.html",
            apps=apps,
            scores=consulta.getAllMetricasbyProveedor(project),
            proveedor=project,
        )
    else:
        return render_template("home/kpis/kpis_proveedores.html", apps=apps)


@home.route("/kpis_historico", methods=("GET", "POST"))
def kpis_historico():
    apps = consulta.getDistinctAplicaciones()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/kpis/kpis_historico.html",
            apps=apps,
            scores=consulta.getAllHistoricobyAplicacion(project),
            proveedor=project,
        )
    else:
        return render_template("home/kpis/kpis_historico.html", apps=apps)


@home.route("/stats")
def stats():
    return render_template("home/stats/stats.html", scores=consulta.getKpis())


@home.route("/stats_proveedores", methods=("GET", "POST"))
def stats_proveedores():
    apps = consulta.getDistinctProveedor()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/stats/stats_proveedores.html",
            apps=apps,
            scores=consulta.getAllStatsbyProveedor(project),
            proveedor=project,
        )
    else:
        return render_template("home/stats/stats_proveedores.html", apps=apps)


@home.route("/stats_historico", methods=("GET", "POST"))
def stats_historico():
    apps = consulta.getDistinctAplicaciones()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/stats/stats_historico.html",
            apps=apps,
            scores=consulta.getAllHistoricobyAplicacion(project),
            proveedor=project,
        )
    else:
        return render_template("home/stats/stats_historico.html", apps=apps)
