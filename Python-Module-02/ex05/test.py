from TinyStatistician import TinyStatistician

tstat = TinyStatistician()

a = [1, 42, 300, 10, 59]
print(f"for the list = {a}:")
print(f"\tThe mean is : {tstat.mean(a)}")

print(f"\tThe median is : {tstat.median(a)}")


a = [24.1, 24.7, 25.0, 25.2, 25.6, 25.6, 26.1, 27.8]
print(f"for the list = {a}:")
print(f"\tThe median is : {tstat.median(a)}")

a = [1, 42, 300, 10, 59]
print(f"for the list = {a}:")
print(f"\tThe first and third quartiles are : {tstat.quartiles(a)}")

a = [1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61]
print(f"for the list = {a}:")
print(f"\tThe first and third quartiles are : {tstat.quartiles(a)}")


a = [1, 42, 300, 10, 59]
print(f"for the list = {a}:")
print(f"\tThe variance = {tstat.var(a)}")

print(f"\tThe standard deviation = {tstat.std(a)}")
