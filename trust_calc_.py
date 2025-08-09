mfr = int(input("Mass Flow Rate: "))
print(mfr, "kg/s")
ve = int(input("Exhaust Velocity: "))
print(ve, "m/s")

Thrust = mfr*ve

if (Thrust > 0):
    print("The required thrust is:", Thrust, "N")
elif (Thrust <= 0):
    print("INVALID INPUT")

