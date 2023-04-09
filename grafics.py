# Import Data https://habr.com/ru/post/468295/
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


def load_elements(self,spis,vid):
    try:
        self.figure.clear()
    except:
        pass
    self.figure = plt.figure(dpi= 80)
    self.canvas = FigureCanvas(self.figure)
    self.toolbar = NavigationToolbar(self.canvas, self)
    if vid == 'Понедельный график выработки и отгрузок':
        create_fig(self.figure.add_subplot(111),spis)
    if vid == 'План-фактный анализ по месяцам':
        create_fig_plan_fact(self.figure.add_subplot(111),spis,self)
    self.figure.subplots_adjust(0.03, 0.11, 0.98, 0.94)
    self.canvas.draw()
''
def create_fig_plan_fact(plt,spis,self):
    """b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white"""
    #df = pd.read_csv('https://github.com/selva86/datasets/raw/master/AirPassengers.csv')
    df = pd.DataFrame.from_records(spis[1:],columns=spis[0])
    # Get the Peaks and Troughs
    data = df['План, кг.'].values
    df.date = df['Месяц'].values
    df.value = df['План, кг.'].values
    df.otgr = df['Отгрузка, кг.'].values
    df.fact = df['Факт, кг.'].values
    df.vneplan = df['Внеплан, кг.'].values

    doublediff = np.sign(np.diff(df.fact))
    peak_locations = np.where(doublediff == 1)[0] + 1

    doublediff2 = np.sign(np.diff(-1*df.fact))
    trough_locations = np.where(doublediff2 == 1)[0] + 1


    doublediff_2 = df.otgr
    peak_locations_2 = np.where(doublediff_2)[0]

    doublediff2_2 = df.otgr
    trough_locations_2 = np.where(doublediff2_2)[0]

    doublediff3 = df.fact
    trough_locations_3 = np.where(doublediff3)[0]

    doublediff5 = df.vneplan
    trough_locations_5 = np.where(doublediff5)[0]
    # Draw Plot
    #plt.figure(figsize=(16,10), dpi= 80)
    #plt = Figure(figsize=(16,10), dpi= 80)
    plt.plot('Месяц', 'План, кг.', data=df, color='tab:blue', label='План, кг.',linewidth = 5)
    plt.plot('Месяц', 'Отгрузка, кг.', data=df, color='y', label='Отгрузка, кг.',linewidth = 5)
    plt.plot('Месяц', 'Факт, кг.', data=df, color='g', label='Факт, кг.', linewidth=5)
    plt.plot('Месяц', 'Внеплан, кг.', data=df, color='r', label='Внеплан, кг.', linewidth=5)


    plt.scatter(df.date[peak_locations], df.value[peak_locations], marker=mpl.markers.CARETUPBASE, color='tab:green', s=200, label='Рост Факт, кг.')
    plt.scatter(df.date[trough_locations], df.value[trough_locations], marker=mpl.markers.CARETDOWNBASE, color='tab:red', s=200, label='Падение Факт, кг.')
    plt.scatter(df.date[peak_locations_2], df.otgr[peak_locations_2], marker=".", color='tab:green', s=300, label='Отгрузка, кг.')
    plt.scatter(df.date[trough_locations_3], df.fact[trough_locations_3], marker=".", color='tab:green', s=300,
                label='Факт, кг.')
    plt.scatter(df.date[trough_locations_5], df.vneplan[trough_locations_5], marker=".", color='tab:green', s=300,
                label='Внеплан, кг.')

    # Annotate
    for t in trough_locations:
        plt.text(df.date[t], df.value[t] * 1.03, df.value[t], horizontalalignment='center', color='darkred', size=15)
    for p in peak_locations:
        plt.text(df.date[p], df.value[p] * 1.03, df.value[p], horizontalalignment='center', color='darkgreen', size = 15)


    for t, p in zip(trough_locations_2,peak_locations_2):
        plt.text(df.date[p], df.otgr[p]*1.03, df.otgr[p], horizontalalignment='center', color='darkgreen', size = 15)
        plt.text(df.date[t], df.otgr[t]*1.03, df.otgr[t], horizontalalignment='center', color='darkred', size = 15)

    for p in trough_locations_3:
        plt.text(df.date[p], df.fact[p] * 1.03, df.fact[p], horizontalalignment='center', color='darkgreen', size=15)

    for p in trough_locations_5:
        plt.text(df.date[p], df.vneplan[p] * 1.03, df.vneplan[p], horizontalalignment='center', color='darkgreen', size=15)


    # Decoration
    plt.set_title(f"План-фактный анализ по месяцам {self.ui.cmb_podrazdelenie.currentText()}")
    for label in plt.get_xticklabels(which='major'):
        label.set(rotation=90, horizontalalignment='right')

    plt.legend(loc='upper left')
    plt.grid(axis='y', alpha=.3)
    #plt.show()
    return plt



