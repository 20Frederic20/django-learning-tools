from django.core.management.base import BaseCommand
import pika


class Command(BaseCommand):
    help = "Consume messages from RabbitMQ"

    def handle(self, *args, **options):
        def callback(ch, method, properties, body):
            print(f"Received {body}")

        credentials = pika.PlainCredentials("guest", "guest")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                "rabbitmq",
                5672,
                "/",
                credentials,
            )
        )
        channel = connection.channel()

        channel.queue_declare(queue="your_queue")

        channel.basic_consume(
            queue="your_queue", on_message_callback=callback, auto_ack=True
        )

        print("Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
