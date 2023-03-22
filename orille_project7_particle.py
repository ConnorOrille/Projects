import dudraw
import math
from random import random
from random import uniform

"""

Creates a particle system using classes that displays fireworks when the 'f' key is pressed.  A fire emits from the center
of the canvas along with a sparkler that continuously runs.
when the mouse is pressed, marbles appear on the canvas


File Name:orille_project7_particle.py
Date:03/08/2023
Course: COMP1352
Assignment: Project 7
Collaborators: 1352 Instructors
Internet Sources: None
"""



#class that allows an x and y value for things we will use later like velocity and acceleration
class Vector:
    def __init__(self, some_x=0, some_y=0):
        self.x = some_x
        self.y = some_y

    def limit(self, l):
        if(self.length() >= l):
            self.resize(l)

    def resize(self, l):
        length = math.sqrt(self.x ** 2 + self.y**2)
        self.x *= (l/length)
        self.y *= (l/length)

    def __add__(self, other_vector)->None:
        return Vector(self.x+other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector)->None:
        return Vector(self.x-other_vector.x, self.y - other_vector.y)

    def __isub__(self, other_vector)->None:
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self

    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self

    def divide(self, s):
        self.x /= s
        self.y /= s

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_in_radians(self):
        return math.tan((self.y/self.x))
    
#class that allows time to be tracked.  This feature is used in order to track the lifetime of all particles on the canvas.
class Time:
    frame = 0

    def tick():
        Time.frame += 1
    
    def time():
        return Time.frame
#the first class, particle is used to draw specific kinds of things on a canvas
class Particle:
    #initialize the class object with
    # a vector that has x and y position
    # a vector that has x and y velocity
    # size which is a float
    # color and lifetime

    def __init__(self,x_pos,y_pos,x_vel,y_vel,size:float,color, lifetime):
        self.position = Vector(x_pos,y_pos)
        self.velocity = Vector(x_vel,y_vel)
        self.size = size
        #random color
        self.color = dudraw.Color(int(random()*255),int(random()*255),int(random()*255))
        self.lifetime = lifetime
    #particles will disappear as time goes on
    #this function checks the lifetime of each particle and returns a boolean value
    def has_expired(self):   
        if self.lifetime <=0:
            return True
        return False
    #everytime a the object moves, lifetime ticks down one
    #if the object still has lifetime, change the position of the particle by the velocity     
    def move(self):
        self.lifetime-=1
        if self.has_expired() == False:
            self.position += self.velocity
#new class SparkParticle is derived from Particle       
class SparkParticle(Particle):
    #initialize it with everything from particle except here we change the color to a gold color to
    #simulate a spark in the real world
    def __init__(self,x_pos,y_pos,x_vel,y_vel,size:float,lifetime):
        #call everything from the parent class particle
        Particle.__init__(self,x_pos,y_pos,x_vel,y_vel,size,color =0, lifetime = lifetime)
        self.color = dudraw.Color(218,165,32)
    #this draw function checks if the particle is active with lifetime
    #and takes the gold color that we initialized the function with
    def draw(self):
        if self.has_expired() != True:
            dudraw.set_pen_color(self.color)
        #takes the point from the position of the particle and uses that point as one side of a line
        #the other endpoint of the line is the position of that particle with the velocity added
        #this other position is now a new vector.
            
            otherposition = self.position+self.velocity
            #draw the line with those points
            dudraw.line(self.position.x,self.position.y,otherposition.x,otherposition.y)
    #a new type of particle that incorporates a new vector, acceleration
    #derived from particle
class AcceleratingParticle(Particle):
    #initializes with the same as particle
    def __init__(self,x_pos,y_pos,x_vel,y_vel,size:float,lifetime,x_acc, y_acc):
        Particle.__init__(self,x_pos,y_pos,x_vel,y_vel,size,color = dudraw.Color(int(random()*255),int(random()*255),int(random()*255)),lifetime = lifetime)
       #new vector called acceleration
        self.acceleration = Vector(x_acc,y_acc)
#move position and velocity by addding velocity and acceleration respectively
    def move(self):
        
        self.position += self.velocity
        self.velocity += self.acceleration
        
        
#new class called firework which draws a small square with a random color if it still has lifetime 
class FireWorkParticle(AcceleratingParticle):
    
    def draw(self):
        if self.has_expired != True:
            
            dudraw.set_pen_color(self.color)
            dudraw.filled_square(self.position.x, self.position.y, self.size)
#new class which draws circles  with a random color if it still has lifetime       
class MarbleParticle(AcceleratingParticle):
    def draw(self):
        if self.has_expired != True:
            dudraw.set_pen_color(self.color)
            dudraw.filled_circle(self.position.x,self.position.y,self.size)


