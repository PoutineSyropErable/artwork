# François Pagé, public so mcgill id hidden. 
"""
created on Fri sep 23 18:13:41 2022

@author: Francois
"""

import turtle
import math



get_bonus = True #True or False

if get_bonus:
    from artwork_bonus import *




def coord_png(x,y): 
    ''' (num,num) -> (num,num) 
    taking coordonates in pixel position (paint) to coordonate in centered cartesian

    >>>coord_png(0,0)
    (-350,325)

    >>>coord_png(350,0)
    (0,325)

    >>>coord_png(700,0)
    (350,325)
    '''
    return(x-350,325-y)


def draw_border():
    ''' () -> NoneType
    | draws the cyan colored border for the image

    >>>draw_border()
    NoneType
     '''
    border=turtle.Turtle()
    border.speed(9)
    border.hideturtle()
    border.color("cyan")
    border.penup()
    border.goto(-350,-325)
    border.pendown()
    border.goto(-350,325)
    border.goto(350,325)
    border.goto(350,-325)
    border.goto(-350,-325)
    
def draw_star(n,length):
    ''' (num,num) -> NoneType
    draws a star at a fixed position. The star has "n" spikes of length "length". You are free to change n and length. 

    >>>draw_star()
    NoneType
    '''
    n = int(abs(n))
    if n<3:
        n= int(3)
    theta = 360/n
    if length >30:
        length = 30
    star = turtle.Turtle()
    star.color("red")
    star.fillcolor("yellow")
    star.begin_fill()
    star.speed(4)
    star.penup()
    star.goto(-325,300)
    star.pendown()
    
    for i in range(2*n):
        star.forward(length)
        star.left( (180-(i%2 +1 )*theta )* (-1)**i)
    star.end_fill()
    star.hideturtle()



def draw_d(doom): #draw the d
    ''' 
    (Turtle) -> NoneType
    
    It draws the D in Doom Eternal. Uses input to recycle object. 

    '''
        #exterior of D
    doom.penup()
    doom.goto(coord_png(87,408))
    doom.pendown()
    
    doom.fillcolor("black")
    doom.begin_fill()
    
    doom.goto(coord_png(87,136))
    doom.goto(coord_png(65,119))
    doom.goto(coord_png(129,119))
    doom.goto(coord_png(128.5,120))
    doom.goto(coord_png(133,119))
    doom.goto(coord_png(196,119))
    doom.goto(coord_png(211,130))
    doom.goto(coord_png(211,309))
    doom.goto(coord_png(215,311))
    doom.goto(coord_png(87,408))
    
    doom.end_fill()
    #end of exterior of D


    #start of interior of D
    doom.penup()
    doom.goto(coord_png(134,298))
    doom.pendown()
    
    doom.fillcolor("white")
    doom.begin_fill()
    
    doom.goto(coord_png(134,169))
    doom.goto(coord_png(161,169))
    doom.goto(coord_png(165,172))
    doom.goto(coord_png(165,275))
    doom.goto(coord_png(134,298))
    doom.end_fill()
    doom.hideturtle()
    #end of exterior of D
    
def draw_o_1(doom): #draw the first o, i'm parsing doom twice as a cheap trick, to save on resetting the speed... i know.
    ''' 
    (Turtle) -> NoneType
    
    It draws the first O in Doom Eternal. Uses input to recycle object.  


    >>>draw_o_1(some_other_turtle)
    NoneType

    '''
    
    #exterior of o
    doom.penup()
    doom.goto(coord_png(217,302))
    doom.pendown()
    
    doom.fillcolor("black")
    doom.begin_fill()
    
    doom.goto(coord_png(217,130))
    doom.goto(coord_png(232,119))
    doom.goto(coord_png(326,119))
    doom.goto(coord_png(341,130))
    doom.goto(coord_png(341,330))
    doom.goto(coord_png(297.5,362))
    doom.goto(coord_png(217,302))
    
    doom.end_fill()
    #end of exterior of o
    
    #start of interior of o
    doom.fillcolor("white")
    doom.begin_fill()
    
    doom.penup()
    doom.goto(coord_png(263,275))
    doom.pendown()
    
    
    
    doom.goto(coord_png(263,172))
    doom.goto(coord_png(267,169))
    doom.goto(coord_png(271,169))
    doom.goto(coord_png(295,172))
    doom.goto(coord_png(295,298))
    doom.goto(coord_png(263,275))
    
    doom.end_fill()
    doom.hideturtle()
    #end of interior of o


#the trick: webplotdigitiliser + string concatenate in for loop.
#at first, i got the coordinate only. 

#-------------------------------From now on, i've already got 3 shape (star, d , o)
    #i've got a For loop(star), input in artwork(star).
    #i've got black, red and yellow For the colors






