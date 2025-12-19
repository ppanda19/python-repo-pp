
class FileLogger:
  def write(self)->None: # Function returns Nothing (->)
    print("Write to File")

class DbLogger:
  def write(self)->None:
    print("Write to DB")

class OrderService:
  def __init__(self,logger):
    self.logger = logger
  
  def process_order(self) -> None:
    print("Processing Order")
    self.logger.write()
    
file_logger = FileLogger()
db_logger = DbLogger()

OrderService_file = OrderService(file_logger) # Dependency Injection
OrderService_file.process_order()

OrderService_db = OrderService(db_logger)
OrderService_db.process_order()

