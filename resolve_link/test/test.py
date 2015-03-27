# Load in our dependencies
import unittest
from resolve_link import resolve_link


# Start our tests
class ResolveLinkTestCase(unittest.TestCase):
    def test_complete_url(self):
        """
        A complete HTTP URL to our target site when resolved
            points to the original URL
        """
        result = resolve_link('https://www.linkedin.com/in/toddwolfson', 'https://www.linkedin.com/')
        self.assertEqual(result, 'https://www.linkedin.com/in/toddwolfson')

    def test_no_protocol(self):
        """
        An HTTP URL without a protocol to our target site when resolved
            points to the original URL with a protocol
        """
        result = resolve_link('www.linkedin.com/in/toddwolfson', 'https://www.linkedin.com/')
        self.assertEqual(result, 'https://www.linkedin.com/in/toddwolfson')

    def test_path(self):
        """
        An HTTP URL with an unexpected path to our target site when resolved
            points to the original URL
        """
        result = resolve_link('https://www.linkedin.com/pub/toddwolfson/aa/bb/cc', 'https://www.linkedin.com/')
        self.assertEqual(result, 'https://www.linkedin.com/pub/toddwolfson/aa/bb/cc')

    def test_query_string(self):
        """
        An HTTP URL with a query string to our target site when resolved
            points to the original URL
        """
        result = resolve_link('https://www.linkedin.com/profile/view?id=87904336&trk=nav_responsive_tab_profile_pic',
                              'https://www.linkedin.com/')
        self.assertEqual(result,
                         'https://www.linkedin.com/profile/view?id=87904336&trk=nav_responsive_tab_profile_pic')

    def test_custom_site(self):
        """
        An HTTP URL to a custom site when resolved
            points to the original URL
        """
        result = resolve_link('http://underdog.io/', 'https://www.linkedin.com/')
        self.assertEqual(result, 'http://underdog.io/')

    def test_custom_no_pathname(self):
        """
        An HTTP URL without a pathname to a custom site when resolved
            points to the original URL with a pathname
        """
        result = resolve_link('http://underdog.io', 'https://www.linkedin.com/')
        self.assertEqual(result, 'http://underdog.io/')

    def test_custom_site_no_protocol(self):
        """
        An HTTP URL without a protocol to a custom site when resolved
            points to the original URL with a protocol and pathname
        """
        result = resolve_link('underdog.io', 'https://www.linkedin.com/')
        self.assertEqual(result, 'http://underdog.io/')

    def test_username(self):
        """
        A username to our target site when resolved
            points to the username on the target site
        """
        result = resolve_link('underdogio', 'https://github.com/')
        self.assertEqual(result, 'https://github.com/underdogio')
