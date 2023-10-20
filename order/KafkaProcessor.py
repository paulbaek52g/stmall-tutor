from kafka import KafkaProducer
from flask_kafka import FlaskKafka
from threading import Event
import json
from config import config_reader
from PolicyHandler import wheneverStockIncreased_NotifyToWaitingUsers
from PolicyHandler import wheneverDeliveryReturned_UpdateOrderStatus

class StreamHandler():
	
	def __init__(self):
		INTERRUPT_EVENT = Event()
		config = config_reader.reader()
		self.destination = config['destination']
		self.group_id = config['group_id']
		self.bootstrap_server = config['bootstrap_servers']
		self.producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[self.bootsrap_server], value_serializer=lambda x: json.dumps(x).encode('utf-8'))
		self.consumer = FlaskKafka(INTERRUPT_EVENT,
		         bootstrap_servers=[self.bootstrap_server],
		         group_id= self.group_id
		         )


	def produce(self, msg):
		self.producer.send(self.destination, value=msg)

streamhandler = StreamHandler()

@streamhandler.consumer.handle(streamhandler.destination)
def consume(msg):
    my_json = msg.value.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    if data['eventType'] == "StockIncreased":
        wheneverStockIncreased_NotifyToWaitingUsers(data)
    if data['eventType'] == "DeliveryReturned":
        wheneverDeliveryReturned_UpdateOrderStatus(data)
