# https://www.youtube.com/watch?v=IEEhzQoKtQU&pbjreload=10
# Threading is different from multi-processing. Threading can speed up our script when it's IO bound, while
# multiprocessing can speed up when its CPU bound. Even threading can slow down our processing speed because it has
# an extra overhead of creating and destroying the thread. So one should know when to use one or another.




# Using threading module.
import threading
t1 = threading.Thread(target = some_function, args = [])
t1.start()      # to start t1 thread concurrently with our main thread.
t1.join()       # wait our main thread to complete t1 thread and join it back to main thread.





#---------------------------------------------------------------------------------------------------------#


# Using thread pool executors (concurrent.futures)
# We dont have to join our threads as this executor automatically waits for our thread to complete.

import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:         # It Will wait till all threads complete execution.
    f1 = executor.submit(some_function, arg1, arg2, ...)          # It will return a future object.
    print(f1.result())    # return value of some_function.

    fobjects = [executor.submit(some_function) for _ in range(10)]
    for f in concurrent.futures.as_completed(fobjects):
        print(f.result())

 print('Done')    # It will print after all the threads gets completed.
