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


