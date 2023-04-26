#! /usr/bin/env python
import sys
last_key = None
min_val = 0.0
max_val = 0.0
sum = 0.0
count = 0
# keys come grouped together so we need to keep track of state a little bit  thus when the key changes, 
# we need to reset our counter, and write out the count we've accumulated
for line in sys.stdin:
   line = line.strip()
   key, value = line.split("\t")
   # we have to be able to deal with missing values
   if value =="NA":
       continue
   value = float(value)
   # if this is the first iteration
   if not last_key:
       last_key = key
        # Update the sum and count variables
        sum = float(value)
        min_val = value
        max_val = value
        count = 1
    # if they're the same, log it
   elif key == last_key:
        if float(value) < min_val:
            min_val = float(value)
        if float(value) > max_val:
            max_val = float(value)
        # Update the sum and count variables
        sum = sum + float(value)
        count = count + 1
   else: 
        result = [last_key, sum/count,min,max]
        print("\t".join(str(v) for v in result))
        last_key = key
        count = 1
        sum = value
# this is to catch the final value that we output
print("\t".join(str(v) for v in [last_key, sum / count, min_val,max_val]))
