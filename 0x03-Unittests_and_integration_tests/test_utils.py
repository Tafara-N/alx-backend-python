#!/usr/bin/env python3

"""
Test SUITE Unittest module Task """

from unittest import TestCase, mock
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """
    Class to parameterize a unit test
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, map, path, expected_output):
        """
        Method to test that the method returns what it is supposed to
        """

        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """
        Method raises correct exceptions
        """

        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """
    Class for testing get_json function
    """

    # order of args: test_url, test_payload
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """
        Method to test if the function returns correct output
        """

        # Setting mock response to have return value of test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Function calls requests.get, need patch to get mock return value
        with patch("requests.get", return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)

            # Checking if the mocked method is called once per input
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """
    Class tests for memoization
    """

    def test_memoize(self):
        """
        Method tests memoize function
        """

        class TestClass:
            """
            Inner test class
            """

            def a_method(self):
                """
                Method MUST ALWAYS return 42
                """

                return 42

            @memoize
            def a_property(self):
                """
                Method returns memoized property
                """

                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
