from flask import url_for

# Python
class FlaskHelperUtil:

    def __init__(self, app=None):
        if app is not None:
            self.app = app
        else:
            from flask import current_app
            self.app = current_app

    def attach_scripts(self, value):
        value_replace_href = self._replace_with_url_for(value, 'href');

        value_replace_href_and_src = self._replace_with_url_for(value_replace_href, 'src');

        return value_replace_href_and_src

    def _replace_with_url_for(self, value, reg):
        key_half_of_entry = f'{reg}="'

        # Find href
        index_href = value.find(key_half_of_entry)

        # get only the value of the href
        while index_href != -1:
            index_start = index_href + len(key_half_of_entry)
            ref_str = self._retrieve_ref_str(value, index_start)

            # if the value is not a url_for replace the value with url_for
            if not ref_str == ('/'):
                value = value[:index_start] + self._retrieve_with_url_for(ref_str) + value[index_start + len(ref_str):]

            # Find next href
            index_href = value.find(key_half_of_entry, index_start)

        return value


    def _retrieve_with_url_for(self, ref_str):
        result = None

        with self.app.app_context():
             result = url_for('static', filename=ref_str)

        return result

    def _retrieve_ref_str(self, processer, index_start):
        index_end = self._retrieve_end_index(processer, index_start)

        return processer[index_start:index_end]

    def _retrieve_end_index(self, processer, index_start):
        return processer.find('"', index_start)