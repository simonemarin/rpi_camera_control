from _functions import forward, backwards

while True:
  delay = input("Delay between steps (milliseconds)?")
  steps = input("How many steps forward? ")
  motor = input("which motor (0 1)")
  forward(int(delay) / 1000.0, int(steps), int(motor))
  steps = input("How many steps backwards? ")
  backwards(int(delay) / 1000.0, int(steps), int(motor))