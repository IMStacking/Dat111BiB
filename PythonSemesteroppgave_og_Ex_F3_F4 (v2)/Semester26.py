from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

from Semester26_Model import predict_price


def draw_the_map():
    x, y = marked_point

    # Sammenlign fire boligstørrelser.
    m2list = [50, 100, 150, 200]
    price_m2 = []

    for area in m2list:
        total_price = predict_price(x, y, area, house_type, standard_type)
        price_m2.append(total_price * PRICE_FACTOR / area)

    # Det store tallet viser prisen per m² for 100 m².
    price = price_m2[m2list.index(m2)]
    price_label = f"{price:,.0f}".replace(",", " ")
    price_text.set_text(f"{price_label} kr/m²")
    marker.set_data([x], [y])

    # Fargen følger valgt standard.
    ax_history.clear()
    bar_color = standard_colors[standard_type]
    ax_history.bar(m2list, price_m2, color=bar_color, width=24)

    # Den stiplede linjen viser snittet av stolpene.
    gjennomsnitt = sum(price_m2) / len(price_m2)
    ax_history.axhline(
        gjennomsnitt, color=TEXT, linestyle="--", label="Gjennomsnitt"
    )

    ax_history.set_xticks(m2list)
    ax_history.set_xlabel("Boligareal (m²)")
    ax_history.set_ylabel("kr/m²")
    ax_history.set_axisbelow(True)
    ax_history.grid(axis="y", linestyle=":", alpha=0.4)
    ax_history.spines["top"].set_visible(False)
    ax_history.spines["right"].set_visible(False)
    ax_history.legend(fontsize=8, frameon=False)

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
standard_colors = {
    1: "red",
    2: "yellow",
    3: "green",
    4: "purple",
}

# Valgene som vises når programmet starter.
house_type = 1
standard_type = 1
m2 = 100
marked_point = (43, 57)

BACKGROUND = "#F1F5F9"
TEXT = "#172B3A"
BLUE = "#126782"
PRICE_FACTOR = 1000  # Bruk 1 hvis modellen gir prisen i hele kroner.

fig = plt.figure(figsize=(11, 7), facecolor=BACKGROUND)
fig.suptitle(
    "Boligpriser i Bergen",
    x=0.06,
    y=0.96,
    ha="left",
    fontsize=23,
    fontweight="bold",
    color=TEXT,
)

# Boligvalg og diagram til venstre, kart til høyre.
ax_radio_house_type = fig.add_axes((0.06, 0.68, 0.32, 0.14))
ax_radio_standard = fig.add_axes((0.06, 0.45, 0.32, 0.17))
ax_history = fig.add_axes((0.09, 0.12, 0.29, 0.18))
ax_map = fig.add_axes((0.44, 0.12, 0.52, 0.70))

ax_radio_house_type.set_title("Boligtype", loc="left", color=TEXT)
ax_radio_standard.set_title("Standard", loc="left", color=TEXT)
ax_map.set_title("Klikk i kartet for å velge sted", loc="left", color=TEXT)

radio_house = RadioButtons(ax_radio_house_type, list(house_types), activecolor=BLUE)
radio_standard = RadioButtons(ax_radio_standard, list(standard_types), activecolor=BLUE)
radio_house.on_clicked(on_house_type)
radio_standard.on_clicked(on_standard)

# Kartbildet ligger i samme mappe som programmet.
image_file = Path(__file__).resolve().parent / "Semester26_Bergen.jpg"
img = mpimg.imread(image_file)
ax_map.imshow(img, extent=(0, 100, 0, 100), aspect="auto")
ax_map.set_xticks([])
ax_map.set_yticks([])

marker, = ax_map.plot(
    [], [],
    marker="o",
    linestyle="none",
    color="red",
    markersize=11,
    markeredgecolor="white",
    markeredgewidth=2,
)

price_text = fig.text(
    0.06, 0.37, "", fontsize=20, fontweight="bold", color=TEXT
)
fig.text(0.06, 0.335, f"Estimat for {m2} m²", fontsize=10, color=TEXT)

draw_the_map()
plt.connect("button_press_event", on_click_map)
plt.show()