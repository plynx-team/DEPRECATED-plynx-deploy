import cv2
import uuid

from typing import Any

import numpy as np
import plynx.base.resource
import plynx.plugins.resources.common


class NumpyArray(plynx.base.resource.BaseResource):
    @classmethod
    def preview(cls, preview_object):
        data = np.load(preview_object.fp)

        body = [
            'shape: {}'.format(data.shape),
            'dtype: {}'.format(data.dtype),
            '-' * 32,
            str(data)
        ]

        return '<pre>{}</pre>'.format('\n'.join(body))


class Image(plynx.plugins.resources.common.Image):
    """Image file"""
    DISPLAY_THUMBNAIL: bool = True

    @staticmethod
    def preprocess_input(value: Any) -> Any:
        """Resource_id to an object"""

        with plynx.utils.file_handler.open(value, "rb") as f:
            image = np.asarray(bytearray(f.read()), dtype="uint8")
            return cv2.imdecode(image, flags=cv2.IMREAD_UNCHANGED)

    @staticmethod
    def postprocess_output(value: Any) -> Any:
        """Object to resource id"""
        filename = str(uuid.uuid4())
        with plynx.utils.file_handler.open(filename, "wb") as f:
            f.write(cv2.imencode(ext=".png", img=value)[1].tobytes())
        return filename
