

def handle_gravity(gravity, object_y, lowest_point):
    if (gravity + object_y > lowest_point):
        return lowest_point
    else:
        return object_y+gravity
    
def handle_jumping(object_y):
    return object_y - 25