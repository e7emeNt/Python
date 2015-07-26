# implementation of card game - Memory

import simplegui
import random

turns=0
state=0
remains=16
last1=0
last2=0
cards=range(8)+range(8)
cover=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
position=[[150,150],[250,150],[350,150],[450,150],
          [150,250],[250,250],[350,250],[450,250],
          [150,350],[250,350],[350,350],[450,350],
          [150,450],[250,450],[350,450],[450,450]]
velo=[[0,0],[0,0],[0,0],[0,0],
     [0,0],[0,0],[0,0],[0,0],
     [0,0],[0,0],[0,0],[0,0],
     [0,0],[0,0],[0,0],[0,0]]

# helper function to initialize globals
def new_game():
    global cards,turns,cover,remains,state,position
    cards=range(8)+range(8)
    random.shuffle(cards)
    random.shuffle(cards)
    cover=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    turns=0
    position=[[150,150],[250,150],[350,150],[450,150],
          [150,250],[250,250],[350,250],[450,250],
          [150,350],[250,350],[350,350],[450,350],
          [150,450],[250,450],[350,450],[450,450]]
    remains=16
    state=0
    label.set_text("Turns = "+str(turns))
    pass  

     
# define event handlers
def hard_mode():
    global velo
    for x in xrange(16):
        velo[x][0]=random.randrange(1,4)
        velo[x][1]=random.randrange(1,4)
        if x/4<=2:
            velo[x][1]=-velo[x][1]
        if x%4<=2:
            velo[x][0]=-velo[x][0]
    new_game()
    pass

def normal_mode():
    global velo
    for x in xrange(16):
        velo[x][0]=0
        velo[x][1]=0
    new_game()
    pass    

def mouseclick(pos):
    # add game state logic here
    global state,turns,last1,last2,remains

    for x in xrange(16):
        if pos[0]>position[x][0]-40 and pos[0]<position[x][0]+40 and pos[1]>position[x][1]-40 and pos[1]<position[x][1]+40 and cover[x]==0:
            cover[x]=1
            if state==0:
                state=1
            elif state==1:
                if cards[last1]==cards[x]:
                    remains-=2
                turns+=1
                label.set_text("Turns = "+str(turns))
                state=2
            else:
                if cards[last2]!=cards[last1]:
                    cover[last1]=0
                    cover[last2]=0
                state=1
            last2=last1
            last1=x
            break
    pass    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global remains

    for x in xrange(16):
        i=15-x
        if cover[i]==1:
            canvas.draw_polygon([[position[i][0]-40,position[i][1]-40], [position[i][0]-40,position[i][1]+40], [position[i][0]+40,position[i][1]+40], [position[i][0]+40,position[i][1]-40]], 5, 'Black', 'Black')
            canvas.draw_text(str(cards[i]), [position[i][0]-15,position[i][1]+15], 40, 'White')
            canvas.draw_image(pics[cards[i]],(50,50),(100,100),position[i],(80,80))
        else:
            canvas.draw_polygon([[position[i][0]-40,position[i][1]-40], [position[i][0]-40,position[i][1]+40], [position[i][0]+40,position[i][1]+40], [position[i][0]+40,position[i][1]-40]], 5, 'Black', 'Black')
            canvas.draw_text('?', [position[i][0]-15,position[i][1]+15], 40, 'White')
            canvas.draw_image(no_pic,(50,50),(100,100),position[i],(80,80))
    if remains==0:
        canvas.draw_polygon([[0,50],[0,90],[599,90],[599,50]],1,"blue","blue")
        canvas.draw_text("You win!", (260,80), 24, "white")

    for x in xrange(16):
        if cover[x]==0:
            position[x][0]+=velo[x][0]
            position[x][1]+=velo[x][1]
            if position[x][0]>510 or position[x][0]<90:
                velo[x][0]=-velo[x][0]
            elif position[x][1]>510 or position[x][1]<90:
                velo[x][1]=-velo[x][1]
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 600, 600)
frame.set_canvas_background("white")
frame.add_button("Reset_Normal", normal_mode)
frame.add_button("Reset_Hard", hard_mode)
label = frame.add_label("Turns = "+str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
pics=range(8)
for x in xrange(8):
    pics[x]=simplegui.load_image("http://qfqin.com/python/memory/"+str(x)+".png")
no_pic=simplegui.load_image("http://qfqin.com/python/memory/none.png")

new_game()
frame.start()


# Always remember to review the grading rubric