# template for "Stopwatch: The Game"
import simplegui

# define global variables
count = 0
player_try = 0
score = 0
stoped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D


def format(count):
    count = int(count)
    minutes = (count // 10)// 60
    whole_sec = count // 10
    amount_sec = whole_sec % 60 
    ten_sec = amount_sec // 10
    sec = amount_sec % 10
    mil_sec = count % 10
    
    #A:BC.D
    
    A = str(minutes)
    B = str(ten_sec)
    C = str(sec)
    D = str(mil_sec)
    
    return A + ":" + B + C + "." + D

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
    
    
def stop():
    global player_try
    global score
    global count
    if count % 10 == 0:
        score +=1
    if timer.is_running():
        player_try += 1
    count = str(count)
    timer.stop()
    return count and player_try and score
    

def reset():
    global count
    global player_try
    global score
    player_try = 0
    count = 0
    score = 0
    return count and player_try and score


# define event handler for timer with 0.1 sec interval

def timer_handler():
    global count
    count = int(count)
    count += 1
    return count


# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(count), (110, 160), 70, "Green")
    canvas.draw_text(str(score), (360, 40), 20, "White")
    canvas.draw_text(("/" + str(player_try)), (370, 40), 20, "White")


    
# create frame

frame = simplegui.create_frame("Timer", 400, 300)

# register event handlers

button1 = frame.add_button('Start', start, 100)
button2 = frame.add_button('Stop', stop, 100)
button3 = frame.add_button('Reset', reset, 100)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)


# start frame

frame.start()

# Please remember to review the grading rubric
