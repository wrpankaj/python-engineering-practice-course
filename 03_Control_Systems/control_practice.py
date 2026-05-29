import control as ctrl
import matplotlib.pyplot as plt

num = [10]
den = [1, 5, 6]

G = ctrl.TransferFunction(num, den)

print("Transfer Function:")
print(G)

poles = ctrl.poles(G)
print("Poles =", poles)

if all(p.real < 0 for p in poles):
    print("System is Stable")
else:
    print("System is Unstable")

t, y = ctrl.step_response(G)

plt.plot(t, y)
plt.title("Step Response of G(s)")
plt.xlabel("Time")
plt.ylabel("Output")
plt.grid(True)
plt.show()
