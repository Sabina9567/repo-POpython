salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Расчет общей суммы расходов за 10 месяцев (с учетом роста цен)
total_spend = 0
for i in range(months):
    if i == 0:
        total_spend += spend  # В первый месяц нет роста цен
    else:
        total_spend += spend * (1 + increase) ** i  # Расчет расходов с учетом роста цен

# Расчет общей суммы дохода за 10 месяцев
total_income = salary * months

# Расчет необходимой подушки безопасности
money_capital = total_spend - total_income

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")