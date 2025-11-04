from app import app  # importa tu Flask app

def test_home_route_return_200_OK():
    client = app.test_client()
    response = client.get("/health", follow_redirects=True)
    assert response.status_code == 200
    assert response.get_json() == {"detail": "ok"}

