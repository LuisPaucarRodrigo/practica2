from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('pruebadocker', b'Hola mundo mi nombre es luis')
producer.flush()