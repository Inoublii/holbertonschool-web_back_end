#!/usr/bin/env python3
""" Test SUITE Unittest module Task """
import requests
from unittest import mock
import unittest
from parameterized import parameterized

from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method return output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''
            Tests access_nested_map for raised expections.
        '''
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
            Tests if get_json function returns the expected result.
        '''
        with mock.patch('utils.requests') as mock_request:
            mock_request.get.return_value = expected_result
            x = mock_request.get(url)
            self.assertEqual(expected_result, x)
