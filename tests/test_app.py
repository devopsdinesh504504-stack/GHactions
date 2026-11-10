from app import create_app


def test_homepage():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Welcome to DevOps CI/CD Project"


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "flask-devops-demo"


def test_api_info_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/info")

    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "Flask DevOps CI/CD Demo"
    assert data["version"] == "1.0.0"
    assert data["environment"] in {"development", "production"}
