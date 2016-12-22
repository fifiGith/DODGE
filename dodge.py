import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class GameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.BLACK)

		self.world = World()
		self.set_mouse_visible(False)

	def on_mouse_motion(self, x, y, dx, dy):
		self.world.player.x = x
		self.world.player.y = y

	def on_draw(self):
		arcade.start_render()
		self.world.player.draw()
		self.world.target.draw()
		self.world.spawn_bullet()

class World:
	def __init__(self):
		self.player = Player()
		self.target = Target()
		self.bullet = Bullet(None)

		self.bullet_list = []

	def spawn_bullet(self):
		self.bullet_list.append(Bullet(RandomDir()))
		for bullet in self.bullet_list:
			bullet.draw()

class Player:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.circle_radius = 3

	def draw(self):
		arcade.draw_circle_filled(self.x, self.y, self.circle_radius, arcade.color.RED)

class Target:
	def __init__(self):
		self.x = random.randrange(0, SCREEN_WIDTH)
		self.y = random.randrange(0, SCREEN_HEIGHT)
		self.circle_radius = 3

	def draw(self):
		arcade.draw_circle_filled(self.x, self.y, self.circle_radius, arcade.color.GREEN)

class Bullet:
	def __init__(self, dir):
		self.dir = dir
		if self.dir == "left":
			self.x = 0
			self.y = random.randrange(0, SCREEN_HEIGHT)
		elif self.dir == "right":
			self.x = SCREEN_WIDTH
			self.y = random.randrange(0, SCREEN_HEIGHT)
		elif self.dir == "up":
			self.x = random.randrange(0, SCREEN_WIDTH)
			self.y = SCREEN_HEIGHT
		elif self.dir == "down":
			self.x = random.randrange(0, SCREEN_WIDTH)
			self.y = 0
		else:
			pass

		self.circle_radius = 3
		self.speed = 10
	
	def update(self):
		if self.dir == "left":
			self.x += self.speed
		elif self.dir == "right":
			self.x -= self.speed
		elif self.dir == "up":
			self.y -= self.speed
		elif self.dir == "down":
			self.y += self.speed
		else:
			pass

	def draw(self):
		self.stop_update = False
		
		if self.stop_update == False:
	
			if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
				self.stop_update = True
	
			if self.stop_update == False:
				self.update();
				arcade.draw_circle_filled(self.x, self.y, self.circle_radius, arcade.color.WHITE)
 
def RandomDir():
	n = random.randrange(0, 4)
	if n == 0:
		return "left"
	elif n == 1:
		return "right"
	elif n == 2:
		return "up"
	elif n == 3:
		return "down"

def main():
	window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()

if __name__ == '__main__':
	main()
