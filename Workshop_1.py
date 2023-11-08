import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

#print(mpl.get_backend())
#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the ax
#plt.show()

data = pd.read_csv('./Russia-Covid19-v2.csv', nrows=100)

#plt.hist(data['total infected'], bins=10, edgecolor='black')
#plt.title('Гистограмма данных')
#plt.xlabel('Значения')
#plt.ylabel('Частота')
#plt.show()
st1 = data['sick now']
st2 = data['new infections']
st3 = []
for i in range(len(st2)):
    st3.append((st1[i]+st2[i])/2)
    print(st1[i], st2[i], (st1[i]+st2[i])/2, st3[i])

# Создание графика
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика

# График с линиями (например, для временных рядов)
plt.plot(st1, label='total infected', linestyle='-', marker='o')
plt.plot(st2, label='total length / cm', linestyle='--', marker='x')
plt.plot(st3, label='sr', linestyle='--', marker='x')



# Добавление подписей к осям и заголовка
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('График данных из CSV-файла')

# Добавление легенды
plt.legend()

# Отображение графика
plt.grid(True)
plt.show()