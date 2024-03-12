import pika

def send_order_confirmation(order_id):
    message = f'Your order #{order_id} has been confirmed!'
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message)
    print(f" [*] Sent '{message}'")

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'order_notifications'
channel.queue_declare(queue=queue_name)

try:
    while True:
        order_id = input("Enter an order number. To exit press CTRL+C\n")
        send_order_confirmation(order_id)
finally:
    # Disconnect gracefully
    connection.close()
    print("\nConnection closed.")