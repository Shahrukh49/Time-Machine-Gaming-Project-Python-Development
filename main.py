import RPi.GPIO as GPIO
import pygame
import datetime
import time as tm
import sys

#sensor pins
trig1, echo1 = 7,12
trig2, echo2 = 13,16
trig3, echo3 = 15,18
trig4, echo4 = 29,32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(trig1,GPIO.OUT)
GPIO.setup(trig2,GPIO.OUT)
GPIO.setup(trig3,GPIO.OUT)
GPIO.setup(trig4,GPIO.OUT)
GPIO.setup(echo1,GPIO.IN)
GPIO.setup(echo2,GPIO.IN)
GPIO.setup(echo3,GPIO.IN)
GPIO.setup(echo4,GPIO.IN)

GPIO.output(trig1, 0)
GPIO.output(trig1, 0)
GPIO.output(trig1, 0)
GPIO.output(trig1, 0)


pygame.init()

clock = pygame.time.Clock()

Screen1 = True
blink = False

white = (255,255,255)
display_width = 1920
display_height = 1080

date_g = input('Enter Date for Present time i.e. YYYY-MM-DD = ')
date_g = date_g.split('-')

gameDisplay = pygame.display.set_mode((display_width, display_height),pygame.FULLSCREEN)
pygame.display.set_caption('Time Machine')

am_o = pygame.image.load('am_o.png')
pm_o = pygame.image.load('pm_o.png')
am_g = pygame.image.load('am_g.png')
pm_g = pygame.image.load('pm_g.png')
am_y = pygame.image.load('am_y.png')
pm_y = pygame.image.load('pm_y.png')

jan_o = pygame.image.load('jan_o.png')
feb_o = pygame.image.load('feb_o.png')
mar_o = pygame.image.load('mar_o.png')
apr_o = pygame.image.load('apr_o.png')
may_o = pygame.image.load('may_o.png')
jun_o = pygame.image.load('jun_o.png')
jul_o = pygame.image.load('jul_o.png')
aug_o = pygame.image.load('aug_o.png')
sep_o = pygame.image.load('sep_o.png')
oct_o = pygame.image.load('oct_o.png')
nov_o = pygame.image.load('nov_o.png')
dec_o = pygame.image.load('dec_o.png')

jan_g = pygame.image.load('jan_g.png')
feb_g = pygame.image.load('feb_g.png')
mar_g = pygame.image.load('mar_g.png')
apr_g = pygame.image.load('apr_g.png')
may_g = pygame.image.load('may_g.png')
jun_g = pygame.image.load('jun_g.png')
jul_g = pygame.image.load('jul_g.png')
aug_g = pygame.image.load('aug_g.png')
sep_g = pygame.image.load('sep_g.png')
oct_g = pygame.image.load('oct_g.png')
nov_g = pygame.image.load('nov_g.png')
dec_g = pygame.image.load('dec_g.png')

jan_y = pygame.image.load('jan_y.png')
feb_y = pygame.image.load('feb_y.png')
mar_y = pygame.image.load('mar_y.png')
apr_y = pygame.image.load('apr_y.png')
may_y = pygame.image.load('may_y.png')
jun_y = pygame.image.load('jun_y.png')
jul_y = pygame.image.load('jul_y.png')
aug_y = pygame.image.load('aug_y.png')
sep_y = pygame.image.load('sep_y.png')
oct_y = pygame.image.load('oct_y.png')
nov_y = pygame.image.load('nov_y.png')
dec_y = pygame.image.load('dec_y.png')

background_image = pygame.image.load('background3.png')

f_o = pygame.image.load('F_o.png')
f_g = pygame.image.load('F_g.png')
f_y = pygame.image.load('F_y.png')

y_f_o = pygame.image.load('y_F_o.png')
y_f_g = pygame.image.load('y_F_g.png')
y_f_y = pygame.image.load('y_F_y.png')

o0 = pygame.image.load('0o.png')
o1 = pygame.image.load('1o.png')
o2 = pygame.image.load('2o.png')
o3 = pygame.image.load('3o.png')
o4 = pygame.image.load('4o.png')
o5 = pygame.image.load('5o.png')
o6 = pygame.image.load('6o.png')
o7 = pygame.image.load('7o.png')
o8 = pygame.image.load('8o.png')
o9 = pygame.image.load('9o.png')

