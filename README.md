# SlowList [![Build Status](https://travis-ci.com/simeg/SlowList.svg?branch=master)](https://travis-ci.com/simeg/SlowList) [![codecov](https://codecov.io/gh/simeg/slowlist/branch/master/graph/badge.svg)](https://codecov.io/gh/simeg/slowlist)

A simple List type that stores its data within a String.

_Written for fun and should not be used for anything really_

## Benchmarks

```
List      	Function        	Description                                     N       Result
------------------------------------------------------------------------------------------------------
Native    	constructor     	new instance with 100 strings                   10000	  7.07ms
SlowList  	constructor     	new instance with 100 strings                   10000	  1926.76ms
------------------------------------------------------------------------------------------------------
Native    	constructor     	new instance with 100 ints                      10000 	5.95ms
SlowList  	constructor     	new instance with 100 ints                      10000	 	1499.77ms
------------------------------------------------------------------------------------------------------
Native    	constructor     	new instance using of() with 100 strings        10000 	6.40ms
SlowList  	constructor     	new instance using of() with 100 strings        10000 	1868.80ms
------------------------------------------------------------------------------------------------------
Native    	constructor     	new instance using of() with 100 ints           10000 	5.77ms
SlowList  	constructor     	new instance using of() with 100 ints           10000	  1447.82ms
------------------------------------------------------------------------------------------------------
Native    	add             	add strings to list                             10000 	1.00ms
SlowList  	add             	add strings to list                             10000	  28.26ms
------------------------------------------------------------------------------------------------------
Native    	add             	add ints to list                                10000	  3.25ms
SlowList  	add             	add ints to list                                10000	  41.65ms
------------------------------------------------------------------------------------------------------
Native    	add_at          	add_at fixed position with string               10000	  21.93ms
SlowList  	add_at          	add_at fixed position with string               10000	  684.87ms
------------------------------------------------------------------------------------------------------
Native    	add_at          	add_at fixed position with int                  10000	  21.45ms
SlowList  	add_at          	add_at fixed position with int                  10000	  183.11ms
------------------------------------------------------------------------------------------------------
Native    	contains        	contains with string                            10000	  1.19ms
SlowList  	contains        	contains with string                            10000	  106.24ms
------------------------------------------------------------------------------------------------------
Native    	contains        	contains with int                               10000	  0.96ms
SlowList  	contains        	contains with int                               10000	  94.71ms
------------------------------------------------------------------------------------------------------
Native    	get             	get last element of list of size 100            10000	  0.46ms
SlowList  	get             	get last element of list of size 100            10000	  104.16ms
------------------------------------------------------------------------------------------------------
Native    	index_of        	index_of last string in list of size 100        10000	  15.42ms
SlowList  	index_of        	index_of last string in list of size 100        10000	  10365.40ms
------------------------------------------------------------------------------------------------------
Native    	index_of        	index_of last int in list of size 100           10000	  16.63ms
SlowList  	index_of        	index_of last int in list of size 100           10000	  7364.60ms
------------------------------------------------------------------------------------------------------
Native    	last_index_of   	last_index_of las string in list of size 100    10000	  9.85ms
SlowList  	last_index_of   	last_index_of las string in list of size 100    10000	  295.06ms
------------------------------------------------------------------------------------------------------
Native    	last_index_of   	last_index_of last int in list of size 100      10000	  9.08ms
SlowList  	last_index_of   	last_index_of last int in list of size 100      10000	  225.17ms
------------------------------------------------------------------------------------------------------
Native    	remove          	remove last string in list of size 100          10000	  21.70ms
SlowList  	remove          	remove last string in list of size 100          10000	  12636.32ms
------------------------------------------------------------------------------------------------------
Native    	remove          	remove last string in list of size 100          10000	  21.24ms
SlowList  	remove          	remove last string in list of size 100          10000	  9124.89ms
------------------------------------------------------------------------------------------------------
Native    	remove_at       	remove_at last int in list of size 100          10000	  6.34ms
SlowList  	remove_at       	remove_at last int in list of size 100          10000	  2270.03ms
------------------------------------------------------------------------------------------------------
Native    	size            	size with string list of size 100               10000	  0.80ms
SlowList  	size            	size with string list of size 100               10000	  9.06ms
------------------------------------------------------------------------------------------------------
Native    	size            	size with int list of size 100                  10000	  0.94ms
SlowList  	size            	size with int list of size 100                  10000	  7.40ms
------------------------------------------------------------------------------------------------------
Native    	set             	set last string in list of size 100             10000	  0.48ms
SlowList  	set             	set last string in list of size 100             10000	  427.26ms
------------------------------------------------------------------------------------------------------
Native    	set             	set last int in list of size 100                10000	  0.55ms
SlowList  	set             	set last int in list of size 100                10000	  430.91ms
------------------------------------------------------------------------------------------------------
Native    	to_string       	to_string string list of size 100               10000	  9.19ms
SlowList  	to_string       	to_string string list of size 100               10000	  43.74ms
------------------------------------------------------------------------------------------------------
Native    	to_string       	to_string int list of size 100                  10000	  269.77ms
SlowList  	to_string       	to_string int list of size 100                  10000	  38.11ms
```

### Conclusion

As you can see SlowList is .. slow.

Notice the last test where **SlowList is actually faster than the native list.**
If the native List type had a dedicated `to_string()` method it would probably
be faster than SlowList though.

This was a fun project. Sometimes you just need to work on a project without
any usage.
