import sys
import time
import os
import random

try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print "Please set MODIM_HOME environment variable to MODIM folder."
    sys.exit(1)

# Set MODIM_IP to connnect to remote MODIM server

import ws_client
from ws_client import *


def i1():

    im.init()

    q = im.ask('help')  # wait for button

    if (q=='yes'):
        a = im.ask('help_option')

        if (a!='timeout'):
            if (a=='direction'):
                im.display.loadUrl('pin.html') 
                im.execute('pin')
            else:   
                if (a=='advertisement'):
                    im.display.loadUrl('ad.html') 
                    ans = im.ask('ad')
                    if (ans=='finish'):
                        im.display.loadUrl('slide.html')
                        im.execute('goodbye')
                else:
                    im.display.loadUrl('slide.html') 
                    im.execute('shop')
                    time.sleep(4)
                    im.execute('goodbye')

                time.sleep(2)
                im.display.loadUrl('index.html')
        else:
            im.init()

    else:
        im.init()


if __name__ == "__main__":

    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)

    mws.run_interaction(i1)


