import time
from datetime import datetime,timedelta


def time_decorator(bs_func):
  def enhanced_func(*args,**kwargs):
    start_time = time.time()
    results = bs_func(*args,**kwargs)
    end_time = time.time()
    print("with decorator,Time to complete the task->", end_time - start_time)
    return results
  return enhanced_func

def brewtea():
  start_time = time.time()
  print("Brewing tea.")
  time.sleep(2)
  print("Tea is ready.")
  end_time = time.time()
  return (end_time - start_time)

@time_decorator
def brewtea_withdecorator():
  print("Brewing tea")
  time.sleep(1)
  print("Tea is ready")

@time_decorator
def make_coffee(coffee_type,timer):
  print(f"Brewing COffee->{coffee_type}")
  time.sleep(timer)
  print("Coffee is Ready.")
  return f"Drink coffee by {datetime.now() + timedelta(minutes=1)}"

# deco_brewtea = time_decorator(brewtea_withdecorator)
# print("Time taken to complete the task->",brewtea())
# deco_brewtea()
brewtea_withdecorator() # functions without argument
make_coffee("Strong",1) # functions with positional arguments
print(make_coffee(coffee_type="Strong",timer=1)) #functions with keyword type arguments