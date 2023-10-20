import util
import DeliveryDB
from Delivery import Delivery
deliveryrepository = DeliveryDB.repository


from Ordered import Ordered

def wheneverOrdered_StartDelivery(data):
    event = Ordered()
    event = util.AutoBinding(data, event)
    
    delivery = Delivery()
    deliveryrepository.save(delivery)
    
from OrderCancelled import OrderCancelled

def wheneverOrderCancelled_CancelDelivery(data):
    event = OrderCancelled()
    event = util.AutoBinding(data, event)
    
    delivery = Delivery()
    deliveryrepository.save(delivery)
    

