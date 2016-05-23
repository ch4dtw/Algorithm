import pygame
import numpy as np
import random
import sys


def calcPoint(lastPoint, thisPoint, point):
	drawPoint = point[0]
	minAngel = -1
	for tmpPoint in point:
		a = np.array([thisPoint[0] - lastPoint[0], thisPoint[1] - lastPoint[1]])
		b = np.array([tmpPoint[0]  - thisPoint[0],  tmpPoint[1] - thisPoint[1]])
		La = np.sqrt(a.dot(a)) # length of vector a
		Lb = np.sqrt(b.dot(b)) # length of vector b
		cosAngel = a.dot(b) / (La * Lb) # cos value
		if(minAngel < cosAngel):
			minAngel = cosAngel
			drawPoint = tmpPoint
	return drawPoint
if __name__ == "__main__":
	pygame.init()
	background = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Convex Hull")
	pointNum = int(sys.argv[1])
	background.fill((255,255,255))
	running = 1
	start = 0
	clock = pygame.time.Clock()
	point = []
	minPoint = (800, 600)
	for i in range(pointNum):
		x = random.randrange(10, 790)
		y = random.randrange(10, 590)
		temp = (x, y)
		point.append(temp)
		if y < minPoint[1]: # first point, y value is smallest
			minPoint = temp
		pygame.draw.circle(background, (0 ,0 ,255), (x, y), 3, 0)

	thisPoint = minPoint
	lastPoint = (thisPoint[0] + 10, thisPoint[1])
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0
			elif  (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
				if not start:
					pygame.draw.circle(background, (0, 255, 0), thisPoint, 5, 0)
					start = 1
				elif thisPoint == minPoint:
					pygame.draw.aaline(background, (192, 192, 192), lastPoint, thisPoint, True)
					break
				else:
					pygame.draw.aaline(background, (192, 192, 192), lastPoint, thisPoint, True)
					pygame.draw.circle(background, (155, 0, 0), thisPoint, 5, 0)
					point.remove(thisPoint)
				lastPoint, thisPoint = thisPoint, calcPoint(lastPoint, thisPoint, point)

		pygame.display.flip()

	pygame.quit()