g0 = pygame.image.load('0g.png')
g1 = pygame.image.load('1g.png')
g2 = pygame.image.load('2g.png')
g3 = pygame.image.load('3g.png')
g4 = pygame.image.load('4g.png')
g5 = pygame.image.load('5g.png')
g6 = pygame.image.load('6g.png')
g7 = pygame.image.load('7g.png')
g8 = pygame.image.load('8g.png')
g9 = pygame.image.load('9g.png')

y0 = pygame.image.load('0y.png')
y1 = pygame.image.load('1y.png')
y2 = pygame.image.load('2y.png')
y3 = pygame.image.load('3y.png')
y4 = pygame.image.load('4y.png')
y5 = pygame.image.load('5y.png')
y6 = pygame.image.load('6y.png')
y7 = pygame.image.load('7y.png')
y8 = pygame.image.load('8y.png')
y9 = pygame.image.load('9y.png')

t_o = pygame.image.load('t_o.png')
t_g = pygame.image.load('t_g.png')
t_y = pygame.image.load('t_y.png')

date_o = [0,0,0,0]

def sensor_read(sensor_num):
    GPIO.output(trig1, 1)
    tm.sleep(0.002)
    GPIO.output(trig1, 0)
    while GPIO.input(echo1) == 0:
        pass
    start_S1 = tm.time()
    while GPIO.input(echo1) == 1:
        pass
    stop_S1 = tm.time()

    t1 = (stop_S1 - start_S1)/2
    
    GPIO.output(trig2, 1)
    m.sleep(0.002)
    GPIO.output(trig2, 0)
    while GPIO.input(echo2) == 0:
        pass
    start_S2 = tm.time()
    while GPIO.input(echo2) == 1:
        pass
    stop_S2 = tm.time()

    t2 = (stop_S2 - start_S2)/2
    
    GPIO.output(trig3, 1)
    m.sleep(0.002)
    GPIO.output(trig3, 0)
    while GPIO.input(echo3) == 0:
        pass
    start_S3 = tm.time()
    while GPIO.input(echo3) == 1:
        pass
    stop_S3 = tm.time()

    t3 = (stop_S3 - start_S3)/2

    GPIO.output(trig4, 1)
    m.sleep(0.002)
    GPIO.output(trig4, 0)
    while GPIO.input(echo4) == 0:
        pass
    start_S4 = tm.time()
    while GPIO.input(echo4) == 1:
        pass
    stop_S4 = tm.time()

    t4 = (stop_S4 - start_S4)/2

    dist1 = 34000*t1
    dist2 = 34000*t2
    dist3 = 34000*t3
    dist4 = 34000*t4

    return dist1, dist2, dist3, dist4
    
