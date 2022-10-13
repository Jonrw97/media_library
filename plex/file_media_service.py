import mimetypes
import os
from os import path
from werkzeug.utils import secure_filename


def save_file(f):

    # TODO: try catch for IO exceptions - which you could populate in an error
    try:
        f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'static/sync', secure_filename(f.filename)))
    except IOError:
        result = 1
        error = f"File:{file_name} can not be uploaded."
        file_name = f.filename
        mime_tuple = mimetypes.guess_type(file_name)
        mime_type, mime_encoding = mime_tuple

    else:
        file_name = f.filename
        mime_tuple = mimetypes.guess_type(file_name)
        mime_type, mime_encoding = mime_tuple
        result = 0
        error = None

    return result, error, mime_type, file_name
