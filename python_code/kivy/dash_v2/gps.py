#-*- coding: utf-8 -*-
from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from kivy.uix.popup import Popup
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
import json
import kivy.garden.mapview

kv = '''
#:import C kivy.utils.get_color_from_hex
#:import sys sys
#:import MapSource mapview.MapSource

BoxLayout:
    canvas:
        Color:
            rgb: C('#ffffff')
        Rectangle:
            pos: self.pos
            size: self.size
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        MapView:
            lat: app.app_lat
            lon: app.app_long
            zoom: 13
            map_source: MapSource(sys.argv[1], attribution="") if len(sys.argv) > 1 else "osm"
            MapMarkerPopup:
                lat: app.app_lat
                lon: app.app_long
                # lat: app.on_location(self.lat)
                # lon: app.on_location(self.long)
                popup_size: dp(230), dp(130)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        Label:
                            text: "[b]Você está aqui![/b]"
                            markup: True
                            halign: "center"
    BoxLayout:
        assunto: assunto
        orientation: 'vertical'
        padding: [30, 30, 30, 100]
        spacing: 10
        Spinner:
            id: assunto
            text: 'Selecionar Assunto'
            background_color: C('#1180c4')
            background_normal: ''
            values: ('Buraco e Pavimentação', 'Calçadas guias e Postes', 'Ciclovias, Faixas e outros', 'Semáforos, sinalização e outros.', 'Iluminação Pública')
            size_hint_y: None
            height: '40dp'

        BoxLayout:
            orientation: 'horizontal'
            height: '40dp'
            size_hint_y: None
            ToggleButton:
                text: 'Ler Localizacao' if self.state == 'normal' else 'Parar Leitura'
                on_state:
                    app.start(1000, 0) if self.state == 'down' else \
                    app.stop()
            Button:
                text: 'Salvar'
                on_press: app.salvarLocalizacao()
'''

class GpsTest(App):
    gps_get = StringProperty()
    gps_location = StringProperty()
    gps_status = StringProperty()
    detail_text = StringProperty()

    app_lat = 50.6394 #i placed this default values here but you can take them out and use '' instead when u are ready
    app_long = 3.057 #i placed this default values here but you can take them out and use '' instead when u are ready

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)

        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'Por favor, ative o GPS'
        return Builder.load_string(kv)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread
    def on_location(self, **kwargs):
        self.lat = kwargs.get('lat')
        self.long = kwargs.get('lon')

        self.app_lat = self.lat
        self.app_long = self.long


    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)
        pass

    def salvarLocalizacao(self):

        if self.root.ids.assunto.text == "Buraco e Pavimentação":
            self.assunto = "pavimentacao"
        elif self.root.ids.assunto.text == "Calçadas guias e Postes":
            self.assunto = "calcadasguias"
        elif self.root.ids.assunto.text == "Ciclovias, Faixas e outros":
            self.assunto = "cicliovia"
        elif self.root.ids.assunto.text == "Semáforos, sinalização e outros.":
            self.assunto = "semaforos"
        else:
            self.assunto = "iluminacao"

        self.localizacao = "POINT(" + self.gps_location + ")"
        self.params = json.dumps({"assunto": self.assunto, "localizacao": self.localizacao})
        self.headers = {'Content-type': 'application/json',
                        'Accept': 'application/json; charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
        self.req = UrlRequest('http://aaa.aaa.com:9000/api/add/', req_body=self.params, req_headers=self.headers, on_success=self.postSucess, on_error=self.postFail)

    def postSucess(self, req, result):
        text = Label(text="Enviado com sucesso!".format())
        pop_up = Popup(title="Sucesso", content=text, size_hint=(.7, .7))
        pop_up.open()

    def postFail(self, req, result):
        text = Label(text="Erro de conexão, verifique sua internet!".format())
        pop_up = Popup(title="Erro de conexão", content=text, size_hint=(.7, .7))
        pop_up.open()

if __name__ == '__main__':
    GpsTest().run()