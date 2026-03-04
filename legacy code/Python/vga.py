import pyglet
import time
import sys

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
print screen
window = pyglet.window.Window(None, None, sys.argv[0], False, 0, True, True, True, display, screen, None, None)
image = pyglet.resource.image('400-400-72.jpg')
image = image.get_transform(True, False, 0)
@window.event
def on_draw():
    window.clear()
    image.blit(950,50)
pyglet.app.run()



time.sleep(3)
window.close()
pyglet.app.exit()




