import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

# Definindo as cores para consistência com o protótipo (tema escuro)
PRIMARY_COLOR = get_color_from_hex('#1A1A1A') # Cor de fundo principal
SECONDARY_COLOR = get_color_from_hex('#2E2E2E') # Cor dos painéis/inputs
TEXT_COLOR = get_color_from_hex('#FFFFFF') # Cor do texto branco
ACCENT_COLOR_GREEN = get_color_from_hex('#4CAF50') # Verde para "aprovado" / alto
ACCENT_COLOR_YELLOW = get_color_from_hex('#FFEB3B') # Amarelo para "parcial" / médio
ACCENT_COLOR_RED = get_color_from_hex('#F44336') # Vermelho para "não aprovado" / baixo

# O Kivy Language (KV) para definir o layout das telas
# Isso permite separar a definição do layout da lógica Python.
KV_CODE = """
<MainScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgb: app.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

        # Logo TurSeguro
        Image:
            source: 'logo_turseguro.png' # Você precisará ter esta imagem no diretório
            size_hint: (0.3, 0.2)
            pos_hint: {'center_x': 0.5, 'top': 0.9}
            allow_stretch: True
            keep_ratio: True

        Label:
            text: 'Descubra destinos turísticos acessíveis e seguros'
            color: app.text_color
            size_hint_y: None
            height: dp(40)
            pos_hint: {'center_x': 0.5, 'top': 0.7}
            font_size: '20sp'

        BoxLayout:
            orientation: 'horizontal'
            size_hint: (0.8, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            padding: dp(10)
            spacing: dp(10)

            TextInput:
                id: search_input
                hint_text: 'Qual local deseja?'
                multiline: False
                background_color: app.secondary_color
                foreground_color: app.text_color
                hint_text_color: app.text_color
                font_size: '18sp'
                padding: [dp(15), dp(15), dp(15), dp(15)]
                size_hint_x: 0.9
                on_text_validate: root.search_location(self.text) # Ao pressionar Enter

            Button:
                background_normal: ''
                background_color: app.secondary_color
                size_hint_x: 0.1
                on_release: root.search_location(search_input.text)
                Image:
                    source: 'search_icon.png' # Ícone de lupa, precisa ser fornecido
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    size: dp(30), dp(30)
                    color: app.text_color

        # Placeholder para o mapa
        # Em um aplicativo real, isso seria um widget de mapa que renderizaria tiles
        # ou um WebView para exibir o HTML gerado pelo Folium.
        Label:
            text: 'Mapa Interativo (integrado com Folium)'
            color: app.text_color
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            size_hint: (1, 0.4)
            canvas.before:
                Color:
                    rgb: app.secondary_color
                Rectangle:
                    pos: self.pos
                    size: self.size


<DetailScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgb: app.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, 1)

            # Painel esquerdo de detalhes
            ScrollView:
                size_hint: (0.4, 1) # Ocupa 40% da largura
                background_color: app.secondary_color # Fundo escuro para o painel
                canvas.before:
                    Color:
                        rgb: app.secondary_color
                    Rectangle:
                        pos: self.pos
                        size: self.size

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)
                    spacing: dp(15)

                    # Top bar com busca e logo
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(50)
                        spacing: dp(10)
                        padding: [0, dp(10), 0, dp(10)]
                        
                        Image:
                            source: 'logo_turseguro.png'
                            size_hint: (0.2, 1)
                            allow_stretch: True
                            keep_ratio: True
                            
                        Label:
                            text: 'TurSeguro'
                            color: app.text_color
                            font_size: '22sp'
                            bold: True
                            size_hint_x: 0.8
                            text_size: self.size
                            valign: 'middle'


                    TextInput:
                        id: detail_search_input
                        hint_text: 'Universidade' # Exemplo do protótipo
                        multiline: False
                        background_color: app.primary_color # Mais escuro para diferenciar
                        foreground_color: app.text_color
                        hint_text_color: app.text_color
                        font_size: '18sp'
                        padding: [dp(15), dp(15), dp(15), dp(15)]
                        size_hint_y: None
                        height: dp(60)
                        on_text_validate: root.search_location(self.text)

                    # Seção de Acessibilidade
                    Label:
                        text: 'Acessibilidade'
                        color: app.text_color
                        font_size: '20sp'
                        bold: True
                        size_hint_y: None
                        height: dp(30)
                        text_size: self.size
                        valign: 'middle'

                    # Itens de Acessibilidade (usar um GridLayout para alinhar)
                    GridLayout:
                        cols: 2
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(10)
                        row_default_height: dp(30)
                        row_force_default: True

                        Label:
                            text: 'Rampas para cadeirantes'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '100%' # Placeholder - será preenchido com dados reais
                            color: app.accent_color_green
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                        Label:
                            text: 'Pista tátil'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '95%' # Placeholder
                            color: app.accent_color_green
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                        Label:
                            text: 'Cão Guia'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '2%' # Placeholder
                            color: app.accent_color_red # Assumindo 2% é vermelho
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                        Label:
                            text: 'Elevadores'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '50%' # Placeholder
                            color: app.accent_color_yellow # Assumindo 50% é amarelo
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                    # Seção de Segurança
                    Label:
                        text: 'Segurança'
                        color: app.text_color
                        font_size: '20sp'
                        bold: True
                        size_hint_y: None
                        height: dp(30)
                        text_size: self.size
                        valign: 'middle'

                    # Itens de Segurança
                    GridLayout:
                        cols: 2
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(10)
                        row_default_height: dp(30)
                        row_force_default: True

                        Label:
                            text: 'Bombeiros'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '85%' # Placeholder
                            color: app.accent_color_green
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                        Label:
                            text: 'Seguranças'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '95%' # Placeholder
                            color: app.accent_color_green
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                        Label:
                            text: 'Câmeras'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '100%' # Placeholder
                            color: app.accent_color_green
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                        Label:
                            text: 'Casos de crimes'
                            color: app.text_color
                            halign: 'left'
                            text_size: self.size
                            valign: 'middle'
                        Label:
                            text: '75%' # Placeholder
                            color: app.accent_color_yellow # Assumindo 75% é amarelo
                            halign: 'right'
                            text_size: self.size
                            valign: 'middle'

                    # Relatório Descritivo
                    Label:
                        text: 'Relatório descritivo'
                        color: app.text_color
                        font_size: '20sp'
                        bold: True
                        size_hint_y: None
                        height: dp(30)
                        text_size: self.size
                        valign: 'middle'

                    Label:
                        id: report_label # Adicionado ID para fácil atualização
                        text: ('A Universidade Católica de Brasília promove acessibilidade com apoio '
                        color: app.text_color
                        font_size: '16sp'
                        size_hint_y: None
                        height: self.texture_size[1] # Ajusta altura para o texto
                        text_size: self.width, None
                        valign: 'top'


            # Área do mapa (direita)
            FloatLayout:
                size_hint: (0.6, 1) # Ocupa 60% da largura
                background_color: app.primary_color # Cor de fundo mais escura para o mapa
                canvas.before:
                    Color:
                        rgb: app.primary_color
                    Rectangle:
                        pos: self.pos
                        size: self.size

                # Placeholder para o mapa Folium
                Label:
                    text: 'Mapa Interativo com Pontos Turísticos'
                    color: app.text_color
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    font_size: '20sp'
                    bold: True

                # Exemplo de pop-up do mapa (simulado com um BoxLayout flutuante)
                # Em um cenário real, isso seria um overlay do widget do mapa.
                BoxLayout:
                    id: map_popup # Adicionado ID
                    orientation: 'vertical'
                    size_hint: (0.4, 0.2)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7} # Posição simulada do pop-up
                    padding: dp(10)
                    spacing: dp(5)
                    background_color: app.secondary_color
                    canvas.before:
                        Color:
                            rgb: app.secondary_color
                        Rectangle:
                            pos: self.pos
                            size: self.size

                    Label:
                        id: popup_title
                        text: 'Universidade Católica de Brasília' # Placeholder
                        color: app.text_color
                        font_size: '16sp'
                        bold: True
                        text_size: self.width, None
                        halign: 'left'

                    Label:
                        id: popup_status
                        text: 'Segurança: aprovado\\nAcessibilidade: aprovado' # Placeholder
                        color: app.text_color
                        font_size: '14sp'
                        text_size: self.width, None
                        halign: 'left'

                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(40)
                        spacing: dp(10)

                        Image:
                            source: 'star_icon.png' # Ícone de estrela, precisa ser fornecido
                            size_hint_x: None
                            width: dp(30)
                            allow_stretch: True
                            keep_ratio: True
                            color: app.text_color

                        Label:
                            id: popup_rating
                            text: '100' # Exemplo de avaliação - Placeholder
                            color: app.text_color
                            font_size: '18sp'
                            halign: 'left'
                            text_size: self.width, None

                        Button:
                            text: 'Detalhes'
                            background_normal: ''
                            background_color: app.accent_color_green # Botão verde
                            color: app.text_color
                            font_size: '16sp'
                            size_hint_x: 0.5
                            # A ação de 'Detalhes' no pop-up do mapa, conforme o protótipo,
                            # parece indicar que o usuário já está na tela de detalhes,
                            # então este botão poderia fechar o pop-up ou não ter ação aqui,
                            # ou se o pop-up aparece na MainScreen, ele navegaria para DetailScreen.
                            # Assumindo que este pop-up está na DetailScreen (conforme imagem),
                            # ele pode apenas fechar ou não ter uma ação de navegação.
                            # Se o pop-up estiver na MainScreen, a ação seria:
                            # on_release: app.root.current = 'detail_screen'
                            on_release: print("Botão 'Detalhes' do pop-up do mapa clicado.")


"""

