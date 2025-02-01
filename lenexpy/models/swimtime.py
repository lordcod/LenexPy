class SwimTime:
    def __init__(self, hour: int, minute: int, second: int, hsec: int):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.hsec = hsec

    def __str__(self):
        return "%02d:%02d:%02d.%02d" % self.hour, self.minute, self.second, self.hsec

    def as_duration(self):
        return self.hour*60*60 + self.minute*60 + self.second + self.hsec / 100
