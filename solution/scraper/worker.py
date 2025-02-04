from redis import Redis
from rq import Worker, Queue

# Conexión manual a Redis
redis = Redis(host='cache', port=6379, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')
queue = Queue('canurl', connection=redis)

# Usamos la conexión de Redis directamente en el Worker
worker = Worker([queue], connection=redis)

# Iniciar el worker
if __name__ == '__main__':
    worker.work()