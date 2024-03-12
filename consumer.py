import pika

def on_message_received(channel, method, properties, body):
    message = body.decode('utf-8')
    print(message)

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue as the producer
queue_name = 'order_notifications'
channel.queue_declare(queue=queue_name)

# Listen for messages
channel.basic_consume(queue=queue_name,
                      on_message_callback=on_message_received,
                      auto_ack=True)

print(' [*] Waiting for order notifications. To exit press CTRL+C')
channel.start_consuming()