import unittest
import os
from util.file_util import FileUtil

class TestFileUtil(unittest.TestCase):

    def test_project_root(self):
        expected = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.assertEqual(expected, FileUtil.PROJECT_ROOT)

    def test_(self):
        expected = '''<!DOCTYPE html><html lang="en"><head>
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

        self.assertEqual(expected, FileUtil.read_file(os.path.join(FileUtil.PROJECT_ROOT,"static", "index.html")))

    def test_read_csv(self):
        file_path = os.path.join(FileUtil.PROJECT_ROOT, 'test', 'resources', 'Summarys.csv')
        result = FileUtil.read_csv(file_path)
        self.assertIsNotNone(result)
        first_row = result[0]
        self.assertEqual("Sally", first_row['STUDENT_NAME'])


    def test_read_csv_line(self):
        file_path = os.path.join(FileUtil.PROJECT_ROOT, 'test', 'resources', 'Summarys.csv')
        result = FileUtil.read_csv_line(file_path, 'STUDENT_NAME', 'Sally')
        self.assertIsNotNone(result)
        self.assertEqual("Sally", result['STUDENT_NAME'])

if __name__ == "__main__":
    unittest.main()