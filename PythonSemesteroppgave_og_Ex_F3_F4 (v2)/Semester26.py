from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

from prisfigur import AREALER, TEKSTFARGE, oppdater_prisfigur, pris_per_kvm, sett_opp_prisfigur


def draw_the_map():
    x, y = marked_point

    price_m2 = pris_per_kvm(x, y, house_type, standard_type)
    price = price_m2[AREALER.index(m2)]
    price_label = f"{price:,.0f}".replace(",", " ")
    price_text.set_text(f"{price_label} kr/m²")
    oppdater_prisfigur(ax_history, marker, x, y, price_m2, standard_type)

    plt.draw()


def on_click_map(event):
    global marked_point

    if event.inaxes != ax_map or event.button != 1:
        return

    marked_point = (event.xdata, event.ydata)
    draw_the_map()


def on_house_type(key):
    global house_type
    house_type = house_types[key]
    draw_the_map()


def on_standard(key):
    global standard_type
    standard_type = standard_types[key]
    draw_the_map()


house_types = {"Enebolig": 1, "Rekkehus": 2, "Leilighet": 3}
standard_types = {"Dårlig": 1, "God": 2, "Meget god": 3, "Luksus": 4}
# Valgene som vises når programmet starter.
house_type = 1
standard_type = 1
m2 = 100
marked_point = (43, 57)

BLUE = "#126782"

fig = plt.figure(figsize=(11, 7))

# Boligvalg og diagram til venstre, kart til høyre.
ax_radio_house_type = fig.add_axes((0.06, 0.68, 0.32, 0.14))
ax_radio_standard = fig.add_axes((0.06, 0.45, 0.32, 0.17))

ax_radio_house_type.set_title("Boligtype", loc="left", color=TEKSTFARGE)
ax_radio_standard.set_title("Standard", loc="left", color=TEKSTFARGE)

radio_house = RadioButtons(ax_radio_house_type, list(house_types), activecolor=BLUE)
radio_standard = RadioButtons(ax_radio_standard, list(standard_types), activecolor=BLUE)
radio_house.on_clicked(on_house_type)
radio_standard.on_clicked(on_standard)

# Kartbildet ligger i samme mappe som programmet.
image_file = Path(__file__).resolve().parent / "Semester26_Bergen.jpg"
img = mpimg.imread(image_file)
ax_history, ax_map, marker = sett_opp_prisfigur(
    fig, img, (0.09, 0.12, 0.29, 0.18), (0.44, 0.12, 0.52, 0.70),
)

price_text = fig.text(
    0.06, 0.37, "", fontsize=20, fontweight="bold", color=TEKSTFARGE
)
fig.text(0.06, 0.335, f"Estimat for {m2} m²", fontsize=10, color=TEKSTFARGE)

draw_the_map()
plt.connect("button_press_event", on_click_map)
plt.show()
