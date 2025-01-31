import numpy as np
import matplotlib.pyplot as plt

# Parametre
alpha = 10 # amplituda deterministickej casti
omega = 2 * np.pi / 24 # frekvencia pre dennu oscilaciu (1 perioda = 24hod)
phi = np.random.uniform(0, 2 * np.pi) # nahodny stav
sigma = 3 # standardna odchylka sumu
lambda_decay = 0.1 # rychlost poklesu kovariancie sumu
T = 100 * 24 # celkovy cas
dt = 0.1 # krok v case (hodiny)

# Casove pole
time = np.arange(0, T, dt)

deterministic_part = alpha * np.cos(omega * time + phi)

# Generovanie nahodneho sumu pomocou Gaussovho procesu (Ornstein-Uhlenbeckov proces) numericky
n_points = len(time)
def ornstein_uhlenbeck_process(n, dt, theta=0.1, sigma=3):
    noise = np.zeros(n)
    for i in range(1, n):
        noise[i] = noise[i-1] - theta * (noise[i-1] * dt) + sigma * np.sqrt(dt) * np.random.randn()
    return noise

random_noise = ornstein_uhlenbeck_process(n_points, dt, lambda_decay, sigma)
temperature = deterministic_part + random_noise

# Vizualizacia
plt.figure(figsize=(12, 6))
plt.plot(time / 24, temperature, label="Simulated Temperature", linewidth=1.5)
plt.plot(time / 24, deterministic_part, label="Deterministic Part", linestyle="--", linewidth=1.5)
plt.xlabel("Time (days)")
plt.ylabel("Temperature")
plt.title("Simulated Temperature Oscillation")
plt.legend()
plt.grid()
plt.show()
