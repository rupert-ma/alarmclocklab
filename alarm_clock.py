
class AlarmClock:
    def __init__(self):
        self.current_time = '12:00pm'
        self.alarm_on = True
        self.alarm_set_to = '1:00pm'

    def change_current_time(self, new_time):
        self.current_time = new_time
        print(f'The new time is {self.current_time}')

    def toggle_alarm(self):
        if self.alarm_on == True:
            self.alarm_on = False
            print('Alarm is off')

        else:
            self.alarm_on = True
            print('Alarm is on')

    def set_alarm(self, alarm_time):
        self.alarm_set_to = alarm_time
        print(f'The alarm is set to {self.alarm_set_to}')

    
