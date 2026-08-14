from datetime import date,datetime,timedelta


class Habit:
    def __init__(self, name,description,goal_per_week=7):
        self.name = name
        self.description = description
        self.goal_per_week = goal_per_week
        self.completed_dates = []
    def complete(self, date=None):
        if date is None:
            date = date.today()
        if date in self.completed_dates:
            print('Уже отмечено!')
        else:
            self.completed_dates.append(date)
            print('Отмечено!')
    def get_completed_this_week(self):
        today = datetime.now()
        seven_days_ago = today - timedelta(days=7)
        count=0
        for date in self.completed_dates:
            if date > seven_days_ago:
                count += 1
        return count
    def get_progress(self):
        completed=self.get_completed_this_week()
        progress=(completed/self.goal_per_week)*100
        return progress
    def is_goal_achieved(self):
        completed = self.get_completed_this_week()
        if completed >= self.goal_per_week:
            return True
        else:
            return False