# Carregar o KV_CODE
Builder.load_string(KV_CODE)

class MainScreen(Screen):
    """
    Tela principal para buscar locais e visualizar o mapa.
    """
    def search_location(self, text):
        """
        Método chamado ao pesquisar um local.
        Neste ponto, você chamaria a lógica do Controller para buscar dados.
        """
        print(f"Pesquisando por: {text}")
        # Lógica para buscar o local e então mudar para a DetailScreen
        # Exemplo: self.manager.get_screen('detail_screen').load_data(dados_do_local)
        self.manager.current = 'detail_screen'

class DetailScreen(Screen):
    """
    Tela para exibir detalhes de um ponto turístico.
    """
    def on_enter(self, *args):
        """
        Chamado quando a tela é exibida.
        Aqui você carregaria os dados do ponto turístico selecionado
        passados pelo Controller.
        """
        print("Entrou na DetailScreen")
        # Exemplo de como você poderia carregar dados (esta função precisaria ser definida)
        # self.load_data_example()

    def load_data_example(self, location_data=None):
        """
        Exemplo de função para carregar dados na tela de detalhes.
        `location_data` seria um dicionário ou objeto com as informações do local.
        """
        if location_data is None: # Dados de exemplo se nada for passado
            location_data = {
                "name": "Universidade Católica (Exemplo)",
                "accessibility": {
                    "Rampas para cadeirantes": {"value": "100%", "color": ACCENT_COLOR_GREEN},
                    "Pista tátil": {"value": "95%", "color": ACCENT_COLOR_GREEN},
                    "Cão Guia": {"value": "2%", "color": ACCENT_COLOR_RED},
                    "Elevadores": {"value": "50%", "color": ACCENT_COLOR_YELLOW},
                },
                "security": {
                    "Bombeiros": {"value": "85%", "color": ACCENT_COLOR_GREEN},
                    "Seguranças": {"value": "95%", "color": ACCENT_COLOR_GREEN},
                    "Câmeras": {"value": "100%", "color": ACCENT_COLOR_GREEN},
                    "Casos de crimes": {"value": "75%", "color": ACCENT_COLOR_YELLOW},
                },
                "report": "Este é um relatório descritivo de exemplo para a Universidade Católica.",
                "popup_title": "Universidade Católica (Exemplo Pop-up)",
                "popup_status": "Segurança: Teste\\nAcessibilidade: Teste",
                "popup_rating": "99"
            }

        self.ids.detail_search_input.text = location_data["name"]

        # Atualizando Acessibilidade
        access_layout = self.ids.accessibility_grid # Precisa adicionar id='accessibility_grid' no KV
        # Limpar labels antigos se necessário, ou melhor, ter IDs para cada label de valor/cor
        # Para simplificar, assumindo que os labels de texto fixo já existem e só atualizamos os valores.
        # Exemplo de atualização (isso precisaria ser mais robusto com IDs para cada label no KV):
        # self.ids.rampas_value.text = location_data["accessibility"]["Rampas para cadeirantes"]["value"]
        # self.ids.rampas_value.color = location_data["accessibility"]["Rampas para cadeirantes"]["color"]

        # Atualizando Segurança (similar à acessibilidade)
        # self.ids.bombeiros_value.text = location_data["security"]["Bombeiros"]["value"]
        # self.ids.bombeiros_value.color = location_data["security"]["Bombeiros"]["color"]
        
        self.ids.report_label.text = location_data["report"]

        # Atualizando pop-up do mapa (se visível ou os dados forem para ele)
        self.ids.popup_title.text = location_data["popup_title"]
        self.ids.popup_status.text = location_data["popup_status"]
        self.ids.popup_rating.text = location_data["popup_rating"]
        
        # Você precisaria adicionar IDs aos Labels de Acessibilidade e Segurança no KV_CODE
        # para poder atualizá-los diretamente. Ex:
        # No KV_CODE, para "Rampas para cadeirantes":
        # Label:
        #     id: rampas_value_label
        #     text: '100%' # Placeholder
        #     color: app.accent_color_green
        # E então aqui:
        # self.ids.rampas_value_label.text = location_data["accessibility"]["Rampas para cadeirantes"]["value"]
        # self.ids.rampas_value_label.color = self.get_color_for_value(location_data["accessibility"]["Rampas para cadeirantes"]["value"]) # Função para determinar cor


    def search_location(self, text):
        """
        Método chamado ao pesquisar um local na tela de detalhes.
        Pode ser para refinar a busca ou voltar para a tela principal com novos resultados.
        """
        print(f"Pesquisando (na tela de detalhes) por: {text}")
        # Lógica de busca ou navegação
        # self.manager.get_screen('main_screen').ids.search_input.text = text # Passa o texto de volta
        # self.manager.get_screen('main_screen').search_location(text) # Inicia nova busca na MainScreen
        self.manager.current = 'main_screen'


