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
lbl_titulo.pack(pady=30)

# Subtitulo
lbl_subtitulo = tk.Label(
    janela,
    text="DUELO DE AURA",
    font=("Arial", 14, "bold"),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_subtitulo.pack(pady=10)

# Identificacao dos integrantes
lbl_integrantes = tk.Label(
    janela,
    text="Lucas Linhares e Rafael Maia",
    font=("Arial", 11),
    bg=COR_FUNDO,
    fg=COR_TEXTO
)
lbl_integrantes.pack(pady=5)

# Mantem a janela aberta
janela.mainloop()