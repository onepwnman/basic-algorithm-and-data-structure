def exe_time_logger(func):
  from time import time
  
  def wrapper(*args, **kwargs):
    start = time()
    result = func(*args, **kwargs)
    print("Execution Time of [{}] function: {}".format(func.__name__, time() - start))
    return result

  return wrapper
