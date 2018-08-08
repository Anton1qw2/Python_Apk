from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.utils import hex_colormap, get_color_from_hex
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy import uix
import cv2
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture

KV = """
# Разметка пункта списка.
<Item@BoxLayout>:
    color: []
    name_color: ''

    Label
        canvas.before:
            Color:
                rgba: root.color
            Rectangle:
                pos: self.pos
                size: self.size
        text: root.name_color
        color: 0, 0, 0, 1

# Контейнер для списка.
BoxLayout:
    orientation: "vertical"

    RecycleView:
        id: rv
        key_size: 'height'
        key_viewclass: 'viewclass'

        RecycleBoxLayout:
            id: box
            default_size: None, None
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(5)

"""

class MyClass(Widget):
    pass

class RecycleViewApp(App):
    text = "Cool Buuton"
    name = ""
    def build(self):
        self.color = [1., 0., 0., 1.]
        self.a = Button(text= self.text, pos = (0,1.),size_hint = (1,.5))
        self.a.bind(on_press = self.cool)
        # self.img = Image(source='top.png')
        self.img = cv2.imread("top.png")
        buffer =cv2.flip(self.img, 0).tostring()
        print(self.img.shape[0:2:-1])
        tex = Texture.create(size= (self.img.shape[1],self.img.shape[0]) ,  colorfmt='bgr')
        import traceback
        try:
            tex.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        except:
            traceback.print_exc()
        self.img = Image()
        self.img.texture = tex

        # self.label = uix.label.Label(text = "LOL", pos = (300,0), size_hint = (1,.5))
        self.MainLayout = uix.floatlayout.FloatLayout(size= (330,300))
        self.MainLayout.add_widget(self.a)
        # self.MainLayout.add_widget(self.label)
        self.MainLayout.add_widget(self.img)
        # self.root = Builder.load_string(KV)
        # self.rv = self.root.ids.rv
        self.create()
        return self.MainLayout
        # self.create()
    def cool(self,instanse):
        self.a.text = "LOL"
        if self.name =="down.png":
            self.name = "top.png"
        else:
            self.name = "down.png"
        self.img.texture = Image(source=self.name).texture
        self.a.background_color = self.color


    def create(self):
        colors = []

        #
        # # Создание списка.
        # for name_color in hex_colormap.keys():
        #     colors.append({
        #         "name_color": self.a.text,
        #         "viewclass": "Item",
        #         'color': get_color_from_hex(hex_colormap[name_color]),
        #         'height': dp(20),
        #     })
        # self.rv.data = colors
RecycleViewApp().run()