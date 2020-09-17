my_string = "Names: Romeo, Juliet"

step_0 = my_string.split(":")

step_1 = step_0[1]

step_2 = step_1.split(",")

step_3 = [name.strip() for name in step_2]

one_go = [name.strip() for name in my_string.split(":")[1].split(",")]

for idx, item in enumerate([step_0, step_1, step_2, step_3]):
    print("Step {}: {}".format(idx, item))

print("Final result in one go: {}".format(one_go))
