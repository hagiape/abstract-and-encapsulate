from fan import Fan

fan1 = Fan()
fan2 = Fan()

fan1.set_speed(Fan.FAST)
print("The fan speed is " + str(fan1.get_speed()))

fan1.set_radius(10.0)
print("The fan speed is " + str(fan1.get_radius()))

fan1.set_color("yellow")
print("The color of the fan is " + fan1.get_color())

fan1.set_on(True)
if fan1.get_on == True:
    print("The fan is currently on.")
else:
    print("The fan is currently off.")