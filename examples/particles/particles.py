import pygame, sys, random
colors = [(255, 0, 0), (255, 255, 255), (0, 0, 255)]
class ParticlePrinciple: #A class is a fancy way of being able to create a group of things that work together.
    def __init__(self): #This allows us to say that the object is doing these things.
        self.particles = [] #This is a list that will hold all of the particles we are creating.
    def emit(self): #This is the method that will be called to update the particles and draw them on the screen.
        self.delete_particles() #This is the method that will be called to delete the particles that are no longer visible on the screen.
        if self.particles:
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.1
                pygame.draw.circle(screen, random.choice(colors), particle[0], int(particle[1]))
    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = 5
        direction_x = random.randint(-3, 3)
        direction_y = random.randint(-3, 3)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

particle1 = ParticlePrinciple()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 10) # Hey so like this thing does the thing every 10 milliseconds. NOT VIBECODED.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            particle1.add_particles()
    screen.fill((30, 30, 30))
    particle1.emit()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()