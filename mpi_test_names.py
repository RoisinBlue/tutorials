from mpi4py import MPI
import numpy as np

# to run: mpi_env > folder > 'mpirun -n [core no.] python mpi_test_names.py
# core no. == n_snaps (wont affect this script but important for mpi_test_read +)

# This script prints out the name & location of the test files I'm using for the next 2 scripts

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# The code prints 9 files in total, 3 for each dir

conedirs = [7,8,9]
# directories
conesnaps = [0,1,2]
# files in each directory (this needs to match n_snaps)
n_snaps = len(conesnaps)

batch = rank%n_snaps
# batch is used to assign a file number to each rank
# rank 0 : 0%3 = 0, rank 1: 1%3 = 1, rank 2: 2%3 = 2
# this is a bit redundant for this script, as we could just use 'rank'

for conedir in conedirs:
    
    # each core prints conesnap_000n for conedir_000[7,8,9]
    
    datapath = 'conedir_000{0:d}/'.format(conedir)
    fname = datapath + 'conesnap_000{0:d}.{1:d}'.format(conedir,batch)
    
    print("This is rank no.", str(rank), " File: ", fname)
        