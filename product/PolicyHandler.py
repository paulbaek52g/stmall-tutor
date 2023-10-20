import util
import ProductDB
from Product import Product
productrepository = ProductDB.repository


from DeliveryCompleted import DeliveryCompleted

def wheneverDeliveryCompleted_StockDecrease(data):
    event = DeliveryCompleted()
    event = util.AutoBinding(data, event)
    
    product = Product()
    productrepository.save(product)
    
from DeliveryReturned import DeliveryReturned

def wheneverDeliveryReturned_StockIncrease(data):
    event = DeliveryReturned()
    event = util.AutoBinding(data, event)
    
    product = Product()
    productrepository.save(product)
    

