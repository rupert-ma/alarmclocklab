from alarm_clock import AlarmClock

alarm_clock_one = AlarmClock()

print(f'The current time is {alarm_clock_one.current_time}')
alarm_clock_one.change_current_time('4:00pm')
alarm_clock_one.set_alarm('8:00am')
alarm_clock_one.toggle_alarm()
