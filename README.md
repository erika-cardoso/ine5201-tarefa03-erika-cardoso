# Forca no Mar

Jogo da forca com interface gráfica em Python e Tkinter. A cada partida, uma palavra aleatória do tema marinho é escolhida do arquivo `palavras.txt`.

## Recursos

- Teclado virtual com letras de A a Z e letras acentuadas do português.
- Palavras com acentos e hifens.
- Desenho da forca atualizado a cada erro.
- Limite de seis erros por partida.
- Indicação de vitória, derrota ou desistência.
- Botoes para iniciar outra partida ou desistir.
- Placar de vitorias e derrotas durante a execucao do aplicativo.
- Interface com cores e ilustracoes inspiradas no mar.

## Requisitos

- Python 3.
- Tkinter, incluido na distribuicao padrao do Python para Windows.

O jogo não requer pacotes Python externos.

## Como executar

Abra um terminal na pasta do projeto e execute:

```powershell
python forca_gui.py
```

O programa carrega `palavras.txt` usando o diretório atual. Execute o comando a partir da pasta que contém os dois arquivos.

## Como jogar

1. Clique nas letras para tentar descobrir a palavra.
2. Cada letra incorreta desenha uma parte do boneco e reduz as tentativas restantes.
3. Acerte todas as letras antes de completar seis erros para vencer.
4. Use **Novo jogo** para sortear outra palavra. O placar atual e mantido.
5. Use **Desistir** para encerrar a partida e revelar a palavra; a desistencia conta como derrota.

O placar é mantido apenas enquanto o aplicativo estiver aberto. Ele volta a zero quando o programa é iniciado novamente.

## Arquivos

| Arquivo | Descrição |
| --- | --- |
| `forca_gui.py` | Interface Tkinter, regras e fluxo das partidas. |
| `palavras.txt` | Lista de palavras usadas para sortear as partidas. |
| `README.md` | Instrucoes do projeto. |

Para adicionar palavras, inclua uma por linha em `palavras.txt`. Letras acentuadas e hifens são aceitos.
