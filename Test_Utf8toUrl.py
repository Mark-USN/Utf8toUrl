import unittest
import subprocess

from Utf8toUrl import utf8_to_url_encoding

class TestUtf8toUrl(unittest.TestCase):

    help_text = """usage: Utf8toUrl.py [-h] [--include-quotes] [--include INCLUDE] [text]

Convert UTF-8 text to URL encoding with optional filtering.

positional arguments:
  text               The text to convert (or leave empty to read from stdin)

options:
  -h, --help         show this help message and exit
  --include-quotes   Always encode quotes as %22 or %27
  --include INCLUDE  Regex pattern to determine which characters should be
                     URL-encoded
"""

    def test_no_args(self):
        """Should print out the help and exit with an error (1)."""
        result = subprocess.run(
            ["python3", "Utf8toUrl.py"],
            capture_output=True,
            text=True
        )

        # Verify the help message
        self.assertMultiLineEqual(result.stdout, self.help_text)

        # Verify the script exits with status code 1
        self.assertEqual(result.returncode, 1)
 
    def test_dash_h(self):
        """Should print out the help and exit."""
        result = subprocess.run(
            ["python3", "Utf8toUrl.py", "-h"],
            capture_output=True,
            text=True
        )

        # Verify the help message
        self.assertMultiLineEqual(result.stdout, self.help_text)

    def test_dash_dash_help(self):
        """Should print out the help and exit."""
        result = subprocess.run(
            ["python3", "Utf8toUrl.py", "--help"],
            capture_output=True,
            text=True
        )

        # Verify the help message
        self.assertMultiLineEqual(result.stdout, self.help_text)

    def test_basic_encoding(self):
        """All characters should be encoded if no regex is provided."""
        self.assertEqual(utf8_to_url_encoding("Hello"), "%48%65%6c%6c%6f")

    def test_multibyte_character(self):
        """Multibyte characters should be encoded properly."""
        self.assertEqual(utf8_to_url_encoding("✨"), "%e2%9c%a8")  # Unicode star

    def test_include_regex(self):
        """Only characters matching the regex should be encoded."""
        self.assertEqual(utf8_to_url_encoding("Hello 123!", include_pattern="[A-Za-z]"), "%48%65%6c%6c%6f 123!")

    def test_include_quotes(self):
        """Quotes should be encoded if add_quotes=True."""
        self.assertEqual(utf8_to_url_encoding('"Hello!"', add_quotes=True), '"%22%48%65%6c%6c%6f%21%22"')

    def test_include_numbers(self):
        """Only numbers should be encoded when regex includes digits."""
        r"""✅ FIXED: Now using raw string r"\d" (treat as raw string) to correctly match digits"""
        self.assertEqual(utf8_to_url_encoding("Test 123", include_pattern=r"\d"), "Test %31%32%33")

    def test_no_encoding(self):
        """If a non-matching regex is provided, nothing should be encoded."""
        self.assertEqual(utf8_to_url_encoding("Hello 123!", include_pattern="None"), "Hello 123!")

    def test_empty_string(self):
        """Empty input should return an empty string."""
        self.assertEqual(utf8_to_url_encoding(""), "")

    def test_spaces(self):
        """Spaces should be encoded if no regex is provided."""
        self.assertEqual(utf8_to_url_encoding("Hello World"), "%48%65%6c%6c%6f%20%57%6f%72%6c%64")  # Space → %20

    def test_special_characters(self):
        """Special characters should be fully encoded if no regex is specified."""
        self.assertEqual(utf8_to_url_encoding("Hello!@#"), "%48%65%6c%6c%6f%21%40%23")

if __name__ == '__main__':
    unittest.main()
