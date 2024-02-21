from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.scrollview import ScrollView

class AlphabetGridApp(App):
    def build(self):
        # Vendosim ngjyrën e sfondit të aplikacionit në grimcë
        Window.clearcolor = get_color_from_hex('#96f3ff')  # Grimcë

        # Krijimi i ScrollView që përmban të gjithë layout-in kryesor
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))

        # Layout kryesor me orientim vertikal, të vendosur brenda ScrollView
        main_layout = BoxLayout(orientation='vertical', padding=[10, 10, 10, 10], spacing=10, size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter('height'))

        # Etiketa e titullit për shkronjat
        title_label = Label(text='Të mësojmë shkronjat', font_size='32sp', size_hint_y=None, height=60, color=get_color_from_hex('#FFFFFF'))
        main_layout.add_widget(title_label)

        # Alfabeti dhe butonat
        alphabet_grid = GridLayout(cols=6, spacing=10, size_hint_y=None)
        alphabet_grid.bind(minimum_height=alphabet_grid.setter('height'))
        self.alphabet = ['A', 'B', 'C', 'Ç', 'D', 'DH', 'E', 'Ë', 'F', 'G', 'GJ', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N', 'NJ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'SH', 'T', 'TH', 'U', 'V', 'X', 'XH', 'Y', 'Z', 'ZH']
        for char in self.alphabet:
            btn = Button(text=char, font_size='24sp', size_hint=(None, None), size=(100, 100), background_normal='', background_color=get_color_from_hex('#0a38f0'), color=get_color_from_hex('#FFFFFF'))
            btn.bind(on_press=self.play_sound)
            alphabet_grid.add_widget(btn)
        main_layout.add_widget(alphabet_grid)
        
        # Etiketa e titullit për zanoret
        title_label = Label(text='Të mësojmë zanoret', font_size='24sp', size_hint_y=None, height=60, color=get_color_from_hex('#FFFFFF'))
        main_layout.add_widget(title_label)
        
        # Grid shtesë për zanoret
        extra_grid = GridLayout(cols=6, spacing=10, size_hint_y=None)
        self.alphabet2 = ['A', 'E', 'Ë', 'I', 'O', 'U', 'Y']
        for char in self.alphabet2:
            btn = Button(text=char, font_size='24sp', size_hint=(None, None), size=(100, 100), background_normal='', background_color=get_color_from_hex('#90EE90'), color=get_color_from_hex('#FFFFFF'))
            btn.bind(on_press=self.play_sound)
            extra_grid.add_widget(btn)
        main_layout.add_widget(extra_grid)
        
        # Etiketa e titullit për numrat
        title_label = Label(text='Të mësojmë numrat', font_size='24sp', size_hint_y=None, height=60, color=get_color_from_hex('#FFFFFF'))
        main_layout.add_widget(title_label)
        
        # Grid për numrat
        number_grid = GridLayout(cols=6, spacing=10, size_hint_y=None)
        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for char in self.number:
            btn = Button(text=char, font_size='24sp', size_hint=(None, None), size=(100, 100), background_normal='', background_color=get_color_from_hex('#90EE90'), color=get_color_from_hex('#FFFFFF'))
            btn.bind(on_press=self.play_sound)
            number_grid.add_widget(btn)
        main_layout.add_widget(number_grid)

        # Vendosim main_layout brenda scroll_view
        scroll_view.add_widget(main_layout)

        return scroll_view

    def play_sound(self, instance):
        sound_name = instance.text
        sound_file = f'{sound_name}.mp3'
        sound = SoundLoader.load(sound_file)
        if sound:
            sound.play()

if __name__ == '__main__':
    AlphabetGridApp().run()
