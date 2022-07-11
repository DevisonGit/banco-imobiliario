from tabuleiro import QTD_MAXIMA_RODADAS, Tabuleiro
import pandas as pd

QTD_MAXIMA_PARTIDAS = 300
FILE = "resultados.csv"


def simulacao():
    file = open(FILE, "w")
    file.write(f"vencedor;rodadas\n")
    qtd_partidas = 1
    while qtd_partidas <= QTD_MAXIMA_PARTIDAS:
        tabuleiro = Tabuleiro()
        tabuleiro.popular_jogadores()
        tabuleiro.popular_propriedades()
        tabuleiro.ordem_aleatoria()
        vencedor, qtd_rodadas = tabuleiro.partida()
        file.write(f"{vencedor};{qtd_rodadas} \n")
        qtd_partidas += 1
    file.close()


def resultado():
    df = pd.read_csv(FILE, sep=';')
    # Quantas partidas terminam por time out (1000 rodadas);
    df_time_out = df['rodadas'].value_counts()
    time_out = df_time_out.max() if df_time_out.idxmax() > QTD_MAXIMA_RODADAS else 0
    print(f"Quantas partidas terminam por time out (1000 rodadas): {time_out}\n")
    
    # Quantos turnos em média demora uma partida;
    media = df['rodadas'].mean()
    print(f"Quantos turnos em média demora uma partida: {media:.2f}\n")

    # Qual a porcentagem de vitórias por comportamento dos jogadores;
    print(f"Qual a porcentagem de vitórias por comportamento dos jogadores:")
    vencedores = round(df['vencedor'].value_counts(normalize=True) * 100, 2)
    print(vencedores.to_string(), '\n')

    # Qual o comportamento que mais vence.
    maior_vencedor = vencedores.idxmax()
    print(f"Qual o comportamento que mais vence: {maior_vencedor}\n")


if __name__ == "__main__":
    simulacao()
    resultado()