class TurismoAcessivelApp(App):
    """
    Classe principal do aplicativo Kivy.
    """
    primary_color = PRIMARY_COLOR
    secondary_color = SECONDARY_COLOR
    text_color = TEXT_COLOR
    accent_color_green = ACCENT_COLOR_GREEN
    accent_color_yellow = ACCENT_COLOR_YELLOW
    accent_color_red = ACCENT_COLOR_RED

    def build(self):
        self.title = 'Turismo Acessível DF'
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        detail_screen = DetailScreen(name='detail_screen')
        sm.add_widget(detail_screen)
        
        # Adicionando IDs aos grids para facilitar a atualização de dados
        # Isso é feito aqui programaticamente, mas idealmente os IDs são no KV.
        # No entanto, para popular dinamicamente ou referenciar o widget diretamente:
        # (No KV, já adicionei 'id: report_label', 'id: map_popup', etc.)
        # Para os GridLayouts de acessibilidade e segurança, se você quiser
        # limpar e recriar os itens dinamicamente, você daria IDs a eles no KV:
        # Exemplo para o GridLayout de acessibilidade:
        # GridLayout:
        #     id: accessibility_grid 
        #     cols: 2 
        #     # ...
        # E então em Python:
        # access_grid = detail_screen.ids.accessibility_grid
        # access_grid.clear_widgets()
        # for item_text, item_detail in dados_acessibilidade.items():
        #     access_grid.add_widget(Label(text=item_text, color=self.text_color, ...))
        #     access_grid.add_widget(Label(text=item_detail['value'], color=item_detail['color'], ...))

        return sm

