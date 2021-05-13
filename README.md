<h1> Fazer Dowload de músicas através do Python </h1>
<hr>

<h4 align='right'>Para visualizar o arquivo .py <a href='Mp3_Dowloader.py'> Clique aqui </a> </h4>

<h2>Sobre o projeto </h2>
<li> <b>Acredito que algum de vocês já encontraram uma música que está somente no youtube e gostou tanto dela que pretende baixa-la para poder ouvir offline, porém procurando por sites para fazer dowload de músicas, nos deparamos com aqueles inumeros anuncios e diversas etapas que precisam ser feitas para que a gente possa fazer um simples dowload. <br>
Enquanto estava em meus estudos em python verifiquei que era possivel fazer o dowload de videos do youtube atraves do python, foi ai que me veio a ideia de fazer esse script para que eu possar fazer o dowload das músicas que gosto do youtube, sem precisar passar pelos diversos sites cheio de anuncios para baixa-la <br>
Ao decorrer deste projeto irei demonstrar com prints e explicações como funciona exatamente o código. </b>
</li>

<h2>Objetivo</h2>
<li> O projeto tem como objetivo demonstrar a utilização do Python para realizar uma interface gráfica simples que realize o dowload de videos do Youtube e converte-los em arquivos.mp3, realizando resumidamente o processo de baixar músicas do youtube</li>

<h2>Bibliotecas Utilizadas </h2>
<blockquote>
    <ul> 
        <li> OS </li> 
        <li> Moviepy.Editor </li>
        <li> Pytube </li> 
        <li> PySimpleGUI </li> 
        <li> re </li> 
    </ul> 
</blockquote>

<h2> Projeto </h2>
Como a ideia do projeto é criar um script python que faça o dowload de uma musica do youtube precisamos primeiramente importar a biblioteca que faça essa etapa.
```python
from pytube import YouTube
```