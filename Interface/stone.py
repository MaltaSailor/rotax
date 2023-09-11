class Stone:
    def __init__(self, color:Color, x:int, y:int)->None:
        """white->1, void->0, black->-1"""
        self.color = color
        self.position = [x, y]