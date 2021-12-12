# Sistemas-Distribuidos-Kafka

## Sistema para coleta e tratamento de tweets utilizando o Apacha Kafka e Zookeeper

### A arquitetura
O Apache Kafka agrega logs de uma forma baseada em mensagens, com fluxos de mensagens sendo definidos por tópicos, onde os produtores podem publicar mensagens.

Neste modelo, o tópico escolhido será "Natal" (Navidad, em espanhol). Haverá um produtor (collector.py), o qual coletará dados do Twitter e as inserirá no broker do Kafka. Serão capturadas 100 publicações contendo a palavra "navidad" e serão submetidas ao tópico "navidad" (o qual contém uma partição). O consumidor (consumer.py), então, irá consumir do tópico e as imprimir, simulando um processamento das informações obtidas da plataforma.

A arquitetura geral do Apache permitiria também o uso de múltiplos brokers (servidores), bem como múltiplos tópicos.

![Exemplo de uma arquitetura do Kafka.](/assets/images/arq.PNG "Exemplo de uma arquitetura do Kafka [1]")

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

### Executando scripts
#### Produtor: Coleta de tweets
> - python3 collector.py

#### Consumidor: Processando dados através do Kafka
> - python3 consumer.py

### Referências e links importantes
> - [1]<http://notes.stephenholiday.com/Kafka.pdf>
> - [2]<https://kafka.apache.org/30/documentation.html#quickstart>
> - [3]<https://www.bmc.com/blogs/working-streaming-twitter-data-using-kafka/>
> - [4]<https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9>
> - [5]<https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1>
