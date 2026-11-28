"""
NenJanken - Duelo de Aura
Dupla: Lucas Linhares e Rafael Maia
Disciplina: Lógica, Algoritmos e Programação
"""

import tkinter as tk
from tkinter import messagebox
import random

# Cores do jogo
COR_FUNDO = "#1e1e2e"
COR_CARD = "#292943"
COR_TEXTO = "#e0e0e0"
COR_ROXO = "#7c3aed"
COR_AZUL = "#3b82f6"
COR_VERDE = "#22c55e"
COR_VERMELHO = "#ef4444"
COR_AMARELO = "#eab308"

# Categorias e golpes de Nen
GOLPES = {
    "pedra": {
        "emoji": "🪨",
        "categoria": "Reforço",
        "descricao": "Soco concentrado de força bruta"
    },
    "tesoura": {
        "emoji": "✂️",
        "categoria": "Transformação",
        "descricao": "Lâmina de aura cortante"
    },
    "papel": {
        "emoji": "📄",
        "categoria": "Emissão",
        "descricao": "Disparo de esfera de aura"
    },
    "escudo": {
        "emoji": "🛡️",
        "categoria": "Conjuração",
        "descricao": "Materialização de uma barreira"
    },
    "garra": {
        "emoji": "🐾",
        "categoria": "Manipulação",
        "descricao": "Controle através de aura"
    },
    "estalo": {
        "emoji": "👆",
        "categoria": "Especialização",
        "descricao": "Ativação de uma regra especial"
    }
}

opcoes = list(GOLPES.keys())

# Regras de vitória
VENCE = {
    "pedra": ["tesoura", "estalo"],
    "tesoura": ["papel", "escudo"],
    "papel": ["pedra", "garra"],
    "escudo": ["pedra", "estalo"],
    "garra": ["tesoura", "escudo"],
    "estalo": ["papel", "garra"]
}

# Combinações neutras
NEUTRO = {
    "pedra": "garra",
    "garra": "pedra",
    "tesoura": "estalo",
    "estalo": "tesoura",
    "papel": "escudo",
    "escudo": "papel"
}

# Variáveis do jogo
placar_jogador = 0
placar_pc = 0
rodada = 0
historico = []


# Mostra o emoji do golpe
def mostrar_emoji(golpe):
    return GOLPES[golpe]["emoji"]


# Atualiza o histórico
def atualizar_historico():
    texto = ""

    for item in historico:
        texto = texto + item + "\n"

    if texto == "":
        texto = "Nenhuma rodada ainda"

    lbl_historico.config(text=texto)


# Verifica o resultado da partida
def verificar_resultado(jogador, computador):
    if jogador == computador:
        return "EMPATE!", COR_AMARELO, "empate"

    elif NEUTRO[jogador] == computador:
        return "CHOQUE DE AURA!", COR_AMARELO, "empate"

    elif computador in VENCE[jogador]:
        return "VOCE VENCEU!", COR_VERDE, "vitoria"

    else:
        return "PC VENCEU!", COR_VERMELHO, "derrota"


# Realiza uma rodada
def jogar(escolha_jogador):
    global placar_jogador, placar_pc, rodada

    escolha_pc = random.choice(opcoes)
    rodada = rodada + 1

    lbl_jogador.config(
        text="Você: " + mostrar_emoji(escolha_jogador)
        + " " + GOLPES[escolha_jogador]["categoria"]
    )

    lbl_pc.config(
        text="PC: " + mostrar_emoji(escolha_pc)
        + " " + GOLPES[escolha_pc]["categoria"]
    )

    resultado, cor, tipo = verificar_resultado(
        escolha_jogador, escolha_pc
    )

    if tipo == "vitoria":
        placar_jogador = placar_jogador + 1

    elif tipo == "derrota":
        placar_pc = placar_pc + 1

    lbl_resultado.config(text=resultado, fg=cor)

    lbl_placar.config(
        text="Você: " + str(placar_jogador)
        + "   |   PC: " + str(placar_pc)
    )

    lbl_rodada.config(text="Rodada: " + str(rodada))

    # Registra a partida no histórico
    linha = (
        "R" + str(rodada) + ": "
        + mostrar_emoji(escolha_jogador) + " vs "
        + mostrar_emoji(escolha_pc) + " - "
        + resultado
    )

    historico.append(linha)

    if len(historico) > 6:
        historico.pop(0)

    atualizar_historico()


# Funções dos botões de escolha
def jogar_pedra():
    jogar("pedra")


def jogar_tesoura():
    jogar("tesoura")


def jogar_papel():
    jogar("papel")


def jogar_escudo():
    jogar("escudo")


def jogar_garra():
    jogar("garra")


def jogar_estalo():
    jogar("estalo")


