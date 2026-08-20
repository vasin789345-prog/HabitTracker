from datetime import datetime,timedelta
import json


class Habit:
    def __init__(self, name,description,goal_per_week=7):
        self.name = name
        self.description = description
        self.goal_per_week = goal_per_week
        self.completed_dates = []
    def complete(self, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        if date in self.completed_dates:
            print('Уже отмечено')
        else:
            self.completed_dates.append(date)
            print('Отмечено')
    def get_completed_this_week(self):
        today = datetime.now()
        week_ago = today - timedelta(days=7)
        count=0
        for date_str in self.completed_dates:
            date_obj = datetime.strptime(date_str,'%Y-%m-%d')
            if  week_ago<=date_obj<=today:
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

    def get_streak(self) -> int:
        if not self.completed_dates:
            return 0
        today_str = datetime.now().strftime("%Y-%m-%d")
        yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        if today_str in self.completed_dates:
            current_day_str = today_str
        elif yesterday_str in self.completed_dates:
            current_day_str = yesterday_str
        else:
            return 0
        streak = 0
        while current_day_str in self.completed_dates:
            streak += 1
            current_date = datetime.strptime(current_day_str, "%Y-%m-%d")
            current_date -= timedelta(days=1)
            current_day_str = current_date.strftime("%Y-%m-%d")
        return streak
    def to_dict(self):
        return {'name':self.name,'description':self.description,'goal_per_week':self.goal_per_week,'completed_dates':self.completed_dates}
    def info(self):
        completed=self.get_completed_this_week()
        streak=self.get_streak()
        progress=self.get_progress()
        print(self.name)
        if self.description:
            print(f'описание: {self.description}')
            print(f'выполнено:{completed} из {self.goal_per_week}')
            print(f'процент выполнентие: {progress}%')
            print(f'серия: {streak} ')
            if self.is_goal_achieved():
                print('Цель достигнута')
            else:
                print('Цель не достигнута')

class HabitTracker:
    def __init__(self,username):
        self.username = username
        self.habits = []
    def add_habit(self,habit):
        self.habits.append(habit)
        print('привычка добавлена')
    def remove_habit(self,name):
        for habit in self.habits:
            if habit.name == name:
                self.habits.remove(habit)
                print('привычка удалена')
                return
            print('привычка не найдена')
    def get_habit(self,name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None
    def show_all(self):
        for habit in self.habits:
            print(habit.name)
    def show_today(self):
        a=[]
        today = datetime.now().strftime('%Y-%m-%d')
        for habit in self.habits:
            if today not in habit.completed_dates:
                a.append(habit.name)
        if not a:
            print('сегодня выполнены все привычки')
            return
        print(f'Привычки котрые сегодня не выполнили ({today})')
        for habit in a:
            print(habit.name)
    def  weekly_report(self):
        print('НЕДЕЛЬНЫЙ ОТЧЕТ')
        for habit in self.habits:
            habit.info()
            print()
    def save_to_file(self,filename):
        data={'username':self.username,'habits':[habit.to_dict() for habit in self.habits]}
        with open(filename,'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
            print('данные сохранены')
    def load_from_file(self,filename):
        with open(filename,'r',encoding='utf-8') as f:
            data = json.load(f)
        self.username=data['username']
        self.habits=[]
        for habit_data in data['habits']:
            habit=Habit(name=habit_data['name'],description=habit_data.get('description'),goal_per_week=habit_data.get('goal_per_week',7))
            habit.completed_dates=habit_data.get('completed_dates',[])
            self.habits.append(habit)
        print('Данные загружены')

# Создаём трекер
tracker = HabitTracker("Алексей")

# Создаём привычки
h1 = Habit("Пить воду", "2 литра в день", 7)
h2 = Habit("Зарядка", "15 минут утром", 5)
h3 = Habit("Чтение", "30 минут", 3)

# Добавляем в трекер
tracker.add_habit(h1)
tracker.add_habit(h2)
tracker.add_habit(h3)

# Отмечаем выполнение
h1.complete()
h1.complete()  # Выведет "Уже отмечено!"
h2.complete()
h3.complete()

# Показываем отчёт
tracker.weekly_report()

# Сохраняем
tracker.save_to_file("habits.json")

# Загружаем в новый трекер
new_tracker = HabitTracker("Алексей")
new_tracker.load_from_file("habits.json")
new_tracker.show_all()



