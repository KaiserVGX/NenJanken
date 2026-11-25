"""
NenJanken - Duelo de Aura
Jogo inspirado nas categorias de Nen de Hunter x Hunter.

Integrantes: Lucas Linhares e Rafael Maia
Disciplina: Logica, Algoritmos e Programacao
"""

import tkinter as tk
from tkinter import messagebox
import random

# Cores principais do jogo
COR_FUNDO = "#1e1e2e"
COR_CARD = "#313244"
COR_TEXTO = "#e0e0e0"
COR_ROXO = "#7c3aed"
COR_AMARELO = "#eab308"

# Variaveis do jogo
placar_jogador = 0
placar_pc = 0
rodada = 0

# Cadastro dos golpes e categorias de Nen
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

# Lista de opcoes do jogo
opcoes = list(GOLPES.keys())

# Regras de vitoria
VENCE = {
    "pedra": ["tesoura", "estalo"],
    "tesoura": ["papel", "escudo"],
    "papel": ["pedra", "garra"],
    "escudo": ["pedra", "estalo"],
    "garra": ["tesoura", "escudo"],
    "estalo": ["papel", "garra"]
}

# Golpes que causam choque de aura
NEUTRO = {
    "pedra": "garra",
    "tesoura": "estalo",
    "papel": "escudo",
    "escudo": "papel",
    "garra": "pedra",
    "estalo": "tesoura"
}


# Funcao para mostrar o golpe escolhido
def mostrar_escolha(golpe):
    emoji = GOLPES[golpe]["emoji"]
    categoria = GOLPES[golpe]["categoria"]

    lbl_resultado.config(
        text="Voce escolheu: " + emoji + " " + golpe.capitalize()
        + "\nCategoria: " + categoria,
        fg=COR_AMARELO
    )


# Funcoes dos botoes
def jogar_pedra():
    mostrar_escolha("pedra")


def jogar_tesoura():
    mostrar_escolha("tesoura")


def jogar_papel():
    mostrar_escolha("papel")


def jogar_escudo():
    mostrar_escolha("escudo")


def jogar_garra():
    mostrar_escolha("garra")


def jogar_estalo():
    mostrar_escolha("estalo")


# Criacao da janela principal
janela = tk.Tk()
janela.title("NenJanken - Duelo de Aura")
janela.geometry("760x850")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

# Titulo do jogo
lbl_titulo = tk.Label(
    janela,
    text="NENJANKEN",
    font=("Arial", 30, "bold"),
    bg=COR_FUNDO,
    fg=COR_ROXO
)
lbl_titulo.pack(pady=(25, 5))

# Subtitulo
lbl_subtitulo = tk.Label(
    janela,
    text="DUELO DE AURA - Sistema de Combate Nen",
    font=("Arial", 12),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_subtitulo.pack(pady=5)

# Identificacao dos jogadores
lbl_jogadores = tk.Label(
    janela,
    text="JOGADOR  VS  COMPUTADOR",
    font=("Arial", 14, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_jogadores.pack(pady=20)

# Placar inicial
lbl_placar = tk.Label(
    janela,
    text="0  x  0",
    font=("Arial", 28, "bold"),
    bg=COR_CARD,
    fg=COR_AMARELO,
    width=15
)
lbl_placar.pack(pady=10)

# Contador de rodadas
lbl_rodada = tk.Label(
    janela,
    text="Rodada: 0",
    font=("Arial", 12),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_rodada.pack(pady=10)

# Mensagem de resultado e escolha
lbl_resultado = tk.Label(
    janela,
    text="Escolha seu golpe para comecar!",
    font=("Arial", 14, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_resultado.pack(pady=20)

# Titulo da area de escolha
lbl_escolha = tk.Label(
    janela,
    text="ESCOLHA SUA CATEGORIA DE NEN",
    font=("Arial", 15, "bold"),
    bg=COR_FUNDO,
    fg=COR_ROXO
)
lbl_escolha.pack(pady=10)

# Area onde ficam os botoes
frame_golpes = tk.Frame(janela, bg=COR_FUNDO)
frame_golpes.pack(pady=10)

# Botao Pedra
btn_pedra = tk.Button(
    frame_golpes,
    text="🪨 Pedra\nReforço",
    font=("Arial", 11, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=20,
    height=3,
    command=jogar_pedra
)
btn_pedra.grid(row=0, column=0, padx=8, pady=8)

# Botao Tesoura
btn_tesoura = tk.Button(
    frame_golpes,
    text="✂️ Tesoura\nTransformação",
    font=("Arial", 11, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=20,
    height=3,
    command=jogar_tesoura
)
btn_tesoura.grid(row=0, column=1, padx=8, pady=8)

# Botao Papel
btn_papel = tk.Button(
    frame_golpes,
    text="📄 Papel\nEmissão",
    font=("Arial", 11, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=20,
    height=3,
    command=jogar_papel
)
btn_papel.grid(row=1, column=0, padx=8, pady=8)

# Botao Escudo
btn_escudo = tk.Button(
    frame_golpes,
    text="🛡️ Escudo\nConjuração",
    font=("Arial", 11, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=20,
    height=3,
    command=jogar_escudo
)
btn_escudo.grid(row=1, column=1, padx=8, pady=8)

# Botao Garra
btn_garra = tk.Button(
    frame_golpes,
    text="🐾 Garra\nManipulação",
    font=("Arial", 11, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=20,
    height=3,
    command=jogar_garra
)
btn_garra.grid(row=2, column=0, padx=8, pady=8)

# Botao Estalo
btn_estalo = tk.Button(
    frame_golpes,
    text="👆 Estalo\nEspecialização",
    font=("Arial", 11, "bold"),
    bg=COR_CARD,
    fg=COR_TEXTO,
    width=20,
    height=3,
    command=jogar_estalo
)
btn_estalo.grid(row=2, column=1, padx=8, pady=8)

# Inicia a interface
janela.mainloop()