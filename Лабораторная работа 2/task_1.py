money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

mounth = 1
money_capital += salary - spend

while money_capital > 0:
     spend += spend * increase
     money_capital += salary - spend
     if  money_capital < 0:
         break
     mounth += 1
print("Количество месяцев, которое можно протянуть без долгов:", mounth)
