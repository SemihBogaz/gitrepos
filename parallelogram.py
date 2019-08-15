def left_slash(num):
    for i in range(int(num)):
        print("\\", end="")


def right_slash(num):
    for i in range(int(num)):
        print("/", end="")


def jump_line(num):
    for i in range(int(num)):
        print()


def space(num):
    for i in range(int(num)):
        print(" ", end="")


def upper_part(diameter):
    start_spc=diameter/2-1
    for i in range(int(diameter/2)):
        space(start_spc-i)
        right_slash(1)
        space(i*2)
        left_slash(1)
        jump_line(1)


def lower_part(diameter):
    for i in range(int(diameter/2)):
        space((0+1)*i)
        left_slash(1)
        space(diameter-(i+1)*2)
        right_slash(1)
        jump_line(1)

#  what tutor does is ...
#      start_space=diameter/2
#     for i in range(int(diameter / 2)):
#         space(i)
#         left_slash(1)
#         space(start_space- i * 2)
#         right_slash(1)
#         jump_line(1)


def parallelogram(diameter):
    upper_part(diameter)
    lower_part(diameter)


parallelogram(20)
