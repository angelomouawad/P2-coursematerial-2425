class Duration:
    def __init__(self, seconds: int):
        self._seconds = seconds
    
    @staticmethod
    def from_seconds(seconds: int):
        return Duration(seconds)
    
    @staticmethod
    def from_minutes(minutes: int):
        return Duration(minutes * 60)
    
    @staticmethod
    def from_hours(hours: int):
        return Duration(hours * 3600)
    
    @property
    def seconds(self):
        return self._seconds
    
    @property
    def minutes(self):
        return self._seconds // 60
    
    @property
    def hours(self):
        return self._seconds // 3600