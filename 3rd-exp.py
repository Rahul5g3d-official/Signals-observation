import numpy as np
import matplotlib.pyplot as plt

# 1. Define Standard Component Values
R = 1000.0          # Resistance in Ohms (1k)
C = 0.1e-6          # Capacitance in Farads (0.1uF)
V_supply = 12.0     # Supply Voltage (V)

# 2. Calculate Oscillation Frequency
# Formula: f = 1 / (2 * pi * R * C * sqrt(6))
f_osc = 1 / (2 * np.pi * R * C * np.sqrt(6))
period = 1 / f_osc

# 3. Generate Time Vector (simulate 5 cycles)
t = np.linspace(0, 5 * period, 1000)

# 4. Generate Output Sine Wave
# Note: In a real IC-741, the output swings near the supply rails
v_out = (V_supply - 2) * np.sin(2 * np.pi * f_osc * t)

# 5. Plotting the Results
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, v_out, label=f'Oscillator Output ({f_osc:.2f} Hz)', color='blue', linewidth=2)
plt.title('Python Simulation: RC Phase Shift Oscillator (IC-741)', fontsize=14)
plt.xlabel('Time (ms)', fontsize=12)
plt.ylabel('Output Voltage (V)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=1)
plt.legend(loc='upper right')
plt.show()

print(f"Calculated Frequency: {f_osc:.2f} Hz")