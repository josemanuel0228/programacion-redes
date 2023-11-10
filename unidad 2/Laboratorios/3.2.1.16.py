'''
nombre: Jose manuel gutierrez perez
fecha: 9 de noviembre 2023
descripcion  laborartorio: 3.2.1.16
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

    def isempty(self):
       
        return not bool(self.__queue)

class SuperQueue(Queue):

    pass
que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")