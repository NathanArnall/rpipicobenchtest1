#Raspberry Pi Pico Benchmark
from machine import freq
from time import sleep, ticks_cpu, ticks_ms
loops = 1000 # Iterations to run through
clockspeedmhz = 50 # Clockspeed of CPU in MHz. Recommended range is 20-270
machine.freq(clockspeedmhz*1000000) # Set CPU speed in Hz
initcputicks = ticks_cpu() # Grabs current number of ticks the CPU has ran through after powered on
print("Initial ticks: " + str(ticks_cpu()))
currentticks = ticks_cpu() - initcputicks # Creates a relative tick count (treat this as 0)
loopct = 0
initms = ticks_ms()
def bench():
    # Start benchmarking code
    print ("Your code should go here") # Or leave this as the benchmark
    # End benchmarking code
    
while loopct < loops + 1:
    loopct += 1
    bench()
    currentticks = ticks_cpu() - initcputicks
    # Printing 1 line costs a lot of ticks (30 each non-empty print + ~2 ticks per character)
    #print("Current ticks: " + str(currentticks))
    #print("Current loops: " + str(tickct))
    #print("Average ticks per benchmark): " + str((currentticks)/tickct))

# Clear some space and dump those stats
print ()
print ()
print ()
print ()
print ()
print(str(loops) + " loops took " + str(currentticks) + " ticks to complete and " + str((ticks_ms() - initms)/1000) + " seconds")
print("You averaged " + str((currentticks)/loops) + " ticks per loop")
print("CPU Stats: " + str(machine.freq()/1000000) + " MHz")
