print('For credits see credits.txt')
import requests,json,threading,random,time
import logging
import threading
import time
print('Player Follow bot by FAVEISH!!BECOME LIKE FOLLOWALL!!PLEASE FOLLOW MY ACCOUNT IF YOU USED THIS!!!!\n Make sure to add some proxies or it won''t work at all.')
proxies=open('proxies.txt')
proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]
ses = requests.session()
cookie = open('cookie').read()
ses.cookies['.ROBLOSECURITY'] = cookie
r = ses.post('https://auth.roblox.com/')
x = r.headers['x-csrf-token']
print(x)
global id
id = 11111
def gfol():
  global id
  global f
  try:
   print('[Faveish]==>Following' +' '+ str(id))
   url = 'https://friends.roblox.com/v1/users/' + str(id) + '/follow'
   f = ses.post(url,{'targetUserId':id},headers=r.headers,proxies=random.choice(proxies))
   id = id + 1
  except:
    print('Bad proxy.')
    id = id
  print(f.text)
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
while True:
 time.sleep(1)
 x = threading.Thread(target=gfol, args=())
 x.start()
