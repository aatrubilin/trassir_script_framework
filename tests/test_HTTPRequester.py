import os
import sys

from unittest import TestCase

CWD = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CWD)

from trassir_script_framework import HTTPRequester


class TestHTTPRequester(TestCase):
    base_requests = HTTPRequester()

    def test_get(self):
        response = self.base_requests.get("http://httpbin.org/get")
        self.assertEqual(200, response.code)
        self.assertEqual("TrassirScript", response.json["headers"]["User-Agent"])

    def test_get_params(self):
        response = self.base_requests.get(
            "http://httpbin.org/get",
            params={"PARAMETER": "TEST"}
        )
        self.assertEqual(200, response.code)
        self.assertEqual("TEST", response.json["args"]["PARAMETER"])

    def test_get_headers(self):
        response = self.base_requests.get(
            "http://httpbin.org/get",
            headers={"Title": "TEST"}
        )
        self.assertEqual(200, response.code)
        self.assertEqual("TEST", response.json["headers"]["Title"])

    def test_post(self):
        response = self.base_requests.post("http://httpbin.org/post")
        self.assertEqual(200, response.code)
        self.assertEqual("TrassirScript", response.json["headers"]["User-Agent"])

    def test_post_data(self):
        response = self.base_requests.post(
            "http://httpbin.org/post",
            data={"PARAMETER": "TEST"}
        )
        self.assertEqual(200, response.code)
        self.assertEqual("TEST", response.json["form"]["PARAMETER"])

    def test_post_headers(self):
        response = self.base_requests.post(
            "http://httpbin.org/post",
            headers={"Title": "TEST"}
        )
        self.assertEqual(200, response.code)
        self.assertEqual("TEST", response.json["headers"]["Title"])
