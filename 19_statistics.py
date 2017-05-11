import statistics

example_list = [4, 2,1, 32, 5, 88, 123, 3,43 , 1]
x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.mode(example_list)
dev = statistics.stdev(example_list)
var = statistics.variance(example_list)
print(x, y, z, dev, var)
