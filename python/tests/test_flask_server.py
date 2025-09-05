import unittest
import requests
import multiprocessing
import time

from open_mic_backend.app import App


def run_server():
    app = App()
    app.start()


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = multiprocessing.Process(target=run_server)
        cls.server_process.start()
        time.sleep(1)  # wait for server to start
        cls.base_url = "http://127.0.0.1:8080"

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.join()

    def test_post_request(self):
        payload = {"email": "bob@test.com"}
        response = requests.post(f"{self.base_url}/login", json=payload)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
