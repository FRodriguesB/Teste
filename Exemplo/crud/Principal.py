from agenda import Agenda
import gi
import sqlite3

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("interface.glade")

class InterfaceAgenda():
    def __init__(self):
        self.nomeCaixa = builder.get_object("nomeCaixa")
        self.telefoneCaixa = builder.get_object("telefoneCaixa")
        self.grade = builder.get_object("grade")
        self.lstagenda = builder.get_object("lstagenda")
        self.lb_status = builder.get_object("lb_status")
        self.conexao = sqlite3.connect("banco.db")
        self.cursor = self.conexao.cursor()
        self.ag = Agenda()

        sql_busca = "select * from agenda"
        self.cursor.execute(sql_busca)
        busca_agenda = self.cursor.fetchall()
        self.lstagenda.clear()
        for i in busca_agenda:
            cod = str(i[0])
            nome = i[1]
            telefone = i[2]
            lista_pergunta = (cod, nome,telefone)
            self.lstagenda.append(lista_pergunta)

    def onDestroy(self, *args):
        Gtk.main_quit()

    def btnInserir(self, button):
        self.ag.nome = self.nomeCaixa.get_text()
        self.ag.telefone = self.telefoneCaixa.get_text()              
        self.lb_status.set_text(str(self.ag.inserir()))
        self.nomeCaixa.set_text("")
        self.telefoneCaixa.set_text("")


    def btnAtualizar(self, button):
        self.ag.nome = self.nomeCaixa.get_text()
        self.ag.telefone = self.telefoneCaixa.get_text()              
        self.lb_status.set_text(str(self.ag.atualizar()))
        self.nomeCaixa.set_text("")
        self.telefoneCaixa.set_text("")              
        
        
    def btnApagar(self, button):
        self.ag.nome = self.nomeCaixa.get_text()
        self.ag.telefone = self.telefoneCaixa.get_text()              
        self.lb_status.set_text(str(self.ag.apagar(self.ag.id)))
        self.nomeCaixa.set_text("")
        self.telefoneCaixa.set_text("")

    def btnBuscar(self, button):
        self.ag.nome = self.nomeCaixa.get_text()
        self.lb_status.set_text(str(self.ag.buscar(self.ag.nome)))
        self.telefoneCaixa.set_text(self.ag.telefone)
        
        

builder.connect_signals(InterfaceAgenda())

window = builder.get_object("FrmAgenda")
window.show_all()

Gtk.main()
