#!/usr/bin/dwyt

import os
import ssl
import unittest
import requests
import urllib.request
import certifi
from kivy.utils import platform


class TestApp(unittest.TestCase):
    
    URL = 'https://media.makeameme.org/created/its-working-oyy433.jpg'
    EXPECTED_STATUS = 200

    def test_requests(self):
        """
        The requests module handles certs seamlessly by default.
        """
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, self.EXPECTED_STATUS)

    @unittest.skipUnless(platform == 'android', 'requires Android')
    def test_urllib(self):
        """
        On Android urllib doesn't have certs by default and would crash unless
        explicitely loaded.
        """
        gfgf = os.environ.get('SSL_CERT_DIR')
        print(f"{gfgf}")
        self.assertIsNone(os.environ.get('SSL_CERT_DIR'))
        with self.assertRaises(urllib.error.URLError) as e:
            urllib.request.urlopen(self.URL)
        self.assertEqual(type(e.exception.args[0]), ssl.SSLCertVerificationError)
        os.environ['SSL_CERT_FILE'] = certifi.where()
        response = urllib.request.urlopen(self.URL)
        self.assertEqual(response.status, self.EXPECTED_STATUS)
