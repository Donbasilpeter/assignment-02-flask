import pytest
from app import app

def test_home_route_invalid_method():
    # Create a test client
    client = app.test_client()
    
    # Simulate a POST request to the GET-only `/` route
    response = client.post('/')
    
    # Assert the response status code
    assert response.status_code == 405, "Expected status code 405 for invalid method"
