# Freezer-Infinito
Projeto desenvolvido para o BRASA Hacks 2020 - trilha Ambev.

O MVP realizado para o desafio consiste em uma interface gráfica programada em linguagem Python, onde é possível realizar a gestão dos clientes de Autos Serviços para as cidades em que o Zé Delivery atua, com a finalidade de gerar um QRcode para cada Auto Serviço.

![GitHub Logo](/images/interface_mvp.png)

No MVP realizado o QRcode direciona para o site do Zé Delivery. O Zé Delivery então receberia os dados referentes aos Auto Serviços e retorna dados sobre a disponibilidade dos produtos. Os dados são então enviados a um site onde se pode visualizar a indisponibilidade das cervejas em cada ponto de venda.

Para o desafio, como não temos acesso aos dados do Zé Delivery, os dados dos charts disponíveis no site foram criados e podem ser atualizados por um google sheets.

Link do site para análise dos dados:
https://sites.google.com/view/equipe-7

Link do vídeo:
https://www.youtube.com/watch?v=4CTg4hWMhvA&feature=youtu.be

Link do Product Hunt:
https://www.producthunt.com/posts/freezer-infinito

## Install

Instale as seguintes dependências para rodar o programa.

```
pip install qrcode
```
```
pip install pandas
```
```
pip install path
```

O programa foi testado e funcionou corretamente com as versões Python 3.7.4, pyqrcode 1.2.1, pandas 0.25.3, path 13.1.0.  
