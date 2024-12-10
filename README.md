# Digitalização de Dados Analogicos

Este codigo, em python, foi criado com o intuido de Digitalizar um painel de luzes, este painel pertence ao Centro de Lançamento da Barreira do Inferno (CLBI) e atua para checar se todo está funcional para o lançamento de um fogete

Dentro do requirements.txt estão anotadadas as bibliotecas utlizadas no projeto, para instalar use o comando: pip install -r requirements.txt

No script qrreader.py está contido as funções para a extração de dados da imagem do painel, capturada por uma câmera, o cliente.py se comunica com o server.py para mandar dos dados contidos em um array para serem exibidos por um painel montado pelo script painelqr.py utilizando a biblioteca pygame

Para rodar o codigo inicie o servidor e depois o cliente: python server.py e depois python client.py
