import unittest
from datetime import datetime
from unittest.mock import patch

from src.main import app
from src.models.model import db_session


class TestRoutesOperations(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.tester.post("/routes/reset")

    def tearDown(self):
        db_session.remove()

    @patch('src.blueprints.operations')
    def test_create_route_token_vacio(self, mocked):
        tester = app.test_client(self)
        response = tester.post("/routes", json={
            'flightId': '1',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': '2024-10-06T21:20:53.214Z',
            'plannedEndDate': '2024-10-06T21:20:53.214Z'
        })
        statuscode = response.status_code
        self.assertEqual(statuscode, 403)

    @patch('src.blueprints.operations.requests.get')
    def test_create_route_missing_fligthtid_parameter(self,mocked):
        mocked.return_value.status_code = 200
        tester=app.test_client(self)
        response = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': '2024-01-01',
            'plannedEndDate': '2024-01-01'
        })
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    @patch('src.blueprints.operations.requests.get')
    def test_create_route_invalid_date(self,mocked):
        mocked.return_value.status_code = 200
        tester=app.test_client(self)
        response = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'flightId': '2',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': '2024-10-06T21:20:53.214Z',
            'plannedEndDate': '2023-10-06T21:20:53.214Z'
        })
        statuscode = response.status_code
        self.assertEqual(statuscode, 412)

    @patch('src.blueprints.operations.requests.get')
    def test_create_route_invalid_date2(self,mocked):
        mocked.return_value.status_code = 200
        tester=app.test_client(self)
        response = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'flightId': '3',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': '2024-10-06T21:20:53.214Z',
            'plannedEndDate': '2000-30'
        })
        statuscode = response.status_code
        self.assertEqual(statuscode, 412)


    @patch('src.blueprints.operations.requests.get')
    def test_create_route_existing_flight(self,mocked):
        mocked.return_value.status_code = 200
        tester=app.test_client(self)
        response1 = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'flightId': '4',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': '2024-10-06T21:20:53.214Z',
            'plannedEndDate': '2024-10-06T21:20:53.214Z'
        })
        response2 = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'flightId': '4',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': '2024-10-06T21:20:53.214Z',
            'plannedEndDate': '2024-10-06T21:20:53.214Z'
        })
        print(response1.status_code)
        statuscode1 = response1.status_code
        statuscode2 = response2.status_code
        self.assertEqual(statuscode1, 201)
        self.assertEqual(statuscode2, 412)

    @patch('src.blueprints.operations.requests.get')
    def test_filter_route(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.get("/routes",headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    @patch('src.blueprints.operations.requests.get')
    def test_filter_route_filter_with_flight(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.get("/routes?flight=1234",headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
 
    @patch('src.blueprints.operations.requests.get')
    def test_create_route_token_valido(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.post("/routes", headers={"Authorization": "FAKE_TOKEN"}, json={
            'flightId': 'test',
            'sourceAirportCode': 'test',
            'sourceCountry': 'test',
            'destinyAirportCode': 'test',
            'destinyCountry': 'test',
            'bagCost': 123,
            'plannedStartDate': '2023-10-06T21:20:53.214Z',
            'plannedEndDate': '2024-10-06T21:20:53.214Z'
        })
        statuscode = response.status_code
        self.assertEqual(statuscode, 201)
    
    @patch('src.blueprints.operations.requests.get')
    def test_create_route_token_validos(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.post("/routes", headers={"Authorization": "FAKE_TOKEN"}, json={
            'flightId': 'test1',
            'sourceAirportCode': 'test',
            'sourceCountry': 'test',
            'destinyAirportCode': 'test',
            'destinyCountry': 'test',
            'bagCost': "ss",
            'plannedStartDate': '2024-10-06T21:20:53.214Z',
            'plannedEndDate': '2024-10-06T21:20:53.214Z'
        })
        statuscode = response.status_code
        self.assertEqual(statuscode, 500)

    @patch('src.blueprints.operations.requests.get')
    def test_consult_route_invalid_uuid(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.get("/routes/123",headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    @patch('src.blueprints.operations.requests.get')
    def test_consult_route_not_exists(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.get("/routes/9d10b18e-9611-49fb-8fd1-4d00e4e32300",headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)
   
    @patch('src.blueprints.operations.requests.get')
    def test_consult_route(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)

        response_create = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'flightId': '5',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': "2024-10-06T21:20:53.214Z",
            'plannedEndDate': "2024-11-06T21:20:53.214Z"
        })
        response = tester.get(f"/routes/{response_create.json['id']}",headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    @patch('src.blueprints.operations.requests.get')
    def test_delete_route_invalid_uuid(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.delete("/routes/123", headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    
    @patch('src.blueprints.operations.requests.get')
    def test_delete_route_not_exists(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response = tester.delete("/routes/9d10b18e-9611-49fb-8fd1-4d00e4e32300", headers={"Authorization": "FAKE_TOKEN"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)
    
    @patch('src.blueprints.operations.requests.get')
    def test_delete_route(self, mocked):
        mocked.return_value.status_code = 200
        tester = app.test_client(self)
        response_create = tester.post("/routes", headers={"Authorization": 'FAKE_TOKEN'}, json={
            'flightId': '4',
            'sourceAirportCode': 'MX01',
            'sourceCountry': 'MEXICO',
            'destinyAirportCode': 'CO01',
            'destinyCountry': 'COLOMBIA',
            'bagCost': 1234.56,
            'plannedStartDate': "2024-10-06T21:20:53.214Z",
            'plannedEndDate': "2024-11-06T21:20:53.214Z"
        })
        response = tester.delete(f"/routes/{response_create.json['id']}", headers={"Authorization": 23})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    @patch('src.blueprints.operations.requests.get')
    def test_check_health_api_route(self, mocked):
        tester = app.test_client(self)
        response = tester.get("/routes/ping")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    @patch('src.blueprints.operations.requests.get')
    def test_reset_db(self, mocked):
        tester = app.test_client(self)
        response = tester.post("/routes/reset")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    @patch('src.blueprints.operations')
    def test_api_not_found(self, mocked):
        tester = app.test_client(self)
        response = tester.post("/routess")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    if __name__ == '__main__':
        unittest.main()
