import requests


def test_nasa_mars_rover_photos_api():
    """
    Test NASA Mars Rover Photos public API.
    Validates response status and basic response structure.
    """

    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": 1000,
        "camera": "fhaz",
        "api_key": "DEMO_KEY"
    }

    response = requests.get(url, params=params)

    # Status code validation
    assert response.status_code == 200, "Expected status code 200"

    data = response.json()

    # Response structure validation
    assert "photos" in data, "Response does not contain 'photos' field"
    assert isinstance(data["photos"], list), "'photos' is not a list"

    # Optional: check first photo fields if photos exist
    if len(data["photos"]) > 0:
        photo = data["photos"][0]
        assert "img_src" in photo
        assert "id" in photo
        assert "earth_date" in photo