# Reinicia os dados da partida
def reiniciar():
    global placar_jogador, placar_pc, rodada, historico

    resposta = messagebox.askyesno(
        "Reiniciar jogo",
        "Deseja realmente reiniciar a partida?"
    )

    if resposta:
        placar_jogador = 0
        placar_pc = 0
        rodada = 0
        historico = []

        lbl_placar.config(text="Você: 0   |   PC: 0")
        lbl_rodada.config(text="Rodada: 0")
        lbl_jogador.config(text="Você: —")
        lbl_pc.config(text="PC: —")
        lbl_resultado.config(
            text="Faça sua escolha!",
            fg=COR_TEXTO
        )

        atualizar_historico()


# Confirma antes de fechar o jogo
def sair():
    resposta = messagebox.askyesno(
        "Sair do NenJanken",
        "Deseja realmente sair do jogo?"
    )

    if resposta:
        janela.destroy()


# Criação da janela
janela = tk.Tk()
janela.title("NenJanken - Duelo de Aura")
janela.geometry("760x850")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

# Título
lbl_titulo = tk.Label(
    janela,
    text="NENJANKEN",
    font=("Arial", 28, "bold"),
    bg=COR_FUNDO,
    fg=COR_ROXO
)
lbl_titulo.pack(pady=(15, 2))

lbl_subtitulo = tk.Label(
    janela,
    text="DUELO DE AURA",
    font=("Arial", 14, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_subtitulo.pack()

lbl_nomes = tk.Label(
    janela,
    text="Lucas Linhares  •  Rafael Maia",
    font=("Arial", 10),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_nomes.pack(pady=(2, 10))

# Placar
lbl_placar = tk.Label(
    janela,
    text="Você: 0   |   PC: 0",
    font=("Arial", 17, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=30,
    pady=8
)
lbl_placar.pack(pady=5)

lbl_rodada = tk.Label(
    janela,
    text="Rodada: 0",
    font=("Arial", 12),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_rodada.pack(pady=5)

# Escolhas
lbl_jogador = tk.Label(
    janela,
    text="Você: —",
    font=("Arial", 12),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_jogador.pack(pady=3)

lbl_pc = tk.Label(
    janela,
    text="PC: —",
    font=("Arial", 12),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_pc.pack(pady=3)

lbl_resultado = tk.Label(
    janela,
    text="Faça sua escolha!",
    font=("Arial", 18, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_resultado.pack(pady=8)

# Área dos golpes
lbl_escolha = tk.Label(
    janela,
    text="ESCOLHA SUA CATEGORIA DE NEN",
    font=("Arial", 13, "bold"),
    bg=COR_FUNDO,
    fg=COR_ROXO
)
lbl_escolha.pack(pady=5)

# Botões de escolha
frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack(pady=5)

botoes = [
    ("🪨 Pedra\nReforço", jogar_pedra),
    ("✂️ Tesoura\nTransformação", jogar_tesoura),
    ("📄 Papel\nEmissão", jogar_papel),
    ("🛡️ Escudo\nConjuração", jogar_escudo),
    ("🐾 Garra\nManipulação", jogar_garra),
    ("👆 Estalo\nEspecialização", jogar_estalo)
]

for i, item in enumerate(botoes):
    botao = tk.Button(
        frame_botoes,
        text=item[0],
        command=item[1],
        font=("Arial", 10, "bold"),
        bg=COR_CARD,
        fg=COR_TEXTO,
        activebackground=COR_ROXO,
        activeforeground="white",
        width=17,
        height=2
    )

    botao.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

# Histórico
lbl_titulo_historico = tk.Label(
    janela,
    text="HISTÓRICO DE PARTIDAS",
    font=("Arial", 12, "bold"),
    bg=COR_FUNDO,
    fg=COR_ROXO
)
lbl_titulo_historico.pack(pady=(10, 3))

lbl_historico = tk.Label(
    janela,
    text="Nenhuma rodada ainda",
    font=("Arial", 10),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=65,
    height=6,
    justify="left",
    anchor="w"
)
lbl_historico.pack(pady=3)

# Botões de controle
frame_controles = tk.Frame(janela, bg=COR_FUNDO)
frame_controles.pack(pady=12)

btn_reiniciar = tk.Button(
    frame_controles,
    text="REINICIAR",
    command=reiniciar,
    font=("Arial", 10, "bold"),
    bg=COR_AZUL,
    fg="white",
    width=16,
    height=2
)
btn_reiniciar.grid(row=0, column=0, padx=8)

btn_sair = tk.Button(
    frame_controles,
    text="SAIR",
    command=sair,
    font=("Arial", 10, "bold"),
    bg=COR_VERMELHO,
    fg="white",
    width=16,
    height=2
)
btn_sair.grid(row=0, column=1, padx=8)

janela.mainloop()