def create_fig(plt,spis):
    """b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white"""
    #df = pd.read_csv('https://github.com/selva86/datasets/raw/master/AirPassengers.csv')
    df = pd.DataFrame.from_records(spis[1:],columns=spis[0])
    # Get the Peaks and Troughs
    data = df['Выработка, кг.'].values
    df.date = df['Дата конца'].values
    df.value = df['Выработка, кг.'].values
    df.otgr = df['Тех. вес, кг.'].values
    df.post = df['Постов'].values
    df.proizv = df["Произв-ть,кг/см."].values

    doublediff = np.sign(np.diff(df.value))
    peak_locations = np.where(doublediff == 1)[0] + 1

    doublediff2 = np.sign(np.diff(-1*df.value))
    trough_locations = np.where(doublediff2 == 1)[0] + 1


    doublediff_2 = df.otgr
    peak_locations_2 = np.where(doublediff_2)[0]

    doublediff2_2 = df.otgr
    trough_locations_2 = np.where(doublediff2_2)[0]

    doublediff3 = df.post
    trough_locations_3 = np.where(doublediff3)[0]

    diff_proizv = df.proizv
    locations_proizv = np.where(diff_proizv)[0]

    # Draw Plot
    #plt.figure(figsize=(16,10), dpi= 80)
    #plt = Figure(figsize=(16,10), dpi= 80)
    plt.plot('Дата конца', 'Выработка, кг.', data=df, color='tab:blue', label='Выработка, кг.',linewidth = 5)
    plt.plot('Дата конца', 'Тех. вес, кг.', data=df, color='y', label='Тех. заверш. вес, кг.',linewidth = 5)
    plt.plot('Дата конца', 'Постов', data=df, color='g', label='Постов', linewidth=5)
    plt.plot('Дата конца', "Произв-ть,кг/см.", data=df, color='r', label="Произв-ть,кг/см.", linewidth=5)

    plt.scatter(df.date[peak_locations], df.value[peak_locations], marker=mpl.markers.CARETUPBASE, color='tab:green', s=200, label='Рост выработка')
    plt.scatter(df.date[trough_locations], df.value[trough_locations], marker=mpl.markers.CARETDOWNBASE, color='tab:red', s=200, label='Падение выработка')
    plt.scatter(df.date[peak_locations_2], df.otgr[peak_locations_2], marker=".", color='tab:green', s=300, label='Заверш. вес')
    plt.scatter(df.date[trough_locations_3], df.post[trough_locations_3], marker=".", color='tab:green', s=300,
                label='Постов')
    plt.scatter(df.date[locations_proizv], df.proizv[locations_proizv], marker=".", color='tab:green', s=300,
                label="Произв-ть,кг/см.")

    # Annotate
    for t in trough_locations:
        plt.text(df.date[t], df.value[t] * 1.03, df.value[t], horizontalalignment='center', color='darkred', size=15)
    for p in peak_locations:
        plt.text(df.date[p], df.value[p] * 1.03, df.value[p], horizontalalignment='center', color='darkgreen', size = 15)


    for t, p in zip(trough_locations_2,peak_locations_2):
        plt.text(df.date[p], df.otgr[p]*1.03, df.otgr[p], horizontalalignment='center', color='darkgreen', size = 15)
        plt.text(df.date[t], df.otgr[t]*1.03, df.otgr[t], horizontalalignment='center', color='darkred', size = 15)

    for p in trough_locations_3:
        plt.text(df.date[p], df.post[p] * 1.03, df.post[p]/1000, horizontalalignment='center', color='darkgreen', size=15)

    for p in locations_proizv:
        plt.text(df.date[p], df.proizv[p] * 1.03, df.proizv[p]/10, horizontalalignment='center', color='darkgreen', size=15)

    # Decoration
    plt.set_title("Понедельный график выработки по нарядам и отгрузок чистый металл")
    for label in plt.get_xticklabels(which='major'):
        label.set(rotation=90, horizontalalignment='right')
    #plt.ylim(50,750)
    #xtick_location = df.index.tolist()[::6]
    #xtick_labels = df.date.tolist()[::6]
    #plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=90, fontsize=12, alpha=.7)
    #plt.title("Peak and Troughs of Air Passengers value (1949 - 1969)", fontsize=22)
    #plt.yticks(fontsize=12, alpha=.7)

    # Lighten borders
    #plt.gca().spines["top"].set_alpha(.0)
    #plt.gca().spines["bottom"].set_alpha(.3)
    #plt.gca().spines["right"].set_alpha(.0)
    #plt.gca().spines["left"].set_alpha(.3)
    plt.legend(loc='upper left')
    plt.grid(axis='y', alpha=.3)
    #plt.show()
    return plt
