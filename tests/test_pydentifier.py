import unittest

import pydentifier

class LowerUnderscoreTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pydentifier.lower_underscore('Admin interface', prefix=''),
            'admin_interface'
        )

    def test_with_prefix_and_suffix(self):
        self.assertEqual(
            pydentifier.lower_underscore('Admin interface', prefix='test', suffix='yeah!!!'),
            'test_admin_interface_yeah'
        )

    def test_acronym(self):
        self.assertEqual(
            pydentifier.lower_underscore('API access', prefix=''),
            'api_access'
        )

    def test_contraction(self):
        self.assertEqual(
            pydentifier.lower_underscore("I'm a function", prefix=''),
            'i_am_a_function'
        )

    def test_keyword(self):
        self.assertEqual(
            pydentifier.lower_underscore('yield', prefix=''),
            'yield_'
        )

    def test_invalid_name(self):
        with self.assertRaises(pydentifier.InvalidIdentifier):
            pydentifier.lower_underscore('123', prefix='')

class UpperUnderscoreTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pydentifier.upper_underscore('Admin interface', prefix=''),
            'ADMIN_INTERFACE'
        )

    def test_with_prefix_and_suffix(self):
        self.assertEqual(
            pydentifier.upper_underscore('Admin interface', prefix='test', suffix='yeah!!!'),
            'TEST_ADMIN_INTERFACE_YEAH'
        )

    def test_acronym(self):
        self.assertEqual(
            pydentifier.upper_underscore('API access', prefix=''),
            'API_ACCESS'
        )

    def test_contraction(self):
        self.assertEqual(
            pydentifier.upper_underscore("I'm a function", prefix=''),
            'I_AM_A_FUNCTION'
        )

    def test_keyword(self):
        self.assertEqual(
            pydentifier.upper_underscore('yield', prefix=''),
            'YIELD'
        )

    def test_invalid_name(self):
        with self.assertRaises(pydentifier.InvalidIdentifier):
            pydentifier.upper_underscore('123', prefix='')

class UpperCamelTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pydentifier.upper_camel('Admin interface', prefix=''),
            'AdminInterface'
        )

    def test_with_prefix_and_suffix(self):
        self.assertEqual(
            pydentifier.upper_camel('Admin interface', prefix='test', suffix='yeah!!!'),
            'TestAdminInterfaceYeah'
        )

    def test_acronym(self):
        self.assertEqual(
            pydentifier.upper_camel('API access', prefix=''),
            'APIAccess'
        )

    def test_contraction(self):
        self.assertEqual(
            pydentifier.upper_camel("I'm a class", prefix=''),
            'IAmAClass'
        )

    def test_invalid_name(self):
        with self.assertRaises(pydentifier.InvalidIdentifier):
            pydentifier.upper_camel('123', prefix='')

class LowerCamelTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            pydentifier.lower_camel('Admin interface', prefix=''),
            'adminInterface'
        )

    def test_with_prefix_and_suffix(self):
        self.assertEqual(
            pydentifier.lower_camel('Admin interface', prefix='test', suffix='yeah!!!'),
            'testAdminInterfaceYeah'
        )

    def test_acronym(self):
        self.assertEqual(
            pydentifier.lower_camel('API access', prefix=''),
            'apiAccess'
        )

    def test_contraction(self):
        self.assertEqual(
            pydentifier.lower_camel("I'm a class", prefix=''),
            'iAmAClass'
        )

    def test_invalid_name(self):
        with self.assertRaises(pydentifier.InvalidIdentifier):
            pydentifier.lower_camel('123', prefix='')
