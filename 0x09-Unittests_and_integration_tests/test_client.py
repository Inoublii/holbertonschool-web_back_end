#!/usr/bin/env python3
""" Unittest
"""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Class for testing """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ returns correct output """
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )


    def test_public_repos_url(self):
        """ Tests if GithubOrgClient._public_repos_url result is correct """
        with patch('client.GithubOrgClient.org',
             new_callable=PropertyMock) as mock:
            mock.return_value = {'repos_url': 'http://mock.url'}
            gc = GithubOrgClient('xyz')
            r = gc._public_repos_url
            self.assertEqual(r, 'test')
