from nose.tools import assert_true
import requests

def test_request_response():
    # Send a request to the API server and store the response.
    response = requests.get('https://citymanagement.herokuapp.com/trafficdata')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)
def test_model(response):
    assert traffic_model(response) != None

