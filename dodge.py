import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

GAMEOVER = False

class GameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.BLACK)

		self.world = World()
		self.set_mouse_visible(False)

	def on_key_press(self, key, modifiers):
		if key == arcade.key.SPACE:
			self.world = World()

	def on_mouse_motion(self, x, y, dx, dy):
		self.world.player.x = x
		self.world.player.y = y

	def on_draw(self):
		arcade.start_render()
		self.world.update()
		self.world.target.render()
		self.world.player.render()

class World:
	def __init__(self):
		self.player = Player(self)
		self.target = Target()
		self.bullet = Bullet(None)

		self.player_collide_bullet = False
		self.player_collide_target = False

		self.bullet_list = []
		self.target_list = []

		self.score = -1

	def spawn_bullet(self):
		if random.randrange(0, 100) < 12:
			self.bullet_list.append(Bullet(RandomDir()))

		for bullet in self.bullet_list:
			bullet.render()
			if self.player_collide_bullet == False:
				self.player_collide_bullet = arcade.check_for_collision(self.player.sprite, bullet.sprite)

	def spawn_target(self):
		self.player_collide_target = arcade.check_for_collision(self.player.sprite, self.target.sprite)
		if self.player_collide_target == True:
			self.target.x = random.randrange(0, SCREEN_WIDTH)
			self.target.y = random.randrange(0, SCREEN_HEIGHT)
			self.score += 1


	def update(self):
		self.spawn_bullet()
		self.spawn_target()
		self.output = "Score: {} || Space to reset".format(self.score)
		arcade.draw_text(self.output, 20, 20, arcade.color.WHITE, 14)

class Player():
	def __init__(self, world):
		self.x = SCREEN_WIDTH / 2
		self.y = SCREEN_HEIGHT / 2
		self.circle_radius = 3

		self.world = world

		self.sprite = arcade.Sprite('images/player.png')

	def render(self):
		if self.world.player_collide_bullet == False:
			self.sprite.set_position(self.x, self.y)
			self.sprite.draw()

class Target():
	def __init__(self):
		self.x = random.randrange(0, SCREEN_WIDTH)
		self.y = random.randrange(0, SCREEN_HEIGHT)
		self.circle_radius = 3

		self.sprite = arcade.Sprite('images/target.png')

	def render(self):
		self.sprite.set_position(self.x, self.y)
		self.sprite.draw()

class Bullet():
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
		self.speed = 7

		self.sprite = arcade.Sprite('images/bullet.png')
	
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

	def render(self):
		self.stop_update = False
		
		if self.stop_update == False:
	
			if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
				self.stop_update = True
	
			if self.stop_update == False:
				self.update();
				self.sprite.set_position(self.x, self.y)
				self.sprite.draw()
				
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
