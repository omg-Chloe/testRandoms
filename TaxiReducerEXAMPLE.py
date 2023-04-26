#! /usr/bin/env python
import sys
last_key = None
count = 0
sum=1
min = 0
max = 0
# keys come grouped together  so we need to keep track of state a little bit thus when the key changes , we need to reset
# our counter, and write out the count we've accumulated

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
       count = 1 
       min=value
       max=value
       sum=value


    # if they're the same, log it
   elif key == last_key:
        count = count + 1 
        if value < min:
            min =value  
        if value > max:
            max=value
        sum = sum + value

   else: 
        result = [last_key, min, max, sum/count]
        print("\t".join(str(v) for v in result))
        last_key = key
        count = 1
        sum=value
        min = value
        max = value
            
# this is to catch the final value that we output
print("\t".join(str(v) for v in [last_key, min, max, sum/count]))
