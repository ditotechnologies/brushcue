from brushcue import Bool, Float, Int


def setup_operators():
    Float.__add__ = Float.add
    Float.__radd__ = lambda self, other: Float.add(other, self)
    Float.__sub__ = Float.subtract
    Float.__rsub__ = lambda self, other: Float.subtract(other, self)
    Float.__mul__ = Float.multiply
    Float.__rmul__ = lambda self, other: Float.multiply(other, self)
    Float.__truediv__ = Float.divide
    Float.__rtruediv__ = lambda self, other: Float.divide(other, self)
    Float.__gt__ = Float.greater_than
    Float.__ge__ = Float.greater_than_or_equal
    Float.__lt__ = Float.less_than
    Float.__le__ = Float.less_than_or_equal
    Float.__eq__ = Float.equals

    Int.__add__ = Int.add
    Int.__radd__ = lambda self, other: Int.add(other, self)
    Int.__sub__ = Int.subtract
    Int.__rsub__ = lambda self, other: Int.subtract(other, self)
    Int.__mul__ = Int.multiply
    Int.__rmul__ = lambda self, other: Int.multiply(other, self)
    Int.__gt__ = Int.greater_than
    Int.__ge__ = Int.greater_than_or_equal
    Int.__lt__ = Int.less_than
    Int.__le__ = Int.less_than_or_equal
    Int.__eq__ = Int.equals

    Bool.__and__ = Bool.and_
    Bool.__rand__ = lambda self, other: Bool.and_(other, self)
    Bool.__or__ = Bool.or_
    Bool.__ror__ = lambda self, other: Bool.or_(other, self)
    Bool.__xor__ = Bool.xor
    Bool.__rxor__ = lambda self, other: Bool.xor(other, self)
    Bool.__invert__ = Bool.not_
