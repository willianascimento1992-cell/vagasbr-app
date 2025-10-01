main_content = '''
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class CardVaga(MDCard):
    titulo = StringProperty("")
    empresa = StringProperty("")
    localidade = StringProperty("")
    salario = StringProperty("")

KV = '''
<CardVaga>:
    orientation: "vertical"
    padding: "10dp"
    size_hint_y: None
    height: "120dp"

    MDLabel:
        text: root.titulo
        theme_text_color: "Primary"
        font_style: "H6"

    MDLabel:
        text: root.empresa
        theme_text_color: "Secondary"
        font_style: "Subtitle1"

    MDLabel:
        text: root.localidade + " | " + root.salario
        theme_text_color: "Hint"
        font_style: "Body2"


ScreenManager:
    TelaBusca:
        name: "busca"

<TelaBusca>:
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Vagas BR - Buscar"
            elevation: 10
            
        MDBoxLayout:
            orientation: "vertical"
            padding: "20dp"
            spacing: "20dp"
            
            MDTextField:
                id: input_cargo
                hint_text: "Digite o cargo (ex: pedreiro)"
                mode: "fill"
                
            MDTextField:
                id: input_cidade
                hint_text: "Digite a cidade (ex: valinhos)"
                mode: "fill"
                
            MDRaisedButton:
                text: "🔍 BUSCAR VAGAS"
                on_release: root.buscar_vagas()
                pos_hint: {"center_x": 0.5}
                md_bg_color: "teal"

            MDLabel:
                id: resultado
                text: "Digite cargo e cidade para buscar vagas"
                halign: "center"
                theme_text_color: "Secondary"
'''

class TelaBusca(MDScreen):
    def buscar_vagas(self):
        cargo = self.ids.input_cargo.text
        cidade = self.ids.input_cidade.text
        
        if cargo and cidade:
            resultado = f"Buscando '{cargo}' em '{cidade}'...\\n\\n✅ App funcionando perfeitamente!\\n📱 APK compilado via GitHub"
            self.ids.resultado.text = resultado
        else:
            self.ids.resultado.text = "⚠️ Por favor, preencha cargo e cidade"

class VagasBR(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

if __name__ == "__main__":
    VagasBR().run()
'''

print("📋 ARQUIVO 5: main.py")
print("🎯 COMO CRIAR NO GITHUB:")
print("1. Clique 'Add file' → 'Create new file'")
print("2. Nome do arquivo: main.py")
print("3. Cole o conteúdo acima")
print("4. Commit: 'Adicionando app principal'")
print("5. Clique 'Commit new file'")
