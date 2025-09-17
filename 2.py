import numpy as np
import time
import matplotlib.pyplot as plt
from statistics import mean

# Параметры эксперимента
N = 12  # 20 - 8 = 12
max_n = 10**2 * N  # максимальный размер матрицы (квадратный корень от предыдущего max_n)
step = 1*N  # шаг для размера матрицы
num_runs = 5  # уменьшили количество запусков, так как умножение матриц требует больше времени

# Списки для хранения результатов
n_values = []
times = []

# Проводим эксперимент для разных размеров матриц
for n in range(1, max_n + 1, step):
    
    # Генерируем две случайные матрицы размера n x n
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    print(f"Обрабатывается размер матрицы = {n}x{n}")
    run_times = []
    
    # Несколько запусков для усреднения
    for run in range(num_runs):
        # Замер времени умножения матриц
        start_time = time.time()
        
        # Умножение матриц - исследуемая операция
        C = np.dot(A, B)
        
        end_time = time.time()
        run_times.append(end_time - start_time)
    
    # Сохраняем среднее время
    n_values.append(n)
    times.append(mean(run_times))


plt.figure(figsize=(12, 6))
plt.plot(n_values, times, 'ro-', linewidth=2, markersize=6)
plt.xlabel('Размер матрицы (n x n)')
plt.ylabel('Среднее время умножения матриц (секунды)')
plt.title('Зависимость времени умножения матриц от их размера\n(Линейные оси)')
plt.grid(True, alpha=0.3)
plt.show()
