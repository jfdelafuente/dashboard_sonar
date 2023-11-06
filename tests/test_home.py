def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"INFOCODES - Home Page | Orange" in response.data


def test_home_page_all(test_client):
    pages = ["", "metricas", "proveedores", "historico"]
    for page in pages:
        response = test_client.get("/{}".format(page))
        assert response.status_code == 200


def test_kpis_page_all(test_client):
    pages = ["", "kpis", "kpis_proveedores", "kpis_historico"]
    for page in pages:
        response = test_client.get("/{}".format(page))
        assert response.status_code == 200


def test_stats_page_all(test_client):
    pages = ["", "stats", "stats_proveedores", "stats_historico"]
    for page in pages:
        response = test_client.get("/{}".format(page))
        assert response.status_code == 200


def test_home_page_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' (Method Not Allowed) status code is returned
    """

    response = test_client.post("/")
    assert response.status_code == 405
    assert b"Flask User Management Example!" not in response.data


def test_metricas_page(test_client):
    response = test_client.get("/metricas")
    assert response.status_code == 200
    assert b"INFOCODES - Metricas | Orange" in response.data


def test_proveedores_metricas_page(test_client):
    response = test_client.get("/proveedores")
    assert response.status_code == 200
    assert b"INFOCODES - Proveedores Metricas | Orange" in response.data


def test_historico_metricas_page(test_client):
    response = test_client.get("/historico")
    assert response.status_code == 200
    assert b"INFOCODES - Historico Metricas | Orange" in response.data


def test_proveedores_page_post(test_client):
    proveedor = "HP"
    pages = ["/proveedores", "kpis_proveedores", "stats_proveedores"]
    for page in pages:
        response = test_client.post(page, data={"project_name": proveedor})
        assert response.status_code == 200


def test_historico_page_post(test_client):
    project = "bscsosp"
    pages = ["/historico", "kpis_historico", "stats_historico"]
    for page in pages:
        response = test_client.post(page, data={"project_name": project})
        assert response.status_code == 200
