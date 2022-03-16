import datetime

user_input = input('Enter your goal and deadline separated by colon\n')
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, '%d.%m.%Y')
today_date = datetime.datetime.today()

remaining_days = deadline_date - today_date
remaining_hours = remaining_days.total_seconds() / 60 / 60

print(f'Dear user! Time remaining for your goal: {goal} is {remaining_days.days} days and {int(remaining_hours)} hours')






# learn python:10.05.2022