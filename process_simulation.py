import numpy as np
import matplotlib.pyplot as plt

# Parametre
alpha = 10 # amplituda deterministickej casti
omega = 2 * np.pi / 24 # frekvencia pre dennu oscilaciu (1 perioda = 24hod)
phi = np.random.uniform(0, 2 * np.pi) # nahodny stav
sigma = 3 # standardna odchylka sumu
lambda_decay = 0.1 # rychlost kovariancie sumu
T = 48 # celkovy cas
dt = 0.1 # krok v case

# Casove pole
time = np.arange(0, T, dt)

deterministic_part = alpha * np.cos(omega * time + phi)

# Generovanie nahodne sumu pomocou Gaussovho procesu
n_points = len(time)
noise_covariance = np.exp(-lambda_decay * np.abs(np.subtract.outer(time, time)))
random_noise = np.random.multivariate_normal(mean=np.zeros(n_points), cov=sigma**2 * noise_covariance)

temperature = deterministic_part + random_noise

# Vypisanie prvych 10 hodnot v case
first_10_times = time[:10]
first_10_temperatures = temperature[:10]
for t, temp in zip(first_10_times, first_10_temperatures):
    print(f"Time: {t:.1f} hours, Temperature: {temp:.2f}")

# Vizualizacia
plt.figure(figsize=(10, 6))
plt.plot(time, temperature, label="Simulated Temperature", linewidth=1.5)
plt.plot(time, deterministic_part, label="Deterministic Part", linestyle="--", linewidth=1.5)
plt.xlabel("Time (hours)")
plt.ylabel("Temperature")
plt.title("Simulated Temperature Oscillation")
plt.legend()
plt.grid()
plt.show()
