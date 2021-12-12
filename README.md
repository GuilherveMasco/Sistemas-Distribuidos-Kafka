# Sistemas-Distribuidos-Kafka

## Sistema para coleta e tratamento de tweets utilizando o Apacha Kafka e Zookeeper

### A arquitetura
O Apache Kafka agrega logs de uma forma baseada em mensagens, com fluxos de mensagens sendo definidos por tópicos, onde os produtores podem publicar mensagens. Neste modelo, o tópico escolhido será "Natal", os produtores serão os usuários do Twitter, as publicações serão capturadas e enviadas ao broker e divididas em tópicos (esses particionados). Os consumidores (collector.py), então, irão consumir do tópico com mensagens referentes ao Natal.

![Ilustração da arquitetura utilizada.](/assets/images/arq_tweet.png "Arquitetura utilizada")

A arquitetura geral do Apache permitiria também o uso de múltiplos brokers (servidores), bem como múltiplos tópicos.

![Ilustração da arquitetura genérica do Kafka.](/assets/images/arq.png "Arquitetura genérica do Kafka [1]")

### **IMPORTANTE:** Antes de começar a execução do projeto é necessária a instalação do Apache Kafka na máquina!

### Pacotes necessários antes da execução
Além do Kafka pré instalado, será necessário instalar os pacotes pip, kafka-python, python-twitter, tweepy e default-jre.

> #### Instalação de pacotes:
> - sudo apt install python3-pip
> - pip install kafka-python
> - pip install python-twitter
> - pip install tweepy
> - sudo apt install default-jre

### Inicialização dos servers
Após tudo instalado, é necessário inicializar os servers Zookeeper e Kafka.
> #### Inicialização dos servers Zookeeper e Kafka (disponíveis na pasta de instalação do Kafka):
> - bin/zookeeper-server-start.sh config/zookeeper.properties
> - bin/kafka-server-start.sh config/server.properties

### Criação
> - bin/kafka-topics.sh --create --replication-factor 1 --partitions 1 --topic trump --bootstrap-server localhost:9092
> - bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic quickstart-events --bootstrap-server localhost:9092

### Listagem
> - bin/kafka-topics.sh --bootstrap-server=localhost:9092 --list

### Escrita no Kafka
> - bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092

### Leitura no Kafka
> - bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
> - bin/kafka-console-consumer.sh --topic trump --from-beginning --bootstrap-server localhost:9092

### Coleta de tweets
> - python3 collector.py

### Referências e links importantes
> - <https://kafka.apache.org/30/documentation.html#quickstart>
> - <https://www.bmc.com/blogs/working-streaming-twitter-data-using-kafka/>
> - <https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9>
