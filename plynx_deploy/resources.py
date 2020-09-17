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
