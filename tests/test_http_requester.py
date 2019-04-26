import os
import sys
CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CWD)

from trassir_script_framework import HTTPRequester


class TestHTTPRequester:
    base_requests = HTTPRequester()

    def test_get(self):
        response = self.base_requests.get("http://httpbin.org/get")
        assert response.code == 200
        assert response.json["headers"]["User-Agent"] == "TrassirScript"

    def test_get_params(self):
        response = self.base_requests.get(
            "http://httpbin.org/get",
            params={"PARAMETER": "TEST"}
        )
        assert response.code == 200
        assert response.json["args"]["PARAMETER"] == "TEST"

    def test_get_headers(self):
        response = self.base_requests.get(
            "http://httpbin.org/get",
            headers={"Title": "TEST"}
        )
        assert response.code == 200
        assert response.json["headers"]["Title"] == "TEST"

    def test_post(self):
        response = self.base_requests.post("http://httpbin.org/post")
        assert response.code == 200
        assert response.json["headers"]["User-Agent"] == "TrassirScript"

    def test_post_data(self):
        response = self.base_requests.post(
            "http://httpbin.org/post",
            data={"PARAMETER": "TEST"}
        )
        assert response.code == 200
        assert response.json["form"]["PARAMETER"] == "TEST"

    def test_post_headers(self):
        response = self.base_requests.post(
            "http://httpbin.org/post",
            headers={"Title": "TEST"}
        )
        assert response.code == 200
        assert response.json["headers"]["Title"] == "TEST"
