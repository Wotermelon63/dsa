import numpy as np
import time
import matplotlib.pyplot as plt
from statistics import mean

# Параметры эксперимента
N = 12  # 20 - 8 = 12
max_n = 10**5 * N  # 1.2 * 10^6
step = 1000 * N  # 120000 вместо 1200
num_runs = 5  # количество запусков для усреднения

# Списки для хранения результатов
n_values = []
times = []

#
for n in range(1, max_n + 1, step):
    
    v = np.random.rand(n) + 0.001  
    print(f"Обрабатывается n = {n}")
    run_times = []
    

    for run in range(num_runs):

        start_time = time.time()
        
        harmonic_mean = len(v) / np.sum(1.0 / v)
        
        end_time = time.time()
        run_times.append(end_time - start_time)
    
    n_values.append(n)
    times.append(mean(run_times))

plt.figure(figsize=(12, 6))
plt.plot(n_values, times, 'ro-', linewidth=2, markersize=6)
plt.xlabel('Размер вектора (n)')
plt.ylabel('Среднее время вычисления (секунды)')
plt.title('Зависимость времени вычисления среднего гармонического от размера вектора')
plt.grid(True, alpha=0.3)
plt.show()
