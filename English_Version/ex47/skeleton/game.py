class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = []
        
    def go(self, direction):
        return self.paths.get(directiion, None)
        
    def add_path(self, path):
        self.path.update(paths)