# new class fireparticle which takes two vectors (position and velocity)
# size, color, and lifetime
class FireParticle(Particle):
    def __init__(self,x_pos,y_pos,x_vel,y_vel,size,lifetime):
        Particle.__init__(self,x_pos,y_pos,x_vel,y_vel,size,color =0,lifetime = lifetime)
        #this particle changes the green rgb value as the lifetime ticks down
        self.green = 230
        self.color = dudraw.Color(247,self.green,20)
        #draws a circle with a color which green rgb value changes -3 everytime lifetime tick
    def draw(self):
        if self.has_expired != True:
            self.green -= 3
            self.color = dudraw.Color(247,self.green,20)           
            dudraw.set_pen_color(self.color)
            dudraw.filled_circle(self.position.x, self.position.y, self.size)
    #move like the parent particle    
    def move(self):
        Particle.move(self)
        #shrink in size as time goes on
        self.size -= .001
#new class particlecontainer has a vector of position and an empty container will eventually be filled with particles   
class ParticleContainer:
    def __init__(self,x_pos,y_pos):
        self.position = Vector(x_pos,y_pos)
        self.particles = []
        #check through the list of particles backwards for the expiration of the particles
        #if the particle hasnt expired, draw and move it
    def animate(self):
        for i in reversed(range(len(self.particles))):
            if self.particles[i].has_expired() != True:
                self.particles[i].move()
                self.particles[i].draw()
            else:
                #if the particle has expired, remove it from the list and canvas
                self.particles.remove(self.particles[i])
            

                
#new class Emitter derived from the class ParticleContainer
# initialize particlecontainer with position 
# add new fire_rate which will determine the amount of particles will emit at a time on the canvas
class Emitter(ParticleContainer):
    def __init__(self,x_pos,y_pos,fire_rate):
        ParticleContainer.__init__(self,x_pos,y_pos)
        self.fire_rate = fire_rate

#new class Fire which derives from emitter
class Fire(Emitter):
    #animate like the parent class emitter
    #append fire_rate amount of fireparticles to the empty container of particles
    #each fire particle has its own position, velocity, size, color, and lifetime
    def animate(self):
        Emitter.animate(self)
        for i in range(self.fire_rate):
            self.particles.append(FireParticle(self.position.x,self.position.y,uniform(-.002,.002),uniform(.002,.005), size = uniform(.03,.05), lifetime = 50 ))
#new class sparkler which is derived from emitter
class Sparkler(Emitter):
    #animate like the parent class and append
    #fire_rate amount of spark particles to the particle container
    def animate(self):
        Emitter.animate(self)
        for i in range(self.fire_rate):
            self.particles.append(SparkParticle(self.position.x,self.position.y,uniform(-.07,.07),uniform(-.07,.07),size = 0.04, lifetime = 5))
#class which is derived from particle container
class FireWork(ParticleContainer):
    def __init__(self,x_pos,y_pos):
        #initialize particle container and add 500 firework particles to the container
        ParticleContainer.__init__(self,x_pos,y_pos)
        for i in range(500):
            self.particles.append(FireWorkParticle(self.position.x,self.position.y,uniform(-.04,.04),uniform(-.04,.04), x_acc =0, y_acc=uniform(-.008,-.012), size =.004, lifetime = 2))
  #new class marble is derived from particle container  
class Marbles(ParticleContainer):
    #initialize particlecontainer and append 10 marble particles to the particle container
    def __init__(self,x_pos,y_pos):
        ParticleContainer.__init__(self,x_pos,y_pos)
        for i in range(10):
            self.particles.append(MarbleParticle(uniform(.05,-.05), uniform(.05,-.05), random()*.08 - .04, random()*.08 - .04, x_acc = 0, y_acc =random()*0.003 - .001, size = 0.05, lifetime = 500 ))
    def animate(self):
        #draw the marbles and animate them across the screen
        ParticleContainer.animate(self)

       #draw the canvas 
dudraw.set_canvas_size(500,500)
#empty container for fire and sparkler particles
containers = []

containers.append(Fire(0.5,.15,10))
containers.append(Sparkler(0.8,0.3,100))
marbles = []

while True:
    #continuously tick time through this while loop
    Time.tick()
    #clear the canvas
    dudraw.clear(dudraw.DARK_GRAY)
    #set pen color 
    dudraw.set_pen_color(dudraw.WHITE)
    #draw stick from which a sparkler will emit from
    dudraw.line(.8,.3,.8,0)
    
  
    
    
    #animate all of the particles in the contaienr 
    for container in containers:
        container.animate()
    #if there are marbles to animate , animate them
    if len(marbles) > 0:
        for marble in marbles:
            marble.animate()

        
    #if the 'f' key is typed, add a firework particle to the container and animate them    
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()
        if key == 'f':
            containers.append(FireWork(dudraw.mouse_x(), dudraw.mouse_y()))
    if dudraw.mouse_clicked():
        marbles.append(Marbles(dudraw.mouse_x(),dudraw.mouse_y()))
        #show the canvas
    dudraw.show(40)
    