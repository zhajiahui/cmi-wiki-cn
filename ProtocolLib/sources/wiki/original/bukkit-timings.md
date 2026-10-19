The timings system (introduced in 2.7.2) can measure the amount of processor time consumed per plugin and per packet listener, allowing you to easily track down the offending plugin.

To use it, simply type the following command:

```
/protocol timings
```

Then, when you feel you have collected enough data (ten minutes should do the job), type the command again. That will stop any measurements and write a report to the *plugins/ProtocolLib* folder in the following format:

```
Started: Fri Sep 20 22:29:45 CEST 2013
Stopped: Fri Sep 20 22:34:04 CEST 2013 (after 258 seconds)

=== PLUGIN BlockPatcher ===
 TYPE: ASYNC_SERVER_SIDE 
 ------------------------------- 
 Packet:      Count:       Min (ms):       Max (ms):       Mean (ms):      Std (ms): 
 ------------------------------- 
 51           1700         0,026289        1,455810        0,089500        0,071098 
 56           450          0,078249        14,498720       0,573007        0,898368 
 SUM          2150         0,026289        14,498720       0,190699        0,459703 
 ------------------------------- 
 TYPE: SYNC_SERVER_SIDE 
 ------------------------------- 
 Packet:      Count:       Min (ms):       Max (ms):       Mean (ms):      Std (ms): 
 ------------------------------- 
 23           153          0,000927        0,605583        0,009881        0,048629 
 40           1419         0,014536        32,806608       0,067887        0,881271 
 51           3400         0,000000        0,420938        0,008877        0,015866 
 52           3752         0,000000        0,172891        0,007943        0,010659 
 53           25738        0,000000        0,202583        0,005128        0,007767 
 56           900          0,000000        0,133921        0,007660        0,010720 
 103          57           0,006494        4,320419        0,089899        0,570491 
 104          5            0,034330        0,073301        0,047444        0,016973 
 SUM          35424        0,000000        32,806608       0,008527        0,178486 
 => Time on main thread: 302,057641 ms
 ------------------------------- 

=== PLUGIN ItemRenamer ===
 TYPE: SYNC_SERVER_SIDE 
 ------------------------------- 
 Packet:      Count:       Min (ms):       Max (ms):       Mean (ms):      Std (ms): 
 ------------------------------- 
 103          57           0,021650        1,002397        0,204237        0,125608 
 104          5            1,963967        12,320726       4,423102        4,423919 
 SUM          62           0,021650        12,320726       0,544468        1,624530 
 => Time on main thread: 33,757046 ms
 ------------------------------- 
 TYPE: SYNC_CLIENT_SIDE 
 ------------------------------- 
 Packet:      Count:       Min (ms):       Max (ms):       Mean (ms):      Std (ms): 
 ------------------------------- 
 107          35           0,057836        1,310755        0,132993        0,224260 
 250          1            0,055053        0,055053        0,055053        NaN 
 SUM          36           0,055053        1,310755        0,130828        0,221414 
 ------------------------------- 

=== PLUGIN Sneaky ===
 TYPE: SYNC_SERVER_SIDE 
 ------------------------------- 
 Packet:      Count:       Min (ms):       Max (ms):       Mean (ms):      Std (ms): 
 ------------------------------- 
 40           1419         0,020413        5,317867        0,059587        0,146036 
 => Time on main thread: 84,554204 ms
 -------------------------------
```

The most important figure here is the *time on the main thread*. This is the time each plugin consumes that could otherwise be spent on game ticks. If you're suffering from low TPS, this could be a part of the cause.
