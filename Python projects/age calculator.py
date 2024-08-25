from datetime import date

def age_calculate(birth_date):
    today=date.today()
    age=today.year-birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day))
    return  age
print(age_calculate(date(1990,3,5)))