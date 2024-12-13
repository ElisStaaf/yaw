import yaw

yaw.style("style.css")

h1 = yaw.rawhtml("<h1>Hello World!</h1>")
p = yaw.rawhtml("<p>This is a \"Hello World!\" app!</p>")

yaw.ghtml(h1)
yaw.ghtml(p)

yaw.compile("app")
