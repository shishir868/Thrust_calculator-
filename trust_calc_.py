mfr = int(input("Mass Flow Rate: "))
print(mfr)
ve = int(input("Exhaust Velocity: "))
print(ve)

Thrust = mfr*ve

if (Thrust > 0):
    print(Thrust)
elif (Thrust <= 0):
    print("INVALID INPUT")

