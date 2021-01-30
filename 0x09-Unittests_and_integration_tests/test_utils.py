#!/usr/bin/env python3
""" Test SUITE Unittest module Task """

import unittest
from parameterized import parameterized

from utils import access_nested_map, get_json
import requests
from unittest import mock


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    get_json tests.
    '''

    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, url, expected_result):
        '''
            Tests if get_json returns expected result.
        '''
        with mock.patch('utils.requests') as mock_request:
            mock_request.get.return_value = expected_result
            x = mock_request.get(url)
            self.assertEqual(expected_result, x)
