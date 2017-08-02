from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):

    velx = NumericProperty(0)
    vely = NumericProperty(0)

    velocity = ReferenceListProperty(velx,vely)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):

    ball = ObjectProperty(None)

    def update(self,dt):
        self.ball.move()
        
        #bounce vertical
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.vely *= -1

        #bounce horizontal
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velx *= -1

        

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update,1.0/60.0)
        return game

if __name__ == '__main__':
    PongApp().run()
