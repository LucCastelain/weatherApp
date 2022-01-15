import unittest
import app


class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def testRegisterSensor(self):
        response = self.client.post("/registerSensor")
        expected_resp = "Country name is required !"
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
        self.assertDictEqual(response.get_json(), expected_resp)

    def testRegisterSensor(self):
        response = self.client.post("/registerSensor?country=France")
        expected_resp = "City name is required !"
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
        self.assertDictEqual(response.get_json(), expected_resp)

    def testGetSensor(self):
        response = self.client.post("/getSensor?sensorsID=1")
        expected_resp = {"id": "1", "country": "France", "city": "Brest"}
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
        self.assertDictEqual(response.get_json(), expected_resp)


if __name__ == "__main__":
    unittest.main()