import util
import OrderDB
from Order import Order
orderrepository = OrderDB.repository


from StockIncreased import StockIncreased

def wheneverStockIncreased_NotifyToWaitingUsers(data):
    event = StockIncreased()
    event = util.AutoBinding(data, event)
    
    order = Order()
    orderrepository.save(order)
    
from DeliveryReturned import DeliveryReturned

def wheneverDeliveryReturned_UpdateOrderStatus(data):
    event = DeliveryReturned()
    event = util.AutoBinding(data, event)
    
    order = Order()
    orderrepository.save(order)
    

