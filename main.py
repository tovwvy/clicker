import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.clock import Clock

kivy.require('1.11.1')

class CookieClicker(App):
    def build(self):
        self.layout = RelativeLayout()

        background = Image(source='l-intro-1648138138.jpg', allow_stretch=True, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(background)

        self.cookie_count = 0
        self.cookie_button = Image(source='png-clipart-cookie-clicker-clicker-heroes-incremental-game-cookie-game-baked-goods-thumbnail.png', size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.cookie_button.bind(on_touch_down=self.on_click)
        self.layout.add_widget(self.cookie_button)

        self.cookie_label = Label(text="Cookies: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 1, 'top': 0.95})
        self.layout.add_widget(self.cookie_label)

        self.click_count = 0
        self.counter_label = Label(text="Clicks: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 1, 'top': 0.9})
        self.layout.add_widget(self.counter_label)

        self.baked_cookie_count = 0
        self.baked_cookie_label = Label(text="Baked Cookies: 0", font_size=20, color='#ffffff', size_hint=(None, None), size=(200, 50), pos_hint={'right': 0.9, 'top': 0.8})
        self.layout.add_widget(self.baked_cookie_label)

        self.hand_count = 0
        self.hand_label = Label(text="Hands: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 1, 'top': 0.75})
        self.layout.add_widget(self.hand_label)

        self.granny_count = 0
        self.granny_label = Label(text="Grannies: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 1, 'top': 0.7})
        self.layout.add_widget(self.granny_label)

        self.buy_hand_icon = Image(source='99162.png', size_hint=(None, None), size=(50, 50), pos_hint={'right': 0.95, 'top': 0.6})
        self.buy_hand_icon.bind(on_touch_down=self.buy_hand)
        self.layout.add_widget(self.buy_hand_icon)

        self.buy_granny_icon = Image(source='GrandmaIconTransparent.webp', size_hint=(None, None), size=(50, 50), pos_hint={'right': 0.95, 'top': 0.5})
        self.buy_granny_icon.bind(on_touch_down=self.buy_granny)  # Внесено зміну тут
        self.layout.add_widget(self.buy_granny_icon)

        Clock.schedule_interval(self.automatic_click, 3)
        Clock.schedule_interval(self.granny_cookie, 20)

        return self.layout

    def on_click(self, instance, touch):
        if self.cookie_button.collide_point(*touch.pos):
            self.click_count += 1
            self.counter_label.text = "Clicks: {}".format(self.click_count)

            if self.click_count % 10 == 0:
                self.cookie_count += 2
                self.cookie_label.text = "Cookies: {}".format(self.cookie_count)

                self.baked_cookie_count += 2
                self.baked_cookie_label.text = "Baked Cookies: {}".format(self.baked_cookie_count)

    def buy_hand(self, instance, touch):
        if self.buy_hand_icon.collide_point(*touch.pos):
            if self.cookie_count >= 10:
                self.cookie_count -= 10
                self.cookie_label.text = "Cookies: {}".format(self.cookie_count)
                self.hand_count += 1
                self.hand_label.text = "Hands: {}".format(self.hand_count)

    def buy_granny(self, instance, touch):
        if self.buy_granny_icon.collide_point(*touch.pos):
            if self.cookie_count >= 30:
                self.cookie_count -= 30
                self.cookie_label.text = "Cookies: {}".format(self.cookie_count)
                self.granny_count += 1
                self.granny_label.text = "Grannies: {}".format(self.granny_count)

    def automatic_click(self, dt):
        if self.hand_count > 0:
            self.on_click(self.cookie_button, None)

    def granny_cookie(self, dt):
        if self.granny_count > 0:
            self.cookie_count += 10
            self.cookie_label.text = "Cookies: {}".format(self.cookie_count)

if __name__ == '__main__':
    CookieClicker().run()
