from app import app, add
def test_add(): assert add(2, 3) == 5
def test_home():
    r = app.test_client().get("/"); assert r.status_code == 200 and r.json["sum"] == 5
