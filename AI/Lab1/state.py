class State:
    shore = None
    boat = 0
    depth = 0
    path = None

    def __init__(self, shore=None, boat=0):
        if shore is None:
            shore = []
        self.shore = shore
        self.boat = boat
        self.depth = 0
        self.path = []
