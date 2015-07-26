#<=============== Stopwatch: The Game! =================>

import simplegui

# Global Variables!
interval = 100
width = 300
height = 200
t = 0
click = 0
success = 0
message = '0:00:0'
isRunning = False

#<=============== Helper Function Zone =================>
def format(t):
    mins = t / 600
    secs = (t % 600) / 10
    if secs < 10:
        secstr = '0' + str(secs)
    else:
        secstr = str(secs)
    tens = (t % 600) % 10
    global message
    message = str(mins) + ":" + secstr + "." + str(tens)
    global points
    
    
#<=============== Event Handler Zone =================>
def start():
    timer.start()
    global isRunning
    isRunning = True

    
def stop():
    global isRunning
    
    if isRunning:
        global click
        click = click + 1
        
    if isRunning and (t % 600) % 10 == 0:
        global success
        success = success + 1
        
    timer.stop()
    isRunning = False
    
    
def reset():
    global t
    global success
    global click
    t = 0
    success = 0
    click = 0
    timer.stop
    

def tick():
    global t
    t = t + 1

#<=============== Draw Handler Zone =================>
def draw(canvas):
    format(t)
    canvas.draw_text(message, [100, 115], 36, "white")
    canvas.draw_text(str(success) + "/" + str(click), [220, 35], 30, "green")
    
#<=================== Frame Zone ====================>
frame = simplegui.create_frame("Stopwatch Game", width, height)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(interval, tick)

#<==================== Start Zone ====================>
frame.start()



