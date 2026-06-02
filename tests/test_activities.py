def test_get_activities_returns_all_activities(client, baseline_activities):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == len(baseline_activities)


def test_get_activities_items_have_required_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    for details in activities.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
