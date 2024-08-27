from tkinter import *
import numpy as np
import math
import time
import sys
np.set_printoptions(threshold=sys.maxsize)
#np.set_printoptions(suppress=True)

WIDTH = 500
HEIGHT = 500
C = 299792458   #m/s
num_orbits = 4
display_radius = 160
period = 200    #T = 152853 s
# Orbital Values
R_Orbit = 422000000     #m
V_Orbit = 17334     #m/s
distance = 588000000000000     #m      1000x distance to Jupiter


#This function draws the normal orbit moviment you would see if you were to watch it through a telescope
def normal_orbit():
    for n in range(num_orbits):
        for Jt in range(period + 1):
            theta = (Jt * 2*math.pi)/period
            theta_before = ((Jt-1) * 2*math.pi)/period
            x = round(1*display_radius * math.cos(theta))
            y = round(1*display_radius * math.cos(theta))
            #print(x, y)
            if (display_radius * math.cos(theta)) < (display_radius * math.cos(theta_before)):
                canvas.moveto(lua_front_1, x+250, y+250)
                canvas.moveto(lua_back_1, 600, 600)
            elif (display_radius * math.cos(theta)) >= (display_radius * math.cos(theta_before)):
                canvas.moveto(lua_back_1, x+250, y+250)
                canvas.moveto(lua_front_1, 600, 600)
            window.update()
            time.sleep(0.03)
    canvas.moveto(lua_back_1, 600, 600)
    canvas.moveto(lua_front_1, 600, 600)


#The Jupiter_Array splits the orbits in half orbits, and for each position in orbit, it calculates the time at which it 
#  should arrive on Earth, using that big formula. When causality breaks, times repeat, and even rolls back.
Jupiter_Array = np.zeros( (2*num_orbits, period) )
for n in range(2*num_orbits):
    for Jt in range(period):
        if math.pow(-1, n) > 0:     #Front Side
            theta = (Jt * math.pi)/period
            Jupiter_Array[n,Jt] = round((1/(C+(V_Orbit*math.cos(theta))))*(distance + (R_Orbit *-1*math.sin(theta))) + (n*period) + Jt - (distance/(C+V_Orbit)))
        elif math.pow(-1, n) < 0:   #Back Side
            theta = ((Jt * math.pi)/period)+math.pi
            Jupiter_Array[n,Jt] = round((1/(C+(V_Orbit*math.cos(theta))))*(distance + (R_Orbit *-1*math.sin(theta))) + (n*period) + Jt - (distance/(C+V_Orbit)))
        #print(theta)


#The histogram is a 1D array that counts how many orbital positions exist for each time instant. It is used to obtain how many
#  front moons and back moons are used at maximum, so they can be latter created by the orbits_module.
histogram = np.zeros((1,round(np.max(Jupiter_Array) + 1)))
histogram_front = np.zeros((1,round(np.max(Jupiter_Array) + 1)))
histogram_back = np.zeros((1,round(np.max(Jupiter_Array) + 1)))
for n in range(2*num_orbits):
    for Jt in range(period):
        histogram[0, round(Jupiter_Array[n,Jt])] += 1
        if math.pow(-1, n) > 0:
            histogram_front[0, round(Jupiter_Array[n,Jt])] += 1
        elif math.pow(-1, n) < 0:
            histogram_back[0, round(Jupiter_Array[n,Jt])] += 1


#The Earth_Arrays (front and back) recieve the orbital angle theta relative to the orbital positions Jt from Jupiter_Array. 
#  These values of theta are placed in order by the time at which the arrive on Earth. Each array has the exact size to have the
#  maximum number of moons at once for each time instant.
#The index 0 of each inner array represents the next available slot for a value theta inside that inner array.
Earth_Array_front = np.full( (round(np.max(Jupiter_Array) + 1) , round(np.max(histogram_front) + 1 )), -1.)
Earth_Array_front[:, 0] = 1
Earth_Array_back = np.full( (round(np.max(Jupiter_Array) + 1) , round(np.max(histogram_back) + 1 )), -1.)
Earth_Array_back[:, 0] = 1
#Filling the the Earth_Arrays with the values of theta
for n in range(2*num_orbits):
    for Jt in range(period):
        if math.pow(-1, n) > 0:     #Front Side
            theta = (Jt * math.pi)/period
            indice = round(Earth_Array_front[round(Jupiter_Array[n,Jt]), 0])
            Earth_Array_front[round(Jupiter_Array[n,Jt]), indice] = theta
            Earth_Array_front[round(Jupiter_Array[n,Jt]), 0] += 1
        elif math.pow(-1, n) < 0:   #Back Side
            theta = ((Jt * math.pi)/period)+math.pi
            indice = round(Earth_Array_back[round(Jupiter_Array[n,Jt]), 0])
            Earth_Array_back[round(Jupiter_Array[n,Jt]), indice] = theta
            Earth_Array_back[round(Jupiter_Array[n,Jt]), 0] += 1
        #print(theta)


#> orbits_module <#
#This is where things get interesting. In order to draw the exact number of moons needed, this program writes it's own module,
#  with 3 functions: 2 to draw the front and back moons, and 1 to move them to the right coordinates at the right time.
#  This last function takes booth Earth_Arrays as arguments. It also takes the window and canvas where to move them.
#  The 2 first functions take only the canvas as argument.   They need to be called in order to do what they are supposed to.
my_file = open("orbits_module.py", "w")
my_file.write("from tkinter import *\n")
my_file.write("import numpy as np\n")
my_file.write("import math\n")
my_file.write("import time\n\n")
my_file.write("display_radius = "+str(display_radius)+"\n")
my_file.write("def start_front_moons(canvas):\n")
for moon in range(round(np.max(histogram_front))):      #Front Moons
    my_file.write("\tglobal front_"+str(moon +1)+"\n")
    my_file.write("\tfront_"+str(moon +1)+" = canvas.create_oval(600, 600, 610, 610, fill=\"#00ccff\", width=0)\n")     #fix coords
