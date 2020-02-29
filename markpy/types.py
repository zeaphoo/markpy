
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

class Boolean(Type):
    def __init__(self, value = False):
        super(Boolean, self).__init__(value)
        self.value = value

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        return self.value == other.value


boolean = bool_ = Boolean

class Integer(Type):
    _bits = 32
    _unsigned = False

    @property
    def signed(self):
        return not self._unsigned

    @property
    def bitwidth(self):
        return self._bits

    def __init__(self, value = 0):
        if value > self.maxval or value < self.minval:
            raise ValueError("value {} not in valid range [{}, {}]".format(value, self.minval, self.maxval))
        super(Integer, self).__init__(value)
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Integer):
            other_value = other.value
        elif isinstance(other, int):
            other_value = other
        elif type(self) != type(other):
            return NotImplemented
        return self.value == other_value

    def __lt__(self, other):
        if isinstance(other, Integer):
            other_value = other.value
        elif isinstance(other, int):
            other_value = other
        elif type(self) != type(other):
            return NotImplemented
        return self.value < other_value

    def __add__(self, other):
        if isinstance(other, int):
            other_value = other
        elif isinstance(other, Integer):
            other_value = other.value
        else:
            raise ValueError('only int or Integer can be added.')
        return Integer(self.value + other_value)

    def __str__(self):
        return "<{}:{}>".format(type(self).__name__, self.value)

    @property
    def maxval(self):
        """
        The maximum value representable by this type.
        """
        if self.signed:
            return (1 << (self.bitwidth - 1)) - 1
        else:
            return (1 << self.bitwidth) - 1

    @property
    def minval(self):
        """
        The minimal value representable by this type.
        """
        if self.signed:
            return -(1 << (self.bitwidth - 1))
        else:
            return 0

class Integer8(Integer):
    _bits = 8
    _unsigned = False

class UnsignedInteger8(Integer):
    _bits = 8
    _unsigned = True

int8 = Integer8
uint8 = UnsignedInteger8

class Integer16(Integer):
    _bits = 16
    _unsigned = False

class UnsignedInteger16(Integer):
    _bits = 16
    _unsigned = True

int16 = Integer16
uint16 = UnsignedInteger16

class Integer32(Integer):
    _bits = 32
    _unsigned = False

class UnsignedInteger32(Integer):
    _bits = 32
    _unsigned = True

int32 = Integer32
uint32 = UnsignedInteger32

class Integer64(Integer):
    _bits = 64
    _unsigned = False

class UnsignedInteger64(Integer):
    _bits = 64
    _unsigned = True

int64 = Integer64
uint64 = UnsignedInteger64


class Float(Type):
    _bits = 32
    def __init__(self, value = 0.0):
        super(Float, self).__init__(value)
        self.value = value

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        return self.value < other.value


class Float32(Float):
    _bits = 32

class Float64(Float):
    _bits = 64

float32 = float_ = Float32
float64 = double_ = Float64
