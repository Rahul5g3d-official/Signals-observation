import math
Vcc = 12
R1 = 33000
R2 = 3300
RC1 = 1000
RE1 = 330
R3 = 33000
R4 = 3300
RC2 = 1000
RE2 = 330
RL = 4700
Cin = 10e-6
Ccoupling = 10e-6
Ce = 100e-6
Vbe = 0.7
VT = 0.026

Vb = Vcc * (R2 / (R1 + R2))
Ve = Vb - Vbe
Ie = Ve / RE1

re = VT / Ie
Av1 = -RC1 / re

RC2_parallel_RL = (RC2 * RL) / (RC2 + RL)
Av2 = -RC2_parallel_RL / re

Av_total = Av1 * Av2
Rin = (R1 * R2) / (R1 + R2)

fL_input = 1 / (2 * math.pi * Rin * Cin)
fL_interstage = 1 / (2 * math.pi * Rin * Ccoupling)
fL_emitter = 1 / (2 * math.pi * RE1 * Ce)

fL = max(fL_input, fL_interstage, fL_emitter)
print("Stage-1 Voltage Gain =", round(Av1, 2))
print("Stage-2 Voltage Gain =", round(Av2, 2))
print("Total Voltage Gain   =", round(Av_total, 2))
print("Lower Cutoff Frequency =", round(fL, 2), "Hz")
