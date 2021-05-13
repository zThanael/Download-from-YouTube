<h1> Fazer Dowload de músicas através do Python </h1>
<hr>

<h4 align='right'>Para visualizar o arquivo .py <a href='Mp3_Dowloader.py'> Clique aqui </a> </h4>

<h2>Sobre o projeto </h2>
<li> <b>Acredito que algum de vocês já encontraram uma música que está somente no youtube e gostou tanto dela que pretende baixa-la para poder ouvir offline, porém procurando por sites para fazer dowload de músicas, nos deparamos com aqueles inumeros anuncios e diversas etapas que precisam ser feitas para que a gente possa fazer um simples dowload. <br>
Enquanto estava em meus estudos em python verifiquei que era possivel fazer o dowload de vídeos do youtube atraves do python, foi ai que me veio a ideia de fazer esse script para que eu possar fazer o dowload das músicas que gosto do youtube, sem precisar passar pelos diversos sites cheio de anuncios para baixa-la <br>
Ao decorrer deste projeto irei demonstrar com prints e explicações como funciona exatamente o código. </b>
</li>

<h2>Objetivo</h2>
<li> O projeto tem como objetivo demonstrar a utilização do Python para realizar uma interface gráfica simples que realize o dowload de vídeos do Youtube e converte-los em arquivos.mp3, realizando resumidamente o processo de baixar músicas do youtube</li>

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

<h2> Explicação do Projeto </h2>
<h3><li>  Fazer Download do Vídeo do YouTube  </li></h3>
<p>    Como a ideia do projeto é criar um script python que faça o dowload de uma musica do youtube precisamos primeiramente importar a biblioteca que faça essa etapa. <br>
<code> from pytube import YouTube </code>
<br>
Obs: Na primeira vez que formos utilizar uma biblioteca diferente, é necessario fazer a instalação da mesma, para isso é apenas necessário abrir o terminal e digitar
~~~python
pip install pytube 
~~~ <br>
    Agora só precisamos fazer o dowload da musica que queremos, para fazer o dowload pelo python
vamos utilizar os seguintes comandos <br>
<img src='/Imagens/exemplo_pytube.png'>
<br>
onde <b>Youtube(link)</b> é para conectar ao vídeo, sendo link a url do youtube, exemplo: <i> link = 'https://www.youtube.com/exemplo'</i>
<br>
    E é na variavel <code>ys</code> que vamos realizar o download, onde passamos <b>.filter(only_audio=True)</b>
para especificar que desejamos baixar somente o áudio, mesmo o arquivo baixado sendo <i>.mp4</i>. <br>
</b>   Finalizando o código passamos <b>.download(path)</b> que consiste no caminho onde o vídeo será baixado, sendo <b> path </b> uma variavel que armazena a url do arquivo, exemplo: <i> path = 'C:\Exemplo' </i>
<br>
    Se passarmos os links tanto do vídeo quanto do caminho e executarmos esse trecho, receberemos o seguinte 
resultado:
<br><img src='/Imagens/exemplo_musica.mp4.png' width='40px' height='40px'><br>
    Percebam que o arquivo esta em formato de vídeo, caso executem o vídeo, ele tera a tela preta e estará apenas
reproduzindo o áudio da música.