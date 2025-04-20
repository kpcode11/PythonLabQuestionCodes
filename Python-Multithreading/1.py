import threading
import time
import random
from queue import Queue

# Shared data structures
order_queue = Queue()
order_status = {}
order_lock = threading.Lock()

class Customer(threading.Thread):
    def __init__(self, customer_id):
        threading.Thread.__init__(self)
        self.customer_id = customer_id
        self.orders = ["Pizza", "Burger", "Pasta", "Salad", "Sandwich"]
    
    def run(self):
        order = random.choice(self.orders)
        order_time = random.randint(1, 3)
        
        # Simulate time taken to decide order
        time.sleep(order_time)
        
        with order_lock:
            order_id = f"ORD-{self.customer_id}-{time.time_ns()}"
            order_queue.put((order_id, order))
            order_status[order_id] = "Placed"
            print(f"Customer {self.customer_id} ordered {order} (Order ID: {order_id})")
        
class Chef(threading.Thread):
    def __init__(self, chef_id):
        threading.Thread.__init__(self)
        self.chef_id = chef_id
    
    def run(self):
        while True:
            if not order_queue.empty():
                order_id, order = order_queue.get()
                
                with order_lock:
                    order_status[order_id] = "Preparing"
                    print(f"Chef {self.chef_id} is preparing {order} (Order ID: {order_id})")
                
                # Simulate cooking time
                cook_time = random.randint(2, 5)
                time.sleep(cook_time)
                
                with order_lock:
                    order_status[order_id] = "Ready"
                    print(f"Chef {self.chef_id} completed {order} (Order ID: {order_id}) in {cook_time} secs")
                
                order_queue.task_done()
            else:
                # No orders left, chefs take a break
                time.sleep(1)

def display_system_status():
    while True:
        with order_lock:
            print("\n=== Current System Status ===")
            print(f"Orders in queue: {order_queue.qsize()}")
            for order_id, status in order_status.items():
                print(f"{order_id}: {status}")
            print("===========================\n")
        time.sleep(3)

def main():
    # Start system status monitor
    status_thread = threading.Thread(target=display_system_status, daemon=True)
    status_thread.start()
    
    # Create chefs
    chefs = [Chef(i+1) for i in range(2)]  # 2 chefs
    for chef in chefs:
        chef.daemon = True
        chef.start()
    
    # Simulate customers placing orders
    customers = [Customer(i+1) for i in range(5)]  # 5 customers
    
    for customer in customers:
        customer.start()
        time.sleep(random.randint(1, 2))  # Stagger customer orders
    
    # Wait for all customers to place orders
    for customer in customers:
        customer.join()
    
    # Wait for all orders to be processed
    order_queue.join()
    
    print("\nAll orders processed! System shutting down.")

if __name__ == "__main__":
    main()