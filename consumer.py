import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notebook.settings")
django.setup()

params = pika.URLParameters('amqps://mcmaaeit:gn6IUolkO-1VI-7ieVW30COo-_Po71RC@sparrow.rmq.cloudamqp.com/mcmaaeit')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='user')


def callback(ch, method, properties, body):
    print('Received in admin')
    # id = json.loads(body)
    print(id)
    # product = Product.objects.get(id=id)
    # product.likes = product.likes + 1
    # product.save()
    print('Product likes increased!')


channel.basic_consume(queue='user', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()
