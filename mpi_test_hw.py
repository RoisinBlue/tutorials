from mpi4py import MPI
import numpy as np

# to run: mpi_env > folder > 'mpirun -n [core no.] python mpi_test_hw.py

# This is a really simple "Hello World" script, to check everything is working ok

comm = MPI.COMM_WORLD
# comm = the 'communicator', it is used for all communication between cores 
size = comm.Get_size()
# size = number of cores
rank = comm.Get_rank()
# rank = which core it's running on

print("This is rank no.", str(rank))

# cores start at 0, so if you set core no. = 4, you will have ranks 0, 1, 2 & 3

print("Hello world from core", str(rank + 1), "of", str(size))

# when testing it's often useful to have the code print out info, like which core is doing what
# remember to double check wether you're printing the 0 > (n - 1) number or the 1 > n number

