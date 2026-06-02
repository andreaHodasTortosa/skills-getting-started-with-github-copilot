def test_signup_then_unregister_workflow(client):
    activity_name = "Art Club"
    email = "workflow.student@mergington.edu"

    signup_response = client.post(
        f"/activities/{activity_name}/signup", params={"email": email}
    )
    assert signup_response.status_code == 200

    activities_after_signup = client.get("/activities").json()
    assert email in activities_after_signup[activity_name]["participants"]

    unregister_response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )
    assert unregister_response.status_code == 200

    activities_after_unregister = client.get("/activities").json()
    assert email not in activities_after_unregister[activity_name]["participants"]
