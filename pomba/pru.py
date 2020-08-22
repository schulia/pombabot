import random 

def _random_pru():
  return  ['Prrrru', 'Pru!', 'pru?','pRuu','pruu','pruuu', 'pru pru', 'pru pruu', 'pru pru pru ?','!urP']

def makepru ():
  prus = _random_pru()
  # prus.remove(last_tweet)
  return prus[(random.randint(0,(len(prus) -1) ))]
  