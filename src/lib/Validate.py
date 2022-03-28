import datetime
regex = datetime.datetime.strptime

class Validate(object):
    """docstring for ClassName."""
    
    @staticmethod
    def validate_date(date: str) -> bool:
        assert regex(date, '%m/%d')
        return True
   