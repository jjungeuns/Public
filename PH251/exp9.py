import numpy as np                              # basic
import matplotlib.pyplot as plt                 # plot

plt.rcParams['font.family'] = 'Times New Roman'

def sin_func(frequency, amplitude):
    time = np.arange(0, 3, 0.001)
    x = amplitude * np.sin(2*np.pi*frequency*time)
    return time, x

def inverse_FT(function_type) :
    freq_arr = function_type[0]
    amp_arr = function_type[1]
    time = np.arange(0, 3, 0.001)
    x = 0
    for i in range(0, len(amp_arr)) :
        x = x + (amp_arr[i]/sum(amp_arr)) * np.sin(2*np.pi*freq_arr[i]*time)
    return time, x    


sin = (np.array([1.00, 2.00, 3.00, 4.00, 5.00]), np.array([368.40, 34.10, 31.70, 15.10, 25.40]))
triangle = (np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]), np.array([367.8, 59.5, 52.0, 42.1, 25.1, 36.8, 37.8, 36.2, 31.6, 19.9]))
square = (np.array([1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]), np.array([367.50, 30.90, 57.90, 29.40, 53.57, 28.90, 50.48, 28.3, 48.2, 27.6]))

plot_type = (sin, triangle, square)
color = ['black', 'r', 'b']
label_plot_type = ["sin", "triangle", "square"]

fig, axs = plt.subplots(3, figsize=(10, 8), sharey=True)
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.grid(False)
for i in range(3) :
    axs[i].plot(inverse_FT(plot_type[i])[0], inverse_FT(plot_type[i])[1], c=color[i], label=label_plot_type[i])
    axs[i].legend(fontsize=15)

plt.xlabel("Time", size=20)
plt.ylabel("Normalized Amplitude", size=20)

plt.show()
