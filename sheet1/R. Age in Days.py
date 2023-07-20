days = int(input())

per_years = int(days / 365) # 2
days_consumed = per_years * 365
days_left = days - days_consumed
per_months = int(days_left / 30) # 2
days_consumed = per_months * 30
per_days = days_left - days_consumed

print(per_years,"years")
print(per_months, "months")
print(per_days, "days")

