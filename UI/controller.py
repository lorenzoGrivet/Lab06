import flet as ft
from database import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleTop(self,e):
        self._view.lv.clean()

        lista= DAO.DAO().getTop5(self._view.ddAnno.value,self._view.ddBrand.value,self._view.ddRetailer.value)
        for a in lista:
            self._view.lv.controls.append(ft.Text(a))
            self._view.update_page()
        return lista

    def handleAnalizza(self,e):
        pass
