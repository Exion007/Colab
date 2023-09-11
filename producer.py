from kafka import KafkaProducer
from json import dumps
from time import sleep

topic_name = 'test2'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

for i in range(5):
    data = {"number" : i}
    print(data)
    producer.send(topic_name, value=data)
    sleep(2)
