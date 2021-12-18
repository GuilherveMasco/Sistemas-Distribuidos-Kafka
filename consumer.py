from kafka import KafkaConsumer

consumer = KafkaConsumer("navidad2", bootstrap_servers=["localhost:9092"], auto_offset_reset="earliest", enable_auto_commit=True, group_id="my-group")

counter = 1
for message in consumer:
	print(str(counter) + message.value.decode("utf-8") + "\n")
	counter = counter + 1
