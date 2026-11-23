Gerenciador de Downloads

Script em Python que organiza automaticamente a sua pasta de Downloads. Ele roda em segundo plano, sem janela e sem a tela preta do terminal, e move cada arquivo novo para a subpasta certa.

Funciona somente no Windows.

O que ele faz

A cada 10 segundos, o script confere a pasta de Downloads e move os arquivos para estas subpastas (criadas automaticamente):

Pasta	Extensões
video	.mp4 .mkv .avi .mov .webm
img	.jpg .jpeg .png .gif .webp .bmp
pdf	.pdf
som	.mp3 .wav .ogg .flac .m4a
instalador	.exe .msi

Outros detalhes:

Espera o download terminar antes de mover o arquivo.
Se já existir um arquivo com o mesmo nome no destino, renomeia o novo (foto.png vira foto_1.png).
Arquivos com outras extensões e subpastas são ignorados.
Requisitos
Windows 10 ou 11
Python 3.8 ou superior

Não precisa instalar nenhuma biblioteca. Na instalação do Python, marque "Add Python to PATH".

Como usar
Baixe o arquivo gerenciador.pyw (ou clone o repositório).
crie um atalho do gerenciador
aperte win+r e digite: shell:startup
mova o atalho para a pasta que abrir feche a pasta e de clique duplo no gerenciador.
agora sempre que você ligar o computador o gerenciador vai estar rodando

#criador:benedito
