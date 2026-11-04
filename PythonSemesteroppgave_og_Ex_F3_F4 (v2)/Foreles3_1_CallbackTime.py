import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from datetime import  datetime as dt


def on_get_time(event):
    text = dt.now().strftime("%H:%M:%S")
    ax_time.set_title(text)
    plt.draw()

def on_get_point(event):
    # Data coordinates (in the plot)
    x = event.xdata
    y = event.ydata
    ax_point.set_title(f"X={x:.2f}, Y={y:.2f}")
    plt.draw()

fig = plt.figure(figsize=(4,3)) # type: ignore[arg-type]

ax_time = fig.add_axes((0.35, 0.05, 0.3, 0.2))
buttonTime = Button(ax_time, label="Update time", hovercolor='yellow')
buttonTime.on_clicked(on_get_time)

ax_point = fig.add_axes((0.20, 0.45, 0.6, 0.4))
button_point = Button(ax_point, label="Click Me", hovercolor='lightblue')
button_point.on_clicked(on_get_point)
plt.show()