import gl_gui.gl_gui as gl_gui
import time

gui = gl_gui.GLVisualisation()
gui.init("my window", 400, 400)

theta = 0.0
while True:
    gui.start()
    gui.translate(0.0, 0.0, -3.0)
    gui.rotate(0.0, theta, 0.0)

    gui.push()

    gui.push()
    gui.translate(0.0, 0.0, 0.0)
    gui.paint_textured_rectangle(0.4, 0.4, 5)
    gui.pop()

    gui.push()
    gui.translate(0.0, 0.3, 0.0)
    gui.paint_textured_rectangle(0.4, 0.4, 5)
    gui.pop()

    gui.pop()
    gui.finish()

    theta+= 5.0
    time.sleep(0.05)
    pass
