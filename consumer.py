from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers="kafka",
                         group_id=None,
                         consumer_timeout_ms=500,
                         auto_offset_reset='earliest')
consumer.subscribe(['dbserver1.inventory.customers'])

for msg in consumer:
    print(msg)

