import pygame
import os
x =  10
y =  10
speed_x = 3
speed_y = 3
Lives = 0


#to load our character/ball
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
#for the background but it wont load.
##background_image = pygame.image.load('backgroundcopy.png').convert()
screen.blit(background_image, [150, 125])

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        x = x+speed_x
        y = y+speed_y

        

        if y <0 or y >255:
                speed_y = speed_y*-1
                Lives += 1
                print(Lives)
                
        if x <0 or x >300:
                speed_x = speed_x*-1
                Lives += 1
                print (Lives) 
#to increase speed
        if Lives == 16 or Lives == 32 or Lives == 48 or Lives == 64 or Lives == 80:
                speed_x = speed_x*+1.1
                speed_y = speed_y*+1.1
#to stop everything
        if Lives == 96:
                x = 200
                y = 200
                print ('parry this you casual bouncy boy')
                break

        

        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('BallS.png'), (x, y, 20, 20))
        
        pygame.display.flip()
        clock.tick(60)
