class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, dx, dy):
        """Returns a new Position object moved by dx, dy."""
        return Position(self.x + dx, self.y + dy)

    def __repr__(self):
        return f'Position({self.x}, {self.y})'

    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class ChessPiece:
    VALID_COLORS = {'black', 'white'}

    def __init__(self, position, color):
        if not self.is_valid_position(position):
            raise ValueError('Invalid position')
        if color not in self.VALID_COLORS:
            raise ValueError('Invalid color')
        self._position = position
        self._color = color

    @property
    def position(self):
        return self._position

    @property
    def color(self):
        return self._color

    @staticmethod
    def is_valid_position(position):
        return 0 <= position.x < 8 and 0 <= position.y < 8

    def is_legal_move(self, new_position):
        raise NotImplementedError("Subclasses must implement is_legal_move")

    def move(self, new_position):
        if not self.is_legal_move(new_position):
            raise ValueError("Illegal move")
        self._position = new_position

class Pawn(ChessPiece):
    def is_legal_move(self, new_position):
        if not self.is_valid_position(new_position):
            return False
        direction = 1 if self.color == 'white' else -1
        return self.position.move(0, direction) == new_position

class King(ChessPiece):
    def is_legal_move(self, new_position):
        if not self.is_valid_position(new_position) or new_position == self.position:
            return False
        return abs(new_position.x - self.position.x) <= 1 and abs(new_position.y - self.position.y) <= 1
