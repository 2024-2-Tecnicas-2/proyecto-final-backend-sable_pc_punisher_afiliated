from django.core.management.base import BaseCommand
from queue import Queue
from login.models import Order


class Command(BaseCommand):
    help = 'Gestión de pedidos usando una cola'

    def handle(self, *args, **kwargs):
        # Crear una cola para manejar los pedidos
        cola_pedidos = Queue()

        # Obtener todos los pedidos pendientes ordenados por fecha
        pedidos_pendientes = Order.objects.filter(status='Pd').order_by('creationDate')

        # Agregar los pedidos a la cola
        for pedido in pedidos_pendientes:
            cola_pedidos.put(pedido)

        self.stdout.write("Pedidos pendientes cargados en la cola.")
        self.stdout.write("¿Qué deseas hacer?")
        self.stdout.write("1. Mostrar el próximo pedido a procesar")
        self.stdout.write("2. Procesar un pedido")
        self.stdout.write("3. Salir")

        while not cola_pedidos.empty():
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                # Mostrar el próximo pedido (sin procesarlo)
                pedido = cola_pedidos.queue[0]  # Ver el primero sin eliminarlo
                self.stdout.write(f"Próximo pedido:\nID: {pedido.id}, Cliente: {pedido.client}, Total: {pedido.finalPrice}")
            elif opcion == "2":
                # Procesar el próximo pedido
                pedido = cola_pedidos.get()  # Eliminar el pedido de la cola
                self.stdout.write(f"Procesando pedido ID: {pedido.id} del cliente {pedido.client}")
                pedido.status = 'Ev'  # Cambiar estado a "Enviado"
                pedido.save()
                self.stdout.write("Pedido procesado y actualizado.")
            elif opcion == "3":
                self.stdout.write("Saliendo del gestor de pedidos.")
                break
            else:
                self.stdout.write("Opción no válida. Inténtalo de nuevo.")

        if cola_pedidos.empty():
            self.stdout.write("Todos los pedidos han sido procesados.")
