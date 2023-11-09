import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl
from scipy.stats import pearsonr, ttest_ind

data = pd.read_csv('./Russia-Covid19-v2.csv', nrows=100)

st1 = data['new infections']
st2 = data['sick now']
st3 = []
for i in range(len(st2)):
    st3.append((st1[i]+st2[i])/2)
    print(st1[i], st2[i], (st1[i]+st2[i])/2, st3[i])

# Создание графика
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика

# График с линиями (например, для временных рядов)
plt.plot(st1, label='new infections', linestyle='-', marker='o')
plt.plot(st2, label='sick now', linestyle='--', marker='x')
plt.plot(st3, label='medium shedding', linestyle='--', marker='x')



# Добавление подписей к осям и заголовка
plt.xlabel('Дни')
plt.ylabel('Количество человек')
plt.title('График всего инфецированных/смерти')

# Добавление легенды
plt.legend()

# Отображение графика
plt.grid(True)
plt.show()

# Коэффициент корреляции Пирсона
corr, _ = pearsonr(st1,st2)
print("Коэффициент корреляции:", corr)

# t-тест
ttest_result = ttest_ind(st1, st2)
print("t-статистика:", ttest_result.statistic)
print("p-value:", ttest_result.pvalue)

