import collections # <deque> = double ended queue

class MessageQueue(object):
    def __init__(self, maxSize=6):
        self._queue         = collections.deque()
        self._numUnanswered = 0
        self._maxSize       = maxSize
      
    def sendMessage(self, message):
        self._queue.append(message)
        self._update()
        
    def _update(self):
        while self._queue:
            if self._numUnanswered >= self._maxSize:
                break
            else:
                # The message can be sent
                messageToSend = self._queue.popleft()
                print '>>>', messageToSend    
                self._numUnanswered += 1
              
    def gotAnAnswer(self): 
        # When it receives a message, it tries to send what's left (if possible)...
        self._numUnanswered -= 1                     
        self._update()        
