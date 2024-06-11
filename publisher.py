import redis
import json
import time

def publish_notification(ticket_info):
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    message = json.dumps(ticket_info)
    client.publish('ticket_notifications', message)
    print(f'Notificación publicada: {message}')

if __name__ == "__main__":
    # Simula la compra de un ticket
    ticket_info = {
        'user_id': 123,
        'ticket_id': 456,
        'event': 'Concierto de Rock',
        'purchase_time': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    publish_notification(ticket_info)
