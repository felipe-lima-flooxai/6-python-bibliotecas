import threading
import time
import random

ingressos_disponiveis = 10
lock = threading.Lock()

def comprar_ingresso(cliente_id):
    global ingressos_disponiveis
    time.sleep(random.uniform(0.1, 0.5))
    with lock:
        if ingressos_disponiveis > 0:
            ingressos_disponiveis -= 1
            print(f"Cliente {cliente_id} comprou 1 ingresso. Restam {ingressos_disponiveis}.")
        else:
            print(f"Cliente {cliente_id} tentou comprar, mas os ingressos acabaram.")

threads = []

for i in range(15):
    t = threading.Thread(target=comprar_ingresso, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
