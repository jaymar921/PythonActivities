import threading
def msg():
  print("Just a thread dont mind me")
t = threading.Thread(target=msg)
t.start()