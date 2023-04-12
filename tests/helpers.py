class NonStringConvertible:
    def __str__(self):
        raise TypeError("Cannot convert NonStringConvertible to str")
