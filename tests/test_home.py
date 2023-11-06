def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"INFOCODES - Home Page | Orange" in response.data


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
