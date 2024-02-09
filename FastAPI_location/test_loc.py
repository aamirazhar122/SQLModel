from fastapi.testclient import TestClient 
from database import Location


# client = TestClient(app)
# test end point "location/{name}"
def get_test_location(self):
        res = client.get("location/zia")
        assert res.status_code == 200
        assert res.json() == {"name" : "zia", "location" : "Karachi"}

# # test end point "location/{name}" with a name not exist
# def get_test_location_not_found():
#     res = Location.get("location/aamir") 
#     assert res.status_code == 404
#     assert res.json() == {"details" : "Location not found"}      
# # test end point "location/{name}" with returns all name
# def get_test_location_all():
#     res = Location.get("location/")
#     assert res.status_code == 200
#     assert res.json() == [
#         {"name" : "zia", "location" : "Karachi"},
#         {"name" : "ali", "location" : "Lahore"},
#         {"name" : "ali", "location" : "Lahore"},
#         {"name" : "ali", "location" : "Lahore"},
#         ]

# # test end point "location/{name}" with invalid name 
# def get_test_location_invalid_name():
#     res = Location.get("location/123")
#     assert res.status_code == 200
#     assert res.json() == {"details":"Invalid name"}