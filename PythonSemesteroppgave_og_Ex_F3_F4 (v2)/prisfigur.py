"""Felles Matplotlib-figur for BIBs skrivebordsprogram og nettside."""

from Semester26_Model import predict_price

AREALER = (50, 100, 150, 200)
PRISFAKTOR = 1000  # Bruk 1 hvis modellen gir prisen i hele kroner.
BAKGRUNN = "#F1F5F9"
TEKSTFARGE = "#172B3A"
STANDARDFARGER = {1: "red", 2: "yellow", 3: "green", 4: "purple"}


def pris_per_kvm(x, y, boligtype, standard):
    return [
        predict_price(x, y, areal, boligtype, standard) * PRISFAKTOR / areal
        for areal in AREALER
    ]


def sett_opp_prisfigur(figur, bilde, diagramplass, kartplass, *, tittelstorrelse=23):
    figur.set_facecolor(BAKGRUNN)
    figur.suptitle(
        "Boligpriser i Bergen", x=0.06, y=0.96, ha="left",
        fontsize=tittelstorrelse, fontweight="bold", color=TEKSTFARGE,
    )
    diagram = figur.add_axes(diagramplass)
    kart = figur.add_axes(kartplass)
    kart.set_title("Klikk i kartet for å velge sted", loc="left", color=TEKSTFARGE)
    kart.imshow(bilde, extent=(0, 100, 0, 100), aspect="auto")
    kart.set_xticks([])
    kart.set_yticks([])
    merke, = kart.plot(
        [], [], marker="o", linestyle="none", color="red", markersize=11,
        markeredgecolor="white", markeredgewidth=2,
    )
    return diagram, kart, merke


def oppdater_prisfigur(diagram, merke, x, y, priser, standard):
    merke.set_data([x], [y])
    diagram.clear()
    if priser is None:
        diagram.set_axis_off()
        return

    diagram.bar(AREALER, priser, color=STANDARDFARGER[standard], width=24)
    gjennomsnitt = sum(priser) / len(priser)
    diagram.axhline(gjennomsnitt, color=TEKSTFARGE, linestyle="--", label="Gjennomsnitt")
    diagram.set_xticks(AREALER)
    diagram.set_xlabel("Boligareal (m²)")
    diagram.set_ylabel("kr/m²")
    diagram.set_axisbelow(True)
    diagram.grid(axis="y", linestyle=":", alpha=0.4)
    diagram.spines["top"].set_visible(False)
    diagram.spines["right"].set_visible(False)
    diagram.legend(fontsize=8, frameon=False)
