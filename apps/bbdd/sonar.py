import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()


def connect_to_db():
    database = r"" + os.environ["DATABASE"]
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn


def getDistinctAplicaciones():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute("SELECT DISTINCT aplicacion FROM metricas").fetchall()
        # for column in scores:
        #     print("columna : %s" % column[0])
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getDistinctProveedor():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT DISTINCT proveedor \
                                FROM proveedor \
                                INNER JOIN metricas on metricas.aplicacion=proveedor.aplicacion"
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getAllMetricas():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute("SELECT * FROM metricas").fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getMetricas():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT name, aplicacion, size, fecha, \
                                bugs, reliability_label, reliability_rating, \
                                vulnerabilities, security_rating, security_label, \
                                code_smells, sqale_rating, sqale_label, alert_status \
                                FROM metricas"
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getKpis():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT name, aplicacion, size, fecha, app_sonar, \
                                complexity, dloc_label, coverage_label, \
                                sqale_rating, sqale_label, alert_status \
                                FROM metricas"
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getAllMetricasbyProveedor(proveedor):
    # print("Realizando consulta")
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT * FROM metricas \
                                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                                WHERE proveedor.proveedor=?",
            (proveedor,),
        ).fetchall()
        # print(scores)
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getAllStatsbyProveedor(proveedor):
    # print("Realizando consulta")
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT * FROM stats \
                                INNER JOIN proveedor on proveedor.aplicacion=stats.aplicacion \
                                WHERE proveedor.proveedor=?",
            (proveedor,),
        ).fetchall()
        # print("Total rows are:  ", len(scores))
        # print("Printing each row")
        # for row in scores:
        #     for i in range(len(row)):
        #         print(row[i])
        #     print("\n")
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getMetricasbyProveedor(proveedor):
    # print("Realizando consulta")
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT name, metricas.aplicacion, size, fecha, \
                                bugs, reliability_label, reliability_rating, \
                                vulnerabilities, security_rating, security_label, \
                                code_smells, sqale_rating, sqale_label, alert_status \
                                FROM metricas \
                                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                                WHERE proveedor.proveedor=?",
            (proveedor,),
        ).fetchall()
        # print(scores)
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getAllHistoricobyAplicacion(aplicacion):
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT * FROM historico where aplicacion=?", (aplicacion,)
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getHistoricobyAplicacion(aplicacion):
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT name, historico.aplicacion, size, fecha, \
                                bugs, reliability_label, reliability_rating, \
                                vulnerabilities, security_rating, security_label, \
                                code_smells, sqale_rating, sqale_label, alert_status \
                                FROM historico where aplicacion=?",
            (aplicacion,),
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getHistoricobyRepo(aplicacion, name):
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT name, aplicacion, fecha, bugs, vulnerabilities, code_smells \
                            FROM historico where aplicacion=? and name=?",
            (aplicacion, name),
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def getRepositorios():
    scores = {}
    try:
        conn = connect_to_db()
        scores = conn.execute(
            "SELECT aplicacion, COUNT(*) AS NUM_REPO \
                            from metricas GROUP BY aplicacion \
                            HAVING COUNT(*) > 2 \
                            ORDER BY COUNT(*) DESC;"
        ).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def get_E_Reliability(proveedor):
    scores = {}
    try:
        conn = connect_to_db()
        query = "SELECT metricas.aplicacion, count(reliability_rating) from metricas \
                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                WHERE proveedor.proveedor='{}' and (metricas.reliability_rating='5' or metricas.reliability_rating='4') GROUP BY metricas.aplicacion".format(
            proveedor
        )
        # print(f"Realizando consulta : {query}")
        scores = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def get_C_Reliability(proveedor):
    scores = {}
    try:
        conn = connect_to_db()
        query = "SELECT metricas.aplicacion, count(reliability_rating) from metricas \
                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                WHERE proveedor.proveedor='{}' and metricas.reliability_rating='3' GROUP BY metricas.aplicacion".format(
            proveedor
        )
        # print(f"Realizando consulta : {query}")
        scores = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores


def get_A_Reliability(proveedor):
    scores = {}
    try:
        conn = connect_to_db()
        query = "SELECT metricas.aplicacion, count(reliability_rating) from metricas \
                INNER JOIN proveedor on proveedor.aplicacion=metricas.aplicacion \
                WHERE proveedor.proveedor='{}' and (metricas.reliability_rating='1' or metricas.reliability_rating='2') GROUP BY metricas.aplicacion".format(
            proveedor
        )
        # print(f"Realizando consulta : {query}")
        scores = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f"Error:{e}")
        conn.close()
    return scores
