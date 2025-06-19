import unittest
from util.flask_helper_util import FlaskHelperUtil

# Figure out how to test FlaskHelperUtil... mock Flask app context?
class TestFlaskHelperUtil(unittest.TestCase):
    def setUp(self):
        self.s = FlaskHelperUtil()

    def test_(self):
        expected = '''<!DOCTYPE html><html lang="en"><head>
  <meta charset="utf-8">
  <title>WriteClientReport</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="{{ url_for(\'static\', filename=\'favicon.ico\') }}">
<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'styles.57c1da058d5340ca783e.css\') }}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{{ url_for(\'static\', filename=\'styles.57c1da058d5340ca783e.css\') }}"></noscript></head>
<body>
  <app-root></app-root>
<script src="{{ url_for(\'static\', filename=\'runtime.09cac5369e3ff4c930c4.js\') }}" defer></script><script src="{{ url_for(\'static\', filename=\'polyfills.1a98c15bd43985bd49c2.js\') }}" defer></script><script src="{{ url_for(\'static\', filename=\'main.8005ce815db643b0d879.js\') }}" defer></script>

</body></html>'''

        input = '''<!DOCTYPE html><html lang="en"><head>
  <meta charset="utf-8">
  <title>WriteClientReport</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="stylesheet" href="styles.57c1da058d5340ca783e.css" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="styles.57c1da058d5340ca783e.css"></noscript></head>
<body>
  <app-root></app-root>
<script src="runtime.09cac5369e3ff4c930c4.js" defer></script><script src="polyfills.1a98c15bd43985bd49c2.js" defer></script><script src="main.8005ce815db643b0d879.js" defer></script>

</body></html>'''

        self.assertEqual(expected, self.s.attach_scripts(input))

if __name__ == "__main__":
    unittest.main()