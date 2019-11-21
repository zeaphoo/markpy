
class Type(object):
    """
    The base class for all markpy types.
    """
    def __init__(self, value):
        self.value = value

    @property
    def type_name(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.type_name

    def __hash__(self):
        return hash(self.type_name)

    def __eq__(self, other):
        raise Exception('Subclass must implement eq function.')

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        raise Exception('Subclass must implement eq function.')

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return (not self.__lt__(other)) and (not self.__eq__(other))

    def __ge__(self, other):
        return not self.__lt__(other)
