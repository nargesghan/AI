class Clock:
    def __init__(self, hour, minute):
        self.hour  = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        return f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}'
      
   

    def __eq__(self, other):
        if self.hour==other.hour:
            if self.minute==other.minute:
                return True
        else:
            return False

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
       return Clock(self.hour, self.minute - minutes)
        