def map_value(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

max_d1, max_d2, max_d3, max_d4 = sensor_read()

while Screen1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    #sensors 
    d1, d2, d3, d4 = sensor_read()

    date_o[0] = str(map_value(d1,20,max_d1,1,31))
    date_o[1] = map_value(d2,20,max_d2,1,12)
    date_o[2] = str(map_value(d3,20,max_d3,0,99))
    date_o[3]= str(map_value(d4,20,max_d4,0,99))

    #backend
    date_time = (str(datetime.datetime.now())).split()
    date = (date_time[0]).split('-')
    time = (date_time[1]).split(':')

    gameDisplay.fill(white)
    gameDisplay.blit(background_image,(0, 0))

    gameDisplay.blit(f_o,(189+350,96+8))
    gameDisplay.blit(f_g,(189+350,464+8))
    gameDisplay.blit(f_y,(189+350,843+8))
    gameDisplay.blit(y_f_o,(189+650,96+8))
    gameDisplay.blit(y_f_g,(189+650,464+8))
    gameDisplay.blit(y_f_y,(189+650,843+8))
    gameDisplay.blit(f_o,(189+650+500,96+8))
    gameDisplay.blit(f_g,(189+650+500,464+8))
    gameDisplay.blit(f_y,(189+650+500,843+8))
    gameDisplay.blit(f_o,(189+650+500+270,96+8))
    gameDisplay.blit(f_g,(189+650+500+270,464+8))
    gameDisplay.blit(f_y,(189+650+500+270,843+8))

    #MONTH ###############
    if date[1] == '01':
              #gameDisplay.blit(jan_o,(189,96))
              #gameDisplay.blit(jan_g,(189,464))
              gameDisplay.blit(jan_y,(189,843))
    elif date[1] == '02':
              #gameDisplay.blit(feb_o,(189,96))
              #gameDisplay.blit(feb_g,(189,464))
              gameDisplay.blit(feb_y,(189,843))
    elif date[1] == '03':
              #gameDisplay.blit(mar_o,(189,96))
              #gameDisplay.blit(mar_g,(189,464))
              gameDisplay.blit(mar_y,(189,843))
    elif date[1] == '04':
              #gameDisplay.blit(apr_o,(189,96))
              #gameDisplay.blit(apr_g,(189,464))
              gameDisplay.blit(apr_y,(189,843))
    elif date[1] == '05':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(may_y,(189,843))
    elif date[1] == '06':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(jun_y,(189,843))
    elif date[1] == '07':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(jul_y,(189,843))
    elif date[1] == '08':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(aug_y,(189,843))
    elif date[1] == '09':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(sep_y,(189,843))
    elif date[1] == '10':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(oct_y,(189,843))
    elif date[1] == '11':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(nov_y,(189,843))
    elif date[1] == '12':
              #gameDisplay.blit(may_o,(189,96))
              #gameDisplay.blit(may_g,(189,464))
              gameDisplay.blit(dec_y,(189,843))
              
    if date_g[1] == '01':
        gameDisplay.blit(jan_g,(189,464))
    elif date_g[1] == '02':
        gameDisplay.blit(feb_g,(189,464))
    elif date_g[1] == '03':
        gameDisplay.blit(mar_g,(189,464))
    elif date_g[1] == '04':
        gameDisplay.blit(apr_g,(189,464))
    elif date_g[1] == '05':
        gameDisplay.blit(may_g,(189,464))
    elif date_g[1] == '06':
        gameDisplay.blit(jun_g,(189,464))
    elif date_g[1] == '07':
        gameDisplay.blit(jul_g,(189,464))
    elif date_g[1] == '08':
        gameDisplay.blit(aug_g,(189,464))
    elif date_g[1] == '09':
        gameDisplay.blit(sep_g,(189,464))
    elif date_g[1] == '10':
        gameDisplay.blit(oct_g,(189,464))
    elif date_g[1] == '11':
        gameDisplay.blit(nov_g,(189,464))
    elif date_g[1] == '12':
        gameDisplay.blit(dec_g,(189,464))

    if date_o[0] == 1:
        gameDisplay.blit(jan_o,(189,96))
    elif date_o[0] == 2:
        gameDisplay.blit(feb_o,(189,96))
    elif date_o[0] == 3:
        gameDisplay.blit(mar_o,(189,96))
    elif date_o[0] == 4:
        gameDisplay.blit(apr_o,(189,96))
    elif date_o[0] == 5:
        gameDisplay.blit(may_o,(189,96))
    elif date_o[0] == 6:
        gameDisplay.blit(jun_o,(189,96))
    elif date_o[0] == 7:
        gameDisplay.blit(jul_o,(189,96))
    elif date_o[0] == 8:
        gameDisplay.blit(aug_o,(189,96))
    elif date_o[0] == 9:
        gameDisplay.blit(sep_o,(189,96))
    elif date_o[0] == 10:
        gameDisplay.blit(oct_o,(189,96))
    elif date_o[0] == 11:
        gameDisplay.blit(nov_o,(189,96))
    elif date_o[0] == 12:
        gameDisplay.blit(dec_o,(189,96))


    # AM / PM ##########
    hour = int(time[0])
    if hour < 12:
        gameDisplay.blit(am_o,(1234,110))
        gameDisplay.blit(am_g,(1234,479))
        gameDisplay.blit(am_y,(1234,856))
    else:
        gameDisplay.blit(pm_o,(1234,110))
        gameDisplay.blit(pm_g,(1234,479))
        gameDisplay.blit(pm_y,(1234,856))

    #YEAR ###############
    year_o_1 = pygame.image.load(date_o[2][0]+'o.png')
    gameDisplay.blit(year_o_1,(189+650,96+8))
    year_g_1 = pygame.image.load(date_g[0][0]+'g.png')
    gameDisplay.blit(year_g_1,(189+650,464+8))
    year_y_1 = pygame.image.load(date[0][0]+'y.png')
    gameDisplay.blit(year_y_1,(189+650,843+8))

    year_o_2 = pygame.image.load(date_o[2][1]+'o.png')
    gameDisplay.blit(year_o_2,(189+650+84,96+8))
    year_g_2 = pygame.image.load(date_g[0][1]+'g.png')
    gameDisplay.blit(year_g_2,(189+650+84,464+8))
    year_y_2 = pygame.image.load(date[0][1]+'y.png')
    gameDisplay.blit(year_y_2,(189+650+84,843+8))

    year_o_3 = pygame.image.load(date_o[3][0]+'o.png')
    gameDisplay.blit(year_o_3,(189+650+84+84,96+8))
    year_g_3 = pygame.image.load(date_g[0][2]+'g.png')
    gameDisplay.blit(year_g_3,(189+650+84+84,464+8))
    year_y_3 = pygame.image.load(date[0][2]+'y.png')
    gameDisplay.blit(year_y_3,(189+650+84+84,843+8))

    year_o_4 = pygame.image.load(date_o[3][1]+'o.png')
    gameDisplay.blit(year_o_4,(189+650+84+84+84,96+8))
    year_g_4 = pygame.image.load(date_g[0][3]+'g.png')
    gameDisplay.blit(year_g_4,(189+650+84+84+84,464+8))
    year_y_4 = pygame.image.load(date[0][3]+'y.png')
    gameDisplay.blit(year_y_4,(189+650+84+84+84,843+8))

    #DAYS ##########
    day_o_1 = pygame.image.load(date_o[0][0]+'o.png')
    gameDisplay.blit(day_o_1,(189+350,96+8))
    day_g_1 = pygame.image.load(date_g[2][0]+'g.png')
    gameDisplay.blit(day_g_1,(189+350,464+8))
    day_y_1 = pygame.image.load(date[2][0]+'y.png')
    gameDisplay.blit(day_y_1,(189+350,843+8))

    day_o_2 = pygame.image.load(date_o[0][1]+'o.png')
    gameDisplay.blit(day_o_2,(189+350+84,96+8))
    day_g_2 = pygame.image.load(date_g[2][1]+'g.png')
    gameDisplay.blit(day_g_2,(189+350+84,464+8))
    day_y_2 = pygame.image.load(date[2][1]+'y.png')
    gameDisplay.blit(day_y_2,(189+350+84,843+8))

    #HOURS #########
    if int(time[0]) > 12:
        time[0] = str(int(time[0])-12)
        if len(time[0]) == 1:
            time[0] = '0'+time[0]
    elif int(time[0]) == 0:
        time[0] = '12'
    hour_o_1 = pygame.image.load(time[0][0]+'o.png')
    gameDisplay.blit(hour_o_1,(189+650+500,96+8))
    hour_g_1 = pygame.image.load(time[0][0]+'g.png')
    gameDisplay.blit(hour_g_1,(189+650+500,464+8))
    hour_y_1 = pygame.image.load(time[0][0]+'y.png')
    gameDisplay.blit(hour_y_1,(189+650+500,843+8))

    hour_o_1 = pygame.image.load(time[0][1]+'o.png')
    gameDisplay.blit(hour_o_1,(189+650+500+84,96+8))
    hour_g_1 = pygame.image.load(time[0][1]+'g.png')
    gameDisplay.blit(hour_g_1,(189+650+500+84,464+8))
    hour_y_1 = pygame.image.load(time[0][1]+'y.png')
    gameDisplay.blit(hour_y_1,(189+650+500+84,843+8))
    
    #MINS ##########
    mins_o_1 = pygame.image.load(time[1][0]+'o.png')
    gameDisplay.blit(mins_o_1,(189+650+500+270,96+8))
    mins_g_1 = pygame.image.load(time[1][0]+'g.png')
    gameDisplay.blit(mins_g_1,(189+650+500+270,464+8))
    mins_y_1 = pygame.image.load(time[1][0]+'y.png')
    gameDisplay.blit(mins_y_1,(189+650+500+270,843+8))

    mins_o_1 = pygame.image.load(time[1][1]+'o.png')
    gameDisplay.blit(mins_o_1,(189+650+500+270+84,96+8))
    mins_g_1 = pygame.image.load(time[1][1]+'g.png')
    gameDisplay.blit(mins_g_1,(189+650+500+270+84,464+8))
    mins_y_1 = pygame.image.load(time[1][1]+'y.png')
    gameDisplay.blit(mins_y_1,(189+650+500+270+84,843+8))

    blink = ~(blink)
    if blink == False:
        gameDisplay.blit(t_o,(189+650+500+202,96+27))
        gameDisplay.blit(t_g,(189+650+500+202,464+27))
        gameDisplay.blit(t_y,(189+650+500+201,843+24))
    else:
        pass

    tm.sleep(1)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
