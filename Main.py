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
from Business_logic import FaceGane


class RecycleViewApp(App):
    text = "Cool Buuton"
    name = ""
    def build(self):
        self.color = [1., 0., 0., 1.]
        self.a = Button(text= self.text)
        self.a.bind(on_press = self.cool)
        self.img = FaceGane.getFace()
        buffer =cv2.flip(self.img, 0).tostring()
        tex = Texture.create(size= (self.img.shape[1],self.img.shape[0]) ,  colorfmt='bgr')
        import traceback
        try:
            tex.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        except:
            traceback.print_exc()
        self.img = Image()
        self.img.texture = tex
        self.MainLayout = uix.floatlayout.FloatLayout(size= (330,300))
        self.MainLayout.add_widget(self.a)
        self.MainLayout.add_widget(self.img)
        return self.MainLayout
    def cool(self,instanse):
        img = FaceGane.getFace()
        buffer =cv2.flip(img, 0).tostring()
        tex = Texture.create(size= (img.shape[1],img.shape[0]) ,  colorfmt='bgr')
        import traceback
        try:
            tex.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        except:
            traceback.print_exc()
        self.img.texture = tex



RecycleViewApp().run()