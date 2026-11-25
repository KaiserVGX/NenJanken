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

# Mensagem inicial
lbl_resultado = tk.Label(
    janela,
    text="Escolha seu golpe para comecar!",
    font=("Arial", 14, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_resultado.pack(pady=25)

# Inicia a interface
janela.mainloop()