my_file.write("def start_back_moons(canvas):\n")
for moon in range(round(np.max(histogram_back))):       #Back Moons
    my_file.write("\tglobal back_"+str(moon +1)+"\n")
    my_file.write("\tback_"+str(moon +1)+" = canvas.create_oval(600, 600, 610, 610, fill=\"#0033cc\", width=0)\n")      #fix coords
my_file.write("\n\n")
my_file.write("def draw_relative_moons(window, canvas, Earth_Array_front, Earth_Array_back):\n")
my_file.write("\tfor t in range(Earth_Array_front.shape[0]):\n")
for moon in range(Earth_Array_front.shape[1] -1):
    my_file.write("\t\tif Earth_Array_front[t, "+str(moon +1)+"] == -1:\n")    # replace the 1
    my_file.write("\t\t\tcanvas.moveto(front_"+str(moon +1)+", 600, 600)\n")
    my_file.write("\t\telse:\n")
    my_file.write("\t\t\ttheta_front_"+str(moon +1)+" = Earth_Array_front[t, "+str(moon +1)+"]\n")
    my_file.write("\t\t\tx_front_"+str(moon +1)+" = round(1*display_radius * math.cos(theta_front_"+str(moon +1)+"))\n")
    my_file.write("\t\t\ty_front_"+str(moon +1)+" = round(1*display_radius * math.cos(theta_front_"+str(moon +1)+"))\n")
    my_file.write("\t\t\tcanvas.moveto(front_"+str(moon +1)+", x_front_"+str(moon +1)+"+250, y_front_"+str(moon +1)+"+250)\n")
for moon in range(Earth_Array_back.shape[1] -1):
    my_file.write("\t\tif Earth_Array_back[t, "+str(moon +1)+"] == -1:\n")    # replace the 1
    my_file.write("\t\t\tcanvas.moveto(back_"+str(moon +1)+", 600, 600)\n")
    my_file.write("\t\telse:\n")
    my_file.write("\t\t\ttheta_back_"+str(moon +1)+" = Earth_Array_back[t, "+str(moon +1)+"]\n")
    my_file.write("\t\t\tx_back_"+str(moon +1)+" = round(1*display_radius * math.cos(theta_back_"+str(moon +1)+"))\n")
    my_file.write("\t\t\ty_back_"+str(moon +1)+" = round(1*display_radius * math.cos(theta_back_"+str(moon +1)+"))\n")
    my_file.write("\t\t\tcanvas.moveto(back_"+str(moon +1)+", x_back_"+str(moon +1)+"+250, y_back_"+str(moon +1)+"+250)\n")
my_file.write("\t\twindow.update()\n")
my_file.write("\t\ttime.sleep(0.02)\n")
my_file.close()
import orbits_module


#>  Creating the Window and Canvas  <#
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.create_rectangle(0, 0, WIDTH+20, HEIGHT+20, fill="black")    #Space
canvas.pack()

#> Creating the moons on the canvas <#
lua_back_1 = canvas.create_oval(190, 190, 200, 200, fill="#0033cc", width=0)    #Back Moon
orbits_module.start_back_moons(canvas=canvas)
planet = canvas.create_oval(200, 200, 300, 300, fill="#ffcc99", width=0)    #Jupiter
orbits_module.start_front_moons(canvas=canvas)
lua_front_1 = canvas.create_oval(190, 190, 200, 200, fill="#00ccff", width=0)   #Front Moon

canvas.moveto(lua_back_1, 600, 600)
canvas.moveto(lua_front_1, 600, 600)


#normal_orbit()

orbits_module.draw_relative_moons(window, canvas, Earth_Array_front, Earth_Array_back)


#>  Debug Earth_Array  <#
def debug_Earth_Array():
    my_file = open("Earth_Array.txt", "w")
    my_file.write(str(Earth_Array_front))
    my_file.write("\n\n\n")
    my_file.write(str(Earth_Array_back))
    my_file.close()
    print(Earth_Array_front.shape)
#debug_Earth_Array()

#> DEBUG COMMANDS <#
#print(Jupiter_Array)
#print(histogram)
#print(histogram_front)
#print(histogram_back)
#print(np.max(histogram_front))
#print(np.max(histogram_back))
#print(Earth_Array_front)
#print(Earth_Array_back)


def relativity_test():          #this is an old test that only works if it's only 1 moon. 
    for t in range(round(np.max(Jupiter_Array) + 1)):
        for moon in range(1):  #round(np.max(histogram_front))
            if Earth_Array_front[t, moon +1] == -1:
                canvas.moveto(lua_front_1, 600, 600)
            else:
                theta_front = Earth_Array_front[t, moon +1]         #moon +1 to avoid the value at index 0
                x_front = round(1*display_radius * math.cos(theta_front))
                y_front = round(1*display_radius * math.cos(theta_front))
                canvas.moveto(lua_front_1, x_front+250, y_front+250)
                #print(theta_front, x_front, y_front)
        for moon in range(1):   #round(np.max(histogram_back))
            if Earth_Array_back[t, moon +1] == -1:
                canvas.moveto(lua_back_1, 600, 600)
            else:
                theta_back = Earth_Array_back[t, moon +1]
                x_back = round(1*display_radius * math.cos(theta_back))
                y_back = round(1*display_radius * math.cos(theta_back))
                canvas.moveto(lua_back_1, x_back+250, y_back+250)
                #print(theta_back, x_back, y_back)
        window.update()
        time.sleep(0.02)

#relativity_test()


window.mainloop()
