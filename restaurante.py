from lib2to3.pygram import pattern_grammar
from mimetypes import init
from tkinter.tix import Tree


class Restaurente:
    def __init__(self, usuario, chefs):
        self.usuario= usuario
        self.chefs= chefs
    
    class Usuario(Restaurante):
        def __init__(self):
            self 
            super(Restaurente).__init__(self.usuario)
        def solicitar_plato(self,solicitud_plato):
            self.solicitud_plato= solicitud_plato == True
            return solicitud_plato
        def pagar_plato(self,solicitar_plato):
            if solicitar_plato == True:
                return "pagar"
            else:
                return "no pagar"
        def nuevo_pedido(self,pedir_algo_diferente,solicitar_plato):
            self.pedir_algo_diferente= pedir_algo_diferente
            if pedir_algo_diferente == solicitar_plato:
                return "no es posible"
            else: 
                return "su pedido se esta tomando adecuadamente"

    class sub_chefs(chefs):
        def __init__(self) -> None:
            super(Restaurente).__init__(self.verificar)
        def preparar_ingredientes(self, ingredientes):
            self.ingredientes=ingredientes = 0
            if ingredientes > 1: 
                return "se puede hacer"
            else :
                return "no se puede hacer"
        def cocinar_armar(self,pedido,preparar_pedido):
            self.pedido= pedido == True
            self.preparar_pedido = preparar_pedido
            if pedido is True:
                return preparar_pedido
            else: 
                return "no es posiblre"
        def mirar(self, ingredientes):
            self.ingredientes=ingredientes
            if ingredientes is True:
                return " hay ingredientes "
            else:
                return "no hay ingredientes "
        def informar(self,ingredientes,informe):
            self.informe= informe == "su informe se esta realizando"
            if ingredientes is False:
                return informe
            else: 
                return "nada"
               


    class chefs(Restaurente):
        def __init__(self):
            self 
            super(Restaurente).__init__(self.chefs)
        def verifica(self,verificacion, pedido):
            self.verificacion = verificacion
            if pedido is True:
                return verificacion
            else:
                return "no existe verificacion del plato"
         

