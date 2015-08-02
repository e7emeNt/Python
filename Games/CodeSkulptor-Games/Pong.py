#<====================== Pong!!! ========================>

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_vel = 0
paddle2_vel = 0

paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [(WIDTH - 1 - HALF_PAD_WIDTH), HEIGHT / 2]

rainbows_and_unicorns = False


#<=============== Helper Function Zone =================>
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
    if direction == LEFT:
        ball_vel[0] = -ball_vel[0]
    

#<================ Event Handler Zone ==================>
def new_game():
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, rainbows_and_unicorns
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 10, "White", "White")
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) -  BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
           
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel == 0
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos[1] <= HALF_PAD_HEIGHT:
        paddle1_vel == 0
        paddle1_pos[1] = HALF_PAD_HEIGHT

    if paddle2_pos[1] >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_vel == 0
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos[1] <= HALF_PAD_HEIGHT:
        paddle2_vel == 0
        paddle2_pos[1] = HALF_PAD_HEIGHT
    
    # nothing to see here!
    if rainbows_and_unicorns:
        ball_vel[0] += 0.1
        
    # determine whether the ball touches the gutters or paddle and ball collide    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    elif ball_pos[0] >= (WIDTH - 1) - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], 
                     [paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],
                     PAD_WIDTH, "White") 
    
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], 
                     [paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],
                     PAD_WIDTH, "White") 
    
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel

    # draw scores
    canvas.draw_text(str(score1), (WIDTH * 1/4, HEIGHT * 1/4), 40, "White")
    canvas.draw_text(str(score2), (WIDTH * 3/4, HEIGHT * 1/4), 40, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, rainbows_and_unicorns
    vel = 8
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    if key == simplegui.KEY_MAP["q"]:
        rainbows_and_unicorns = True

def keyup(key):
    global paddle1_vel, paddle2_vel, rainbows_and_unicorns
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["q"]:
        rainbows_and_unicorns = False


#<==================== Frame Zone ======================>
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


#<====================== Start Zone =====================>
new_game()
frame.start()
