from datetime import date, timedelta, datetime

zero_date = date(2024,1,1)
today = date.today()
days = (date.today() - date(2024,1,1)).days

def time_limit(today, lt_date):
    if today.day - lt_date.day >=7:
        return f'Можешь пройти тест еще раз!\nКоличество дней с последнего прохождения: {today.day - lt_date.day}'
    else:
        return f'Ты не можешь пройти тест!\nКоличество дней с последнего прохождения: {today.day - lt_date.day}'

print(zero_date, today, days)