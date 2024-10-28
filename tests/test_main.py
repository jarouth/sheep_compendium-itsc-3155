from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }


def test_add_sheep():
    # Prepare the new sheep data in a dictionary format
    new_sheep_data = {
        "id": 10,
        "name": "suffolk",
        "breed": "Merino",
        "sex": "ram"
    }
    response = client.post("/sheep/", json=new_sheep_data)
    assert response.status_code == 201
    
    assert response.json() == new_sheep_data
    new_sheep = client.get(f"/sheep/{new_sheep_data['id']}")
    assert new_sheep.status_code == 200

def test_delete_sheep():
    sheep_to_delete = {
        "id": 11,
        "name": "F1",
        "breed": "Merino",
        "sex": "ewe"
    }
    response = client.post("/sheep/", json=sheep_to_delete)
    assert response.status_code == 201
    
    assert response.json() == sheep_to_delete
    new_sheep = client.delete(f"/sheep/{sheep_to_delete['id']}")
    assert new_sheep.status_code == 204
    
    get_response = client.delete(f"/sheep/{sheep_to_delete['id']}")
    assert get_response.status_code == 404