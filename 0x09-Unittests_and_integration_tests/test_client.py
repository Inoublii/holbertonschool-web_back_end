#!/usr/bin/env python3
""" Unittest
"""

from unittest import TestCase, mock
from unittest.mock import patch, PropertyMock
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
        with patch(
             'client.GithubOrgClient.org', new_callable=PropertyMock) as mock:
            mock.return_value = {'repos_url': 'http://mock.url'}
            gc = GithubOrgClient('xyz')
            r = gc._public_repos_url
            self.assertEqual(r, 'test')

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test that the list of repos is what you expect from the chosen
            payload. the public repos
        """
        get_json_mock.return_value = [
            {'name': 'random_rep'},
            {'name': 'random-rep1'},

        ]
        get_json_mock()
        with patch(
            'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mocked_public_repos:
            mocked_public_repos.return_value = [
                {'name': 'rand'},
                {'name': 'rand1'},

            ]
            gc = GithubOrgClient('abc')
            r = gc._public_repos_url
            self.assertEqual(r, mocked_public_repos.return_value)
            mocked_public_repos.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
