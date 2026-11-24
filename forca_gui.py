import random
import tkinter as tk


def carregar_palavras(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        palavras = f.readlines()

    return [palavra.strip().lower() for palavra in palavras]


def escolher_palavra(lista):
    return random.choice(lista)


def atualizar_display(palavra, letras_tentadas):
    display = ""

    for letra in palavra:
        if letra in letras_tentadas:
            display += letra + " "
        else:
            display += "_ "

    return display


def verificar_vitoria(palavra, letras_tentadas):
    return all(letra in letras_tentadas for letra in palavra)


def desenhar_boneco(erros):
    desenho.delete("all")

    desenho.create_line(20, 180, 180, 180, width=3)
    desenho.create_line(60, 180, 60, 20, width=3)
    desenho.create_line(60, 20, 140, 20, width=3)
    desenho.create_line(140, 20, 140, 40, width=3)

    if erros >= 1:
        desenho.create_oval(125, 40, 155, 70, width=2)
    if erros >= 2:
        desenho.create_line(140, 70, 140, 120, width=2)
    if erros >= 3:
        desenho.create_line(140, 85, 115, 105, width=2)
    if erros >= 4:
        desenho.create_line(140, 85, 165, 105, width=2)
    if erros >= 5:
        desenho.create_line(140, 120, 115, 150, width=2)
    if erros >= 6:
        desenho.create_line(140, 120, 165, 150, width=2)


lista_palavras = carregar_palavras("palavras.txt")
palavra_secreta = escolher_palavra(lista_palavras)
letras_tentadas = []
erros = 0
botoes_letras = {}
jogo_encerrado = False


def encerrar_jogo(vitoria):
    global jogo_encerrado

    if jogo_encerrado:
        return

    jogo_encerrado = True

    if vitoria:
        texto_palavra.config(text="Vitória!")
    else:
        texto_palavra.config(text=f"Derrota! Palavra: {palavra_secreta}")

    for botao in botoes_letras.values():
        botao.config(state="disabled")


def tentar_letra(letra):
    global erros

    if jogo_encerrado:
        return

    letras_tentadas.append(letra.lower())

    if letra.lower() not in palavra_secreta:
        erros += 1
        desenhar_boneco(erros)

    texto_palavra.config(
        text=atualizar_display(palavra_secreta, letras_tentadas)
    )
    texto_erros.config(text=f"Tentativas restantes: {6 - erros}")
    botoes_letras[letra].config(state="disabled")

    if verificar_vitoria(palavra_secreta, letras_tentadas):
        encerrar_jogo(True)
    elif erros >= 6:
        encerrar_jogo(False)


janela = tk.Tk()
janela.title("Jogo da Forca")
janela.geometry("600x650")

titulo = tk.Label(
    janela,
    text="MINHA FORCA",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=10)

desenho = tk.Canvas(
    janela,
    width=200,
    height=200,
    bg="white"
)
desenho.pack(pady=5)
desenhar_boneco(0)

texto_palavra = tk.Label(
    janela,
    text=atualizar_display(palavra_secreta, letras_tentadas),
    font=("Arial", 28)
)
texto_palavra.pack(pady=10)

texto_erros = tk.Label(
    janela,
    text="Tentativas restantes: 6",
    font=("Arial", 14)
)
texto_erros.pack(pady=5)

teclado = tk.Frame(janela)
teclado.pack(pady=20)

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i, letra in enumerate(letras):
    botao = tk.Button(
        teclado,
        text=letra,
        font=("Arial", 12),
        width=4,
        command=lambda l=letra: tentar_letra(l)
    )
    botao.grid(row=i // 7, column=i % 7, padx=3, pady=3)
    botoes_letras[letra] = botao

janela.mainloop()
