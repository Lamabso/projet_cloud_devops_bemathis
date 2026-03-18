def _assert_health_payload(resp_json: dict):
    assert isinstance(resp_json, dict)
    assert "status" in resp_json
    assert isinstance(resp_json["status"], str)
    assert resp_json["status"] in ("ok test", "ready")


def test_healthz(client):
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.is_json
    _assert_health_payload(resp.get_json())


def test_readyz(client):
    resp = client.get("/readyz")
    assert resp.status_code == 200
    assert resp.is_json
    _assert_health_payload(resp.get_json())
