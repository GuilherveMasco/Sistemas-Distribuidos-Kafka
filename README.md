# Sistemas-Distribuidos-Kafka

## Sistema para coleta e tratamento de tweets utilizando o Apacha Kafka e Zookeeper

### A arquitetura
O Apache Kafka agrega logs de uma forma baseada em mensagens, com fluxos de mensagens sendo definidos por tópicos, onde os produtores podem publicar mensagens.

No exemplo de execução, o tópico escolhido será "Natal" (Navidad, em espanhol). Haverá um produtor (collector.py), o qual coletará dados do Twitter e as inserirá no broker do Kafka. Serão capturadas 100 publicações contendo a palavra "navidad" e serão submetidas ao tópico "navidad" (o qual contém uma partição). O consumidor (consumer.py), então, irá consumir do tópico e as imprimir, simulando um processamento das informações obtidas da plataforma.

Também é proposta uma aplicação que gerencia a criação e exclusão de tópicos, bem como a leitura de mensagens. Essa aplicação foi desenvolvida utilizando a arquitetura cliente-servidor e disponibiliza uma API que pode ser acessada através de um socket TCP. Abaixo segue a imagem que ilustra essa arquitetura. A documentação da API pode ser acessada pelo link [Documentação da API](doc/api_documentation.pdf).

![Arquitetura da aplicação proposta](/doc/architeture.png "Arquitetura da aplicação proposta")


### **IMPORTANTE:** Antes de começar a execução do projeto é necessário que você tenha uma versão Apache Kafka na sua máquina!

Baixe e descompacte o Kafka em sua máquina através do link: <https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz>.

### Pacotes necessários antes da execução
Além do Kafka pré instalado, será necessário instalar os pacotes *pip*, *kafka-python*, *python-twitter*, *tweepy* e *default-jre*.

> #### Instalação de pacotes:
> - sudo apt install python3-pip
> - pip install kafka-python
> - pip install python-twitter
> - pip install tweepy
> - sudo apt install default-jre

### Iniciando o Kafka (linha de comando)
#### Inicialização dos servers
Após tudo instalado, é necessário inicializar os servers Zookeeper e Kafka.
> #### Inicialização dos servers Zookeeper e Kafka (disponíveis na pasta de instalação do Kafka):
> - bin/zookeeper-server-start.sh config/zookeeper.properties
> - bin/kafka-server-start.sh config/server.properties

#### Criação do tópico
> - bin/kafka-topics.sh --create --replication-factor 1 --partitions 1 --topic navidad --bootstrap-server localhost:9092

#### Listagem dos tópicos criados
> - bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list

#### Submetendo dados no tópico
> - bin/kafka-console-producer.sh --topic navidad --bootstrap-server localhost:9092

#### Lendo dados do tópico
> - bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
> - bin/kafka-console-consumer.sh --topic trump --from-beginning --bootstrap-server localhost:9092

### Executando scripts de teste
#### Produtor: Coleta de tweets
> - python3 collector.py

#### Consumidor: Processando dados através do Kafka
> - python3 consumer.py

### Executando a aplicação proposta
Para executar o servidor da aplicação proposta você deve utilizar o comando abaixo:
> - python3 ./api/server.py

A comunicação com o servidor está descrita em [Documentação da API](doc/api_documentation.pdf). Abaixo seguem alguns exemplos:
> - python3 ./api/manager.py create_topic natal 1
> - python3 ./api/manager.py delete_topic natal
> - python3 ./api/client.py subscribe_topic natal

### Referências e links importantes
> - [1]<http://notes.stephenholiday.com/Kafka.pdf>
> - [2]<https://kafka.apache.org/30/documentation.html#quickstart>
> - [3]<https://www.bmc.com/blogs/working-streaming-twitter-data-using-kafka/>
> - [4]<https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9>
> - [5]<https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1>
