from datetime import datetime,timedelta


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
        week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        count=0
        for date in self.completed_dates:
            if date > week_ago:
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

    def get_streak(self):
        dates=[]
        for date in self.completed_dates:
            dates.append(date.strftime('%Y-%m-%d'))
            dates.sort(reverse=True)
            today = datetime.today().date
            if today in dates:
                first_day = today
            elif (today-timedelta(days=1)) in dates:
                first_day = today-timedelta(days=1)
            else:
                return 0
            streak=0
            day=first_day
            while day in dates:
                streak+=1
                day-=timedelta(days=1)
            return streak





