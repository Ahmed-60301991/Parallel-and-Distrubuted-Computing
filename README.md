1) Synchronization Metrics Used

    RLock: Prevents race conditions when multiple threads share  data (latest_temperatures and temperature_averages). Prevents unsafe updates by allowing a thread  to grab the lock again if it needs to.
    Condition: Used for thread coordination, to update  temperatures every 1 second and averages every 5 seconds without the need to poll constantly.

2)  Why No Metrics Were Required?

The professor did not ask for metrics because the lab concentrates on showing correct synchronization behaviour not on optimizing  performance. The task is rather basic and deterministic and thus performance bottlenecks are unlikely. Measures such  as execution time or lock contention are usually more important in high concurrency or high performance systems. Here the  goal is to make sure that shared data access is synchronized correctly not to measure system efficiency