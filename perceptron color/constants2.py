import random
from utils import get_luminosity,isBright

LEARNING_RATE = 0.2
ITERATIONS = 50
THRESHOLD = 1.0
SAMPLES = 10
#-----------PYGAME--------------------------------
WIDTH = 300
HEIGHT= 300
BLACK = (0,0,0)
#------------PYGAME END-----------------------------



WEIGHTS = [round(random.uniform(0,1),2) for i in range(4)]

EXAMPLES = [
   [1,random.randint(0,255),random.randint(0,255),random.randint(0,255)]
   for i in range (SAMPLES)
]

OUTPUT = [
    1 if isBright(get_luminosity(EXAMPLES[i][1:])) else 0
    for i in range (SAMPLES)
]
