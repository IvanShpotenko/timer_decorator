# timer decorator

A decorator timer, which can be used to measure the performance of the function/method.  
It uses two ways to measure performance:  
  1) [time.process_time()](https://docs.python.org/3/library/time.html#time.process_time)  
  2) [time.perf_counter()](https://docs.python.org/3/library/time.html#time.perf_counter)  
In short, .perf_coutnter() counts overall time elapsed, while the .process_time() does not include time, when CPU was not active. For instance, it does not counts time when function waited for some kind of pesponse (like HTTP ones).