if __name__ == '__main__':
    # Para testes, crie arquivos de imagem de placeholder:
    # logo_turseguro.png (um logo simples)
    # search_icon.png (uma lupa)
    # star_icon.png (uma estrela)
    # Você pode usar sites como FlatIcon para ícones gratuitos.
    
    # Exemplo rápido de como criar imagens placeholder se não as tiver:
    # from PIL import Image as PILImage, ImageDraw, ImageFont
    # import os

    # def create_placeholder_image(filename, text, size=(100,100), bg_color="black", text_color="white"):
    #     if not os.path.exists(filename):
    #         img = PILImage.new('RGB', size, color = bg_color)
    #         d = ImageDraw.Draw(img)
    #         try:
    #             font = ImageFont.truetype("arial.ttf", size[1]//3)
    #         except IOError:
    #             font = ImageFont.load_default()
    #         text_width, text_height = d.textbbox((0,0), text, font=font)[2:]
    #         x = (size[0] - text_width) / 2
    #         y = (size[1] - text_height) / 2
    #         d.text((x,y), text, fill=text_color, font=font)
    #         img.save(filename)
    #         print(f"Criada imagem placeholder: {filename}")

    # create_placeholder_image("logo_turseguro.png", "Logo", size=(200,100))
    # create_placeholder_image("search_icon.png", "🔎", size=(50,50))
    # create_placeholder_image("star_icon.png", "⭐", size=(50,50))
    
    TurismoAcessivelApp().run()
