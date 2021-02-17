import pico
from pico import PicoApp

@pico.expose()
def hello(who="world"):
    s = "hello %s!" % who
    return s


@pico.expose()
def goodbye(who):
    s = "goodbye %s!" % who
    return s


app = PicoApp()
app.register_module(__name__)
