#!/usr/bin/env python3

"""
Parameterize and patch as decorators:
Method tests that GithubOrgClient.org returns the correct value.
"""


import unittest
from unittest.mock import Mock, PropertyMock, call, patch

import requests
from parameterized import parameterized, parameterized_class

import client
import utils
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to parameterize and patch as decorators
    """

    @parameterized.expand([("google", {"google": True}), ("abc", {"abc": True})])
    @patch("client.get_json")
    def test_org(self, org, expected, get_patch):
        """
        Method tests that GithubOrgClient.org returns the correct value
        """

        get_patch.return_value = expected
        x = GithubOrgClient(org)
        self.assertEqual(x.org, expected)
        get_patch.assert_called_once_with("https://api.github.com/orgs/" + org)

    def test_public_repos_url(self):
        """
        Method tests that _public_repos_url works
        """

        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = "client.GithubOrgClient.org"
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        """
        Method tests the public repos
        """

        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}

        to_mock = "client.GithubOrgClient._public_repos_url"

        get_json_mock.return_value = [jeff, bobb, suee]

        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ["Jeff", "Bobb", "Suee"])
            self.assertEqual(x.public_repos("a"), ["Jeff"])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )

    def test_has_license(self, repo, license, expected):
        """
        Method tests the license checker
        """

        self.assertEqual(GithubOrgClient.has_license(
            repo, license), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos","apache2_repos"), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for github org client
    """

    @classmethod
    def setUpClass(cls):
        """
        Method for preparing testing
        """

        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch("requests.get")
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """
        Method to finish testing
        """

        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Method tests public repos
        """

        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.get.assert_has_calls(
            [call("https://api.github.com/orgs/x"), call(self.org_payload["repos_url"])]
        )

    def test_public_repos_with_license(self):
        """
        Method tests public repos
        """

        y = GithubOrgClient("x")
        self.assertEqual(y.org, self.org_payload)
        self.assertEqual(y.repos_payload, self.repos_payload)
        self.assertEqual(y.public_repos(), self.expected_repos)
        self.assertEqual(y.public_repos("NONEXISTENT"), [])
        self.assertEqual(y.public_repos("apache-2.0"), self.apache2_repos)
        self.get.assert_has_calls(
            [call("https://api.github.com/orgs/x"), call(self.org_payload["repos_url"])]
        )
