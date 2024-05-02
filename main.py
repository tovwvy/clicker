import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar

kivy.require('1.11.1')

class CookieClicker(App):
    def __init__(self, **kwargs):
        super(CookieClicker, self).__init__(**kwargs)
        self.cookie_count = 0
        self.hand_count = 0
        self.granny_count = 0
        self.click_count = 0  
        self.baked_cookie_count = 0  
        self.level = 1  # Ініціалізуємо атрибут рівня

    def build(self):
        self.layout = RelativeLayout()

        background = Image(source='l-intro-1648138138.jpg', allow_stretch=True, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout.add_widget(background)

        # Кнопка печива
        self.cookie_button = Image(source='png-clipart-cookie-clicker-clicker-heroes-incremental-game-cookie-game-baked-goods-thumbnail.png', 
                                   size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.cookie_button.bind(on_touch_down=self.on_click)
        self.layout.add_widget(self.cookie_button)
       
        # Лейбли та іконки
        self.cookie_label = Label(text="Cookies: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 0.95, 'top': 0.95})
        self.layout.add_widget(self.cookie_label)

        self.counter_label = Label(text="Clicks: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 0.95, 'top': 0.9})
        self.layout.add_widget(self.counter_label)

        self.baked_cookie_label = Label(text="Baked Cookies: 0", font_size=20, color='#ffffff', size_hint=(None, None), size=(200, 50), pos_hint={'right': 0.95, 'top': 0.8})
        self.layout.add_widget(self.baked_cookie_label)

        self.hand_label = Label(text="Hands: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 0.95, 'top': 0.75})
        self.layout.add_widget(self.hand_label)

        self.granny_label = Label(text="Grannies: 0", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 0.95, 'top': 0.7})
        self.layout.add_widget(self.granny_label)

        self.level_label = Label(text="Level: 1", font_size=20, size_hint=(None, None), size=(150, 50), pos_hint={'right': 0.95, 'top': 0.6})
        self.layout.add_widget(self.level_label)

        # Modernized level progress bar
        self.level_progress = ProgressBar(max=100, size_hint=(None, None), size=(200, 20), pos_hint={'right': 0.95, 'top': 0.55})
        self.level_progress.background = 'atlas://data/images/defaulttheme/slider_bg'
        self.level_progress.foreground = 'atlas://data/images/defaulttheme/slider_fg'
        self.layout.add_widget(self.level_progress)

        # Іконки для покупки
        self.buy_hand_icon = Image(source='99162.png', size_hint=(None, None), size=(50, 50), pos_hint={'right': 0.95, 'top': 0.45})
        self.buy_hand_icon.bind(on_touch_down=self.buy_hand)  
        self.layout.add_widget(self.buy_hand_icon)

        self.buy_granny_icon = Image(source='GrandmaIconTransparent.webp', size_hint=(None, None), size=(50, 50), pos_hint={'right': 0.95, 'top': 0.35})
        self.buy_granny_icon.bind(on_touch_down=self.buy_granny)  
        self.layout.add_widget(self.buy_granny_icon)

        # Лейбли для відображення кількості
        self.hand_count_label = Label(text="0", size_hint=(None, None), size=(50, 50), pos_hint={'right': 0.9, 'top': 0.45})
        self.layout.add_widget(self.hand_count_label)

        self.granny_count_label = Label(text="0", size_hint=(None, None), size=(50, 50), pos_hint={'right': 0.9, 'top': 0.35})
        self.layout.add_widget(self.granny_count_label)

        Clock.schedule_interval(self.automatic_click, 1)
        Clock.schedule_interval(self.level_up, 1)

        return self.layout

    def on_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # Increment click count and update label
            self.click_count += 1
            self.counter_label.text = "Clicks: {}".format(self.click_count)

            # Increment cookie count and update label every 10 clicks
            if self.click_count % 10 == 0:
                self.cookie_count += 2
                self.cookie_label.text = "Cookies: {}".format(self.cookie_count)

                self.baked_cookie_count += 2
                self.baked_cookie_label.text = "Baked Cookies: {}".format(self.baked_cookie_count)

    def buy_hand(self, instance, touch):
        if self.cookie_count >= 10:
            self.cookie_count -= 10
            self.cookie_label.text = "Cookies: {}".format(self.cookie_count)
            self.hand_count += 1
            self.hand_label.text = "Hands: {}".format(self.hand_count)
            self.hand_count_label.text = str(self.hand_count)  

    def buy_granny(self, instance, touch):
        if self.cookie_count >= 30:
            self.cookie_count -= 30
            self.cookie_label.text = "Cookies: {}".format(self.cookie_count)
            self.granny_count += 1
            self.granny_label.text = "Grannies: {}".format(self.granny_count)
            self.granny_count_label.text = str(self.granny_count)

 

    def level_up(self, dt):
        if self.cookie_count >= self.level * 100:
            self.level += 1
            self.cookie_count -= self.level * 100
            self.cookie_label.text = "Cookies: {}".format(self.cookie_count)
            self.level_label.text = "Level: {}".format(self.level)
            self.level_progress.max = self.level * 100
            self.level_progress.disabled = True

    def automatic_click(self, dt):
        hand_cookies_produced = 0
        granny_cookies_produced = 0
    
        if self.hand_count > 0:
            hand_cookies_produced = 2 * self.hand_count

        if self.granny_count > 0:
            granny_cookies_produced = 10 * self.granny_count

        self.cookie_count += hand_cookies_produced + granny_cookies_produced
        self.cookie_label.text = "Cookies: {}".format(self.cookie_count)

if __name__ == '__main__':
    CookieClicker().run()
