from validator.rules_src import Rule


class Hex(Rule):
    """
    The field under validation must be a hexadecimal number

    Examples:
    >>> from validator import validate

    >>> reqs = {"date" : "A1B2c3"}
    >>> rule = {"date" : "hex"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "0xA1b2C3"}
    >>> rule = {"date" : "hex"}
    >>> validate(reqs, rule)
    True

    >>> reqs = {"date" : "abcdefgh"}
    >>> rule = {"date" : "hex"}
    >>> validate(reqs, rule)
    False
    """

    def __init__(self):
        Rule.__init__(self)

    def check(self, arg):
        # Try to convert it to the hex.
        try:
            _ = int(arg, 16)
            return True
        except:
            # if transfered to exception we know its not hex.
            self.set_errror_message(
                f"Expected String to be in Hexadecimal format, Got: {arg}"
            )
            return False

    def __from_str__(self):
        pass
