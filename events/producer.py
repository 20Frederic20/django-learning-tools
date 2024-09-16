import pika


def callback(ch, method, properties, body):
    print(f"Received {body}")

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

    print(" [x] Sent 'Hello World!'")
    channel.start_consuming()
