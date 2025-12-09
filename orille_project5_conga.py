"""

This program uses classes and the dudraw window to draw a circle on the screen with a random color.
A circle first appears when you hit the 'n' key for the first time.  This circle will continue following
the mouse's current position.  Afterward's if you hit 'n' again, more circles will appear and begin following
the previous circle in the line.  It looks like a conga line.

File Name:orille_project5_conga.py
Date:02/10/2023
Course: COMP1352
Assignment: Project 5
Collaborators: 1352 Instructors
Internet Sources: None
"""
#brings in random to be used to place circles with random colors and coordinates
from random import random
#brings in dudraw to bring up the canvas to draw circles on.
import dudraw
#class of dancers or circles that will be drawn
class Dancer:
    #creates empty lists that will be used to store the data of the circles
    name = 0
    #names of the dancers
    dancers = []
    #x positions of the dancers
    x_pos = []
    #y positions of the dancers
    y_pos = []
    #rgb values of the dancers
    colors = []
    #sizes of the dancers
    sizes = []
    #initializes values for each x-position, y_position, color, and size
    #the default values are random values for x and y positions, black for an rgb value, and .025 for the radius
    def __init__(self, x = int(random()*50), y = int(random()*50), c =(0,0,0), s = .025):
        self.x_posi = x
        self.y_posi = y
        self.color = c
        self.size = s
        #add one to the name
        Dancer.name += 1
        #Add all of the values to the empty lists that were created above
        
        self.dancers.append(Dancer.name)
        self.x_pos.append(self.x_posi)
        self.y_pos.append(self.y_posi)
        self.colors.append(self.color)
        self.sizes.append(self.size)
        
        
        

    def __str__(self):
        #checks each list for debugging purposes
        return f'the list is: {self.dancers}\nthe xpos list is: {self.x_pos}\nthe ypos list is: {self.y_pos}\nthe colors are: {self.colors}\nthe sizes are {self.sizes}'
    #this function draws the circles using the lists created before
    def draw(self):
        #checks the list
        for i in range(len(self.colors)):
            #uses the random rgb values as a random color
            dudraw.set_pen_color_rgb(self.colors[i][0],self.colors[i][1],self.colors[i][2])
            #draw a circle at the x and y positions listed before and use the size as the radius.
            dudraw.filled_circle(self.x_pos[i], self.y_pos[i], self.sizes[i])
            #this function takes only itself in.  It changes the x and y positions of the circles which will be used to redraw the circles
            #every frame
    def move(self):
        #checks through the list(the number of circles)
        for i in range(len(self.colors)):
            #for the first circle drawn, take its distance from the current mouse position and set it to a variable
            if i == 0:
                dist_x = float(dudraw.mouse_x() - self.x_pos[i])
                dist_y = float(dudraw.mouse_y() - self.y_pos[i])
                #after the first circle, have each sequential circle, follow the last.
                #take the distance from that position and set it to a variable
            if i > 0:
                dist_x = float(self.x_pos[i-1] - self.x_pos[i])
                dist_y = float(self.y_pos[i-1] - self.y_pos[i])
            #add .5% of the distance in the x and y planes to the x and y positions
            #this change will allow the movement for the circles to change smoothly until they reach their target.
            
            self.x_pos[i]+=.005*dist_x
            self.y_pos[i]+=.005*dist_y
 
        
    
#show the white canvas
dudraw.set_canvas_size(500,500)
dudraw.clear()



   
#sets a variable to start the while loop
l=0
#this variable ensures that the animation starts drawing circles only after the 'n' key is pressed.
m = 0
#while loop which starts the animation
while l == 0:
    #if a key is pressed
    if dudraw.has_next_key_typed():
        #if the key is 'n', draw a circle
        if dudraw.next_key_typed() == 'n':
            dancer = Dancer(random(),random(),(int(random()*255),int(random()*255),int(random()*255)))
            #add one to this variable to start drawing circles after Dancer() is called
            m += 1 
        #if 'q' is pressed, stop the function
        elif dudraw.next_key_typed() == 'q':
            l +=1
        
    #after a circle is created, the canvas is cleared, circles are drawn using the function below.        
    if m>0:
        dudraw.clear()
        #calls the .draw function to draw the circle to the canvas
        dancer.draw()
        #calls the .move function to change the x and y values of the circles which will be redrawn every frame of animation.
        dancer.move()
    


        
    


        
        
    #show the canvas for a split second 
    dudraw.show(5)



        
        
        