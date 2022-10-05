import os
import mimetypes
from werkzeug.utils import secure_filename


def save_file(f):

    # TODO: try catch for IO exceptions - which you could populate in an error

    f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        'static/sync', secure_filename(f.filename)))
    file_name = f.filename
    mime_tuple = mimetypes.guess_type(file_name)
    mime_type, mime_encoding = mime_tuple

    result = 0
    error = None

    return result, error, mime_type, file_name
