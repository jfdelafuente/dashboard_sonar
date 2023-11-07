import json


def test_get_historico_by_project(test_client):
    response = test_client.get("/api/historico/amonosp")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    assert res["project_name"][0] == "amonmonorepo-application-typescript"
    assert res["aplicacion"][0] == "amonosp"
    assert response.status_code == 200


def test_get_historico_by_name(test_client):
    response = test_client.get(
        "/api/historico/amonosp/amonmonorepo-application-typescript"
    )
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    assert res["project_name"][0] == "amonmonorepo-application-typescript"
    assert res["aplicacion"][0] == "amonosp"
    assert response.status_code == 200


def test_get_repos(test_client):
    response = test_client.get("/api/charts_data")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    # assert res['labels'] == 1
    # assert res['values'] == 'Havard'
    assert response.status_code == 200


def test_show_proveedores(test_client):
    response = test_client.get("/api/show/proveedores")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    # assert res['labels'] == 1
    # assert res['values'] == 'Havard'
    assert response.status_code == 200


def test_show_aplicaciones(test_client):
    response = test_client.get("/api/show/aplicaciones")
    res = json.loads(response.data.decode("utf-8"))
    print(res)
    # assert res['labels'] == 1
    # assert res['values'] == 'Havard'
    assert response.status_code == 200
