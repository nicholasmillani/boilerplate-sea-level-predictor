import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Carregar os dados
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Criar figura e eixo
    fig, ax = plt.subplots()

    # 3. Scatter plot dos dados reais
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 4. Regressão linear com todos os dados
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    ax.plot(years_extended, intercept + slope * years_extended, 'r')

    # 5. Regressão linear a partir de 2000
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, intercept_recent + slope_recent * years_recent, 'g')

    # 6. Customização do gráfico
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # 7. Salvar a figura
    plt.savefig("sea_level_plot.png")
    return plt.gca()
