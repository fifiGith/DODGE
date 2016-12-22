import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.BLACK)

		self.bullet = Bullet("up")

	def on_draw(self):
		arcade.start_render()
		self.bullet.draw()
		

class Bullet:
	def __init__(self, dir):
		self.dir = dir
		self.x = random.randrange(0, SCREEN_WIDTH)
		self.y = random.randrange(0, SCREEN_HEIGHT)
		self.speed = 5
		self.circle_radius = 20
	
	def update(self):
		if self.dir == "left":
			self.x += self.speed
		elif self.dir == "right":
			self.x -= self.speed
		elif self.dir == "up":
			self.y -= self.speed
		elif self.dir == "down":
			self.y += self.speed

	def draw(self):
		self.update();
		arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.WHITE)
 
def main():
	window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()

if __name__ == '__main__':
	main()
