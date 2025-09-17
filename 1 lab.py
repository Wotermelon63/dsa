import numpy as np
import time
import matplotlib.pyplot as plt
from statistics import mean

# Параметры эксперимента
N = 12  # 20 - 8 = 12
max_n = 10**5 * N  # 1.2 * 10^6
step = 1000 * N  # Увеличиваем шаг в 100 раз: 120000 вместо 1200
num_runs = 5  # количество запусков для усреднения

# Списки для хранения результатов
n_values = []
times = []

# Проводим эксперимент для разных размеров вектора
for n in range(1, max_n + 1, step):
    print(f"Обрабатывается n = {n}")
    
    # Генерируем случайный вектор с неотрицательными элементами
    v = np.random.rand(n)
    
    run_times = []
    
    # Пять запусков для усреднения
    for run in range(num_runs):
        # Выбираем случайный индекс для доступа
        random_index = np.random.randint(0, n)
        
        # Замер времени доступа к элементу
        start_time = time.time()
        
        # Доступ к элементу по индексу - исследуемая операция
        element = v[random_index]
        
        end_time = time.time()
        run_times.append(end_time - start_time)
    
    # Сохраняем среднее время
    n_values.append(n)
    times.append(mean(run_times))

# Построение графика с линейными осями
plt.figure(figsize=(12, 6))
plt.plot(n_values, times, 'bo-', linewidth=2, markersize=6)
plt.xlabel('Размер вектора (n)')
plt.ylabel('Среднее время доступа (секунды)')
plt.title('Зависимость времени доступа к элементу от размера вектора\n(Линейные оси, большой шаг)')
plt.grid(True, alpha=0.3)
plt.show()
