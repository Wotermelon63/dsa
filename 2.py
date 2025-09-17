import numpy as np
import time
import matplotlib.pyplot as plt
from statistics import mean

N = 12 
max_n = 10**2 * N
step = 1*N
num_runs = 5   

n_values = []
times = []

for n in range(1, max_n + 1, step):
    
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    print(f"Обрабатывается размер матрицы = {n}x{n}")
    run_times = []
    
    for run in range(num_runs):
        start_time = time.time()
        
        C = np.dot(A, B)
        
        end_time = time.time()
        run_times.append(end_time - start_time)
    
    n_values.append(n)
    times.append(mean(run_times))


plt.figure(figsize=(12, 6))
plt.plot(n_values, times, 'ro-', linewidth=2, markersize=6)
plt.xlabel('Размер матрицы (n x n)')
plt.ylabel('Среднее время умножения матриц (секунды)')
plt.title('Зависимость времени умножения матриц от их размера\n(Линейные оси)')
plt.grid(True, alpha=0.3)
plt.show()
