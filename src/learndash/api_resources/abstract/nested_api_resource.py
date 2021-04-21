from learndash.api_resources.abstract.api_resource import APIResource


class NestedAPIResource(APIResource):

    def __init__(self, id=None, **kwargs):
        super().__init__(id)
        self.parent = kwargs.get('parent', None)

    def class_url(self):
        base = self.parent.instance_url()
        if not self.api_path:
            raise Exception('No api path defined.')
        return f'{base}/{self.api_path}'

    def instance_url(self):
        id = self.id
        if not isinstance(id, int):
            raise Exception(f'Could not determine URL, received an invalid id "{id}".')

        base = self.class_url()
        return f'{base}/{id}'
