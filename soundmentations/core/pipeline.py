class Pipeline:
    def __init__(self, transformations):
        self.transformations = transformations

    def apply(self, data):
        for transformation in self.transformations:
            data = transformation(data)
        return data