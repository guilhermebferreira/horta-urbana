# Horta Urbana

Horta Urbana é uma solução para levar as verduras e hortaliças dos produtores locais diretamente para a casa dos consumidores, através de um serviço de assinatura com entregas semanais.

Gerando uma demanda fixa para os produtores locais, diminuindo os desperdício e criando um relacionamento cliente x produtor.

O Horta Urbana foi desenvolvido durante o 2ª Hackaton da Faculdade Católica do Tocantins, cuja tema foram os [17 Objetivos de Desenvolvimento Sustentável da ONU](https://nacoesunidas.org/conheca-os-novos-17-objetivos-de-desenvolvimento-sustentavel-da-onu/) e consquistou o segundo lugar da competição, sendo um projeto transversal, que atacava pelo menos três objetivos globais de uma vez.

- *Objetivo 2:* Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição e promover a agricultura sustentável
- *Objetivo 8:* Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo e trabalho decente para todos
- *Objetivo 12:* Assegurar padrões de produção e de consumo sustentáveis


![Segunda colocação no Hackaton da Faculdade Católica do Tocantins](https://cloud.githubusercontent.com/assets/5393392/25753994/0aeaa386-3194-11e7-8328-648638715c2f.png)

## Instalação do backend

Faça um cópia do projeto

	git clone https://github.com/guilhermebferreira/horta-urbana.git

	cd horta-urbana

Realize a instalação das dependencias

	pip install -r requirements.txt

Sincronixe o banco de dados com as novas migrações, e se for o caso configure um banco de dados diferente em `settings.py`

	python manage.py migrate


## Executando o backend


	python manage.py runserver

A API gera três urls que devem ser utilizadas pelo chatbot

    #URLs utilizadas pelo chatbot
    url(r'^pacotes/$', pacote_list, name='cliente-list'),
    url(r'^pedir/$', criar_pedido, name='criar-pedido'),
    url(r'^status/$', assinatura_status, name='assinatura-status')

- http://127.0.0.1:8000/pedir/
	- Deve ser utilizada para criar a assinatura
	- Caso o user ainda não exista, ele é criado no momento do pedido
	- É gerada uma ordem de pagamento baseada no pacote e na periodicidade escolhida

## Chatbot

Como interface de interação com o usuário final, foi implementado um chatbot

Para acessa-lo vá até a [pagina do Facebook da Horta Urbana](https://www.facebook.com/Horta-Urbana-1295410903900087/?fref=ts), e clique em *Enviar mensagem*

[Link da página do facebok](https://www.facebook.com/Horta-Urbana-1295410903900087/?fref=ts)

[Link direto para a conversa](http://bit.ly/hurbana)

## Links externos

![Apresentação do Horta Urbana](https://cloud.githubusercontent.com/assets/5393392/25754921/60731c86-3197-11e7-9d96-a9df1dd7e715.png)

[Veja os slides utilizados no evento](http://slides.com/guilhermeferreira-2/deck)

[Máteria no site da Católica sobre os resultados do evento](http://www.catolica-to.edu.br/portal/portal/noticia/2679)