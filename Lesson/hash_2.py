from hash_distribution import plot, distribute
from string import printable

plot(distribute(printable, num_containers=2))

plot(distribute(printable, num_containers=5))
