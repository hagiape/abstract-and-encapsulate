from fan import Fan

fan1 = Fan()
fan2 = Fan()

fan1.set_speed(Fan.FAST)
print("The speed of the fan is " + str(fan1.get_speed()))

fan1.set_radius(10.0)
print("The radius of the fan is " + str(fan1.get_radius()) + " units")

fan1.set_color("yellow")
print("The color of the fan is " + fan1.get_color())

fan1.set_on(True)
if fan1.get_on == True:
    print("The fan is currently on.")
else:
    print("The fan is currently off.")

fan2.set_speed(Fan.MEDIUM)
print("The speed of the fan is " + str(fan2.get_speed()))

fan2.set_radius(5.0)
print("The radius of the fan is " + str(fan2.get_radius()) + " units")

fan2.set_color("blue")
print("The color of the fan is " + fan2.get_color())

fan2.set_on(False)
if fan2.get_on == True:
    print("The fan is currently on.")
else:
    print("The fan is currently off.")
