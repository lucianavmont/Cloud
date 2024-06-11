import redis
import json

def handle_notification(message):
    ticket_info = json.loads(message['data'])
    print(f'Notificación recibida: Usuario {ticket_info["user_id"]} compró un ticket para {ticket_info["event"]}.')

def subscribe_notifications():
    client = redis.StrictRedis(host='localhost', port=6379, db=0)
    pubsub = client.pubsub()
    pubsub.subscribe('ticket_notifications')
    
    print('Esperando notificaciones de compra de tickets...')
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            handle_notification(message)

if __name__ == "__main__":
    subscribe_notifications()
