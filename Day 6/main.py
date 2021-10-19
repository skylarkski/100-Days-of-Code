def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_north():
    while not is_facing_north():
        turn_left()

def wall_on_left():
    turn_left

face_north()
        
while not at_goal():
    
    if wall_in_front() and wall_on_right():
        turn_left()
    elif is_facing_north() and wall_in_front() and not wall_on_right():
        turn_right()
        move()
        if front_is_clear():
            move()
    elif front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif front_is_clear() and not wall_on_right():
        turn_right()
        move()
    
