import pygame
import math
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

state='brush'
dist=0

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False


prev, cur = None, None
screen.fill(BLACK)

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    
  if event.type == pygame.MOUSEBUTTONDOWN :
      prev = pygame.mouse.get_pos()
  if event.type == pygame.MOUSEMOTION :
      cur = pygame.mouse.get_pos()
      if prev and state == 'brush':
        pygame.draw.line(screen, RED, prev, cur, 1)
        prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
          prev = None
  
  if event.type == pygame.MOUSEBUTTONDOWN :
      prev1 = pygame.mouse.get_pos()
  if event.type == pygame.MOUSEBUTTONUP :
      cur1 = pygame.mouse.get_pos()
      if prev and state == 'circle':
        dict = math.sqrt( math.pow((prev1[0]-cur1[0]), 2 ) + math.pow((prev1[1]-cur1[1]), 2 ))
        pygame.draw.circle(screen, RED, ( prev1[0]- ( dist / 2 ) , prev1[1]- ( dist / 2 ) ), dist/2, 3)
  
  if event.type == pygame.K_c:
      state = 'circle'
      print(state)
  pygame.display.flip()

  clock.tick(30)


pygame.quit()