def draw_f_name(): #this draws the F in my name. 
    ''' () -> NoneType
    draws the F in my name. 
    '''
    f_name= turtle.Turtle()
    f_name.penup()

    f_name.begin_fill()
    f_name.pensize(1.3)
    f_name.color(0,0,0)
    f_name.fillcolor(255,106,0)

    f_name.goto(272.12983268356066,256.0806908044912)
    f_name.pendown()

    f_name.goto(272.30750487329425,254.3048375977536)
    f_name.goto(272.48517706302783,253.23927375197414)
    f_name.goto(273.0181936322286,252.7061673182287)
    f_name.goto(273.72888239116304,252.3505034203805)
    f_name.goto(274.61724333983096,252.17228205842957)
    f_name.goto(274.61724333983096,250.75170333651334)
    f_name.goto(273.0181936322286,250.75287157559384)
    f_name.goto(270.1754385964911,250.93252078530986)
    f_name.goto(266.6219948018193,250.93511687215548)
    f_name.goto(258.44907407407396,250.76351553166083)
    f_name.goto(258.44907407407396,252.1840942535771)
    f_name.goto(259.5151072124756,252.53846010800248)
    f_name.goto(260.5811403508771,253.603115323386)
    f_name.goto(260.7588125406107,254.1357025397623)
    f_name.goto(260.7588125406107,256.6217153031157)
    f_name.goto(260.7588125406107,282.90242165856637)
    f_name.goto(260.7588125406107,298.7063599398847)
    f_name.goto(260.7588125406107,299.59422164108236)
    f_name.goto(260.5811403508771,300.30464080638274)
    f_name.goto(259.87045159194275,300.8378770444705)
    f_name.goto(258.98209064327483,301.1936707466609)
    f_name.goto(258.44907407407396,301.54920484016685)
    f_name.goto(258.44907407407396,302.79221122184356)
    f_name.goto(262.0025178687459,302.789615134998)
    f_name.goto(296.6485948667965,302.7643032882533)
    f_name.goto(303.9331546458739,302.7589813102198)
    f_name.goto(305.3545321637426,302.93551521572107)
    f_name.goto(306.4205653021441,303.6450257506255)
    f_name.goto(306.95358187134497,304.71007037903587)
    f_name.goto(307.13125406107844,305.2426575954122)
    f_name.goto(308.19728719948006,305.2418787693585)
    f_name.goto(308.37495938921364,303.9987425833395)
    f_name.goto(308.37495938921364,298.3164276956745)
    f_name.goto(308.37495938921364,294.58740855064434)
    f_name.goto(308.37495938921364,291.7462511068118)
    f_name.goto(307.13125406107844,291.74715973720777)
    f_name.goto(306.7759096816114,292.63528104709)
    f_name.goto(306.2428931124106,293.5235321613145)
    f_name.goto(305.3545321637426,294.0568982037445)
    f_name.goto(304.1108268356075,294.0578068341405)
    f_name.goto(301.6234161793371,294.05962409493236)
    f_name.goto(287.23196881091604,294.0701382466571)
    f_name.goto(274.0842267706302,293.90217142774634)
    f_name.goto(272.30750487329425,294.0810418114086)
    f_name.goto(272.30750487329425,291.95017372853425)
    f_name.goto(272.30750487329425,288.5762992639832)
    f_name.goto(272.12983268356066,283.07168652089996)
    f_name.goto(272.12983268356066,281.82868013922325)
    f_name.goto(274.4395711500974,281.8269926827736)
    f_name.goto(278.34835932423647,281.82413698724343)
    f_name.goto(292.20679012345664,281.81401224854557)
    f_name.goto(293.62816764132543,281.81297381380733)
    f_name.goto(294.87187296946064,282.34478220412996)
    f_name.goto(295.582561728395,283.2321246879585)
    f_name.goto(295.93790610786215,284.1197267804716)
    f_name.goto(297.18161143599724,284.11881815007564)
    f_name.goto(297.18161143599724,281.98795006720127)
    f_name.goto(297.18161143599724,270.9784649723503)
    f_name.goto(295.93790610786215,270.97937360274625)
    f_name.goto(295.76023391812856,271.6897927680467)
    f_name.goto(295.4048895386614,272.40034173768936)
    f_name.goto(294.69420077972705,273.1111503160166)
    f_name.goto(293.9835120207927,273.4668142138648)
    f_name.goto(292.5621345029239,273.46785264860307)
    f_name.goto(287.5873131903833,273.4714871701869)
    f_name.goto(282.61249187784273,273.4751216917707)
    f_name.goto(275.3279320987654,273.48044366980423)
    f_name.goto(272.12983268356066,273.4827801479653)
    f_name.goto(272.12983268356066,270.28647802365373)
    f_name.goto(272.12983268356066,265.31445249694684)
    f_name.goto(272.12983268356066,260.697571650719)
    f_name.goto(272.12983268356066,256.0806908044912)
    
    f_name.end_fill()
    f_name.hideturtle()
    

def draw_doom():
    ''' () -> NoneType
    draws DO and OM(if Bonus) in DOOM logo. 
    '''
    doom = turtle.Turtle()
    doom.speed(5)
    
    
    draw_d(doom)
    draw_o_1(doom)




    if get_bonus:
        print("----------------------")
        print("___________ From here on out, the bonus stuFF is being drawn, i won't comment the rest as it is done by code_______________________")
        print("----------------------------------------- THE FUNCTION IN THE BONUS GODE POSSESS CAPITAL LETTERS IN IT!")
        print("----------------------")
        draw_o_2() #From bonus code.
        draw_m() #From bonus code





def my_artwork():
    turtle.colormode(255)  # <------------- WITHOUT THIS, I CAN'T USE RNG AND STRING NAME. NOT GONNA TRY TO CONVERT IT ALL, THIS WOULD BE BS. 
    #turtle.speed(10)
    turtle.hideturtle()
    
    draw_border()
    draw_f_name()
    draw_star(12,30) #this one has a for loop and you can change the: draw_star(nu,ber of side,side lenght)

    draw_doom()



    #this is bonus From now on. do not correct. 
    if get_bonus:
        draw_eternal() #bonus line oF code
        draw_crucible() #bonus code



    
    
    
    
    turtle.done() #<<<---- Without this function, the whole thing crash in every ide except for thommy. 
    
my_artwork()





    
    