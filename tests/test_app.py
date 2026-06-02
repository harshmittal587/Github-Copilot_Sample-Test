def test_get_activities_returns_chess_club(client):
    # Arrange
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_new_participant(client):
    # Arrange
    email = "newstudent@mergington.edu"
    # Act
    response = client.post("/activities/Chess Club/signup", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}


def test_duplicate_signup_returns_400(client):
    # Arrange
    email = "michael@mergington.edu"
    # Act
    response = client.post("/activities/Chess Club/signup", params={"email": email})
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_missing_activity_returns_404(client):
    # Arrange
    email = "test@mergington.edu"
    # Act
    response = client.post("/activities/Nonexistent/signup", params={"email": email})
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_delete_participant_success(client):
    # Arrange
    email = "daniel@mergington.edu"
    # Act
    response = client.delete("/activities/Chess Club/participants", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Chess Club"}


def test_delete_missing_participant_returns_404(client):
    # Arrange
    email = "missing@mergington.edu"
    # Act
    response = client.delete("/activities/Chess Club/participants", params={"email": email})
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
