import tkinter as tk
from tkinter import messagebox
import random

palavras_dicas = {
    "PYTHON": "Linguagem de programação",
    "INTERFACE": "Ponto de interação entre componentes",
    "PROGRAMACAO": "Atividade de escrever código",
    "JOGO": "Atividade de entretenimento",
    "FORCA": "Jogo de adivinhação de palavras",
    "FERRARI": "Marca de carro esportivo",
    "BORBOLETA": "Inseto com asas coloridas",
    "ROXO": "Cor",
    "ALFACE": "Vegetal de folhas verdes",
    "MORANGO": "Fruta vermelha e pequena",
    "PROFESSOR": "Pessoa que ensina",
    "UVA": "Fruta pequena e redonda",
    "BOLO": "Doce assado, geralmente servido em festas",
    "CACHORRO": "Animal de estimação, melhor amigo do homem",
    "SHOPPING": "Local de compras",
    "VIDA": "Estado de existência",
    "CARRO": "Veículo automotor",
    "GIRAFA": "Animal de pescoço longo",
    "LARANJA": "Fruta cítrica",
    "SOL": "Estrela que ilumina a Terra"
}

palavra, dica = random.choice(list(palavras_dicas.items()))

acertos = 0
pontos = 0
erros = 0

def iniciar_jogo():
    global palavra, dica, letras_descobertas, tentativas_restantes, acertos, pontos, erros
    palavra, dica = random.choice(list(palavras_dicas.items()))
    letras_descobertas = ['_' for _ in palavra]
    tentativas_restantes = 6
    erros = 0
    atualizar_palavra()
    atualizar_tentativas()
    dica_label.config(text=f"Dica: {dica}")
    for btn in botoes:
        btn.config(state=tk.NORMAL)
    msg_label.config(text="Adivinhe a palavra!")
    atualizar_acertos()
    atualizar_pontos()
    atualizar_erros()
    canvas.delete("all")
    desenhar_forca()

def atualizar_palavra():
    palavra_label.config(text=" ".join(letras_descobertas))

def atualizar_tentativas():
    tentativas_label.config(text=f"Tentativas restantes: {tentativas_restantes}")

def atualizar_acertos():
    acertos_label.config(text=f"Acertos: {acertos}")

def atualizar_pontos():
    pontos_label.config(text=f"Pontos: {pontos}")

def atualizar_erros():
    erros_label.config(text=f"Erros: {erros}")

def desenhar_forca():
    canvas.create_line(10, 150, 150, 150, width=3, fill="white")
    canvas.create_line(80, 150, 80, 10, width=3, fill="white")
    canvas.create_line(80, 10, 140, 10, width=3, fill="white")
    canvas.create_line(140, 10, 140, 30, width=3, fill="white")

def desenhar_boneco(erros):
    if erros == 1:
        canvas.create_oval(120, 30, 160, 70, width=3, outline="white")  # Cabeça
    elif erros == 2:
        canvas.create_line(140, 70, 140, 110, width=3, fill="white")  # Tronco
    elif erros == 3:
        canvas.create_line(140, 80, 120, 100, width=3, fill="white")  # Braço esquerdo
    elif erros == 4:
        canvas.create_line(140, 80, 160, 100, width=3, fill="white")  # Braço direito
    elif erros == 5:
        canvas.create_line(140, 110, 120, 140, width=3, fill="white")  # Perna esquerda
    elif erros == 6:
        canvas.create_line(140, 110, 160, 140, width=3, fill="white")  # Perna direita

def tentativa(letra):
    global tentativas_restantes, acertos, pontos, erros
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_descobertas[i] = letra
        atualizar_palavra()
        if '_' not in letras_descobertas:
            msg_label.config(text="Você venceu!")
            for btn in botoes:
                btn.config(state=tk.DISABLED)
            acertos += 1
            pontos += 10
            atualizar_acertos()
            atualizar_pontos()
    else:
        tentativas_restantes -= 1
        erros += 1
        desenhar_boneco(erros)
        atualizar_tentativas()
        atualizar_erros()
        if tentativas_restantes == 0:
            msg_label.config(text=f"Você perdeu! A palavra era: {palavra}")
            for btn in botoes:
                btn.config(state=tk.DISABLED)
            pontos -= 5
            atualizar_pontos()

root = tk.Tk()
root.title("Jogo da Forca")

fundo = "#4B0082"  # Violeta
root.configure(bg=fundo)

canvas = tk.Canvas(root, width=200, height=200, bg=fundo, highlightthickness=0)
canvas.pack(pady=10)
desenhar_forca()

palavra_label = tk.Label(root, text="", font=("Helvetica", 18), bg=fundo, fg="white")
palavra_label.pack(pady=10)

tentativas_label = tk.Label(root, text="", font=("Helvetica", 14), bg=fundo, fg="white")
tentativas_label.pack(pady=10)

msg_label = tk.Label(root, text="", font=("Helvetica", 14), bg=fundo, fg="white")
msg_label.pack(pady=10)

dica_label = tk.Label(root, text="", font=("Helvetica", 14), bg=fundo, fg="white")
dica_label.pack(pady=10)

acertos_label = tk.Label(root, text=f"Acertos: {acertos}", font=("Helvetica", 14), bg=fundo, fg="white")
acertos_label.pack(pady=10)

pontos_label = tk.Label(root, text=f"Pontos: {pontos}", font=("Helvetica", 14), bg=fundo, fg="white")
pontos_label.pack(pady=10)

erros_label = tk.Label(root, text=f"Erros: {erros}", font=("Helvetica", 14), bg=fundo, fg="white")
erros_label.pack(pady=10)

botoes_frame = tk.Frame(root, bg=fundo)
botoes_frame.pack(pady=10)

botoes = []
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i, letra in enumerate(letras):
    btn = tk.Button(botoes_frame, text=letra, font=("Helvetica", 12), width=4, command=lambda l=letra: tentativa(l))
    if i < 21:
        btn.grid(row=i // 7, column=i % 7, padx=2, pady=2)
    else:
        btn.grid(row=3, column=i - 21 + 1, padx=2, pady=2)
    botoes.append(btn)

reiniciar_btn = tk.Button(root, text="Reiniciar", font=("Helvetica", 14), command=iniciar_jogo)
reiniciar_btn.pack(pady=20)

iniciar_jogo()

root.mainloop()
