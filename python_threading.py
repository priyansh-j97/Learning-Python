import threading

class messenger(threading.Thread):
    def run(self):
        for _ in range(10): #we can write "_" instead of assigning any variable for looping, if we only want the loop to run a certain number of times
            print(threading.currentThread().getName())

m=messenger(name='Sending message...')
n=messenger(name='Receiving message...')

m.start() #this is the way of calling the run() method
n.start()