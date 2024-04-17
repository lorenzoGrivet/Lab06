from database import DAO

class Model:
    def __init__(self):
        self.products= DAO.DAO().getProductsDao()
        self.retailers = DAO.DAO().getRetailerDao()


    def getProducts(self):
        return self.products

    def getRetailers(self):
        return self.retailers