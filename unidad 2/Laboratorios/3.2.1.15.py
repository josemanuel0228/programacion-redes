'''
nombre: Jose manuel gutierez perez
fecha: 9 de noviembre 2023
descripcion 
laborartorio: 3.2.1.15
'''
class QueueError(Exception):  
    pass
class Queue:
    def __init__(self):
        self.__queue = []  

    def put(self, elem):
      
        self.__queue.append(elem)

    def get(self):
       
        if not self.__queue: 
            raise QueueError("Error de Cola")
        return self.__queue.pop(0)

que = Queue()

try:
    que.put(1)
    que.put("perro")
    que.put(False)
    
    print(que.get())
    print(que.get())
    print(que.get())
    print(que.get())
except QueueError as e:
    print(f"Error de Cola: {e}")