from mpi4py import MPI
import numpy as np
import os.path

# to run: mpi_env > folder > 'mpirun -n [core no.] python mpi_test_read.py
# !!!!!!! core no. == n_snaps !!!!!!!!!!!
# if core no. not set correctly, will read 0 conesnaps multiple times

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


#conedirs = [7,8,9]
conedirs = [7,8,9,10]
# If you run with the [7,8,9,10] list you'll get the error statment
conesnaps = [0,1,2]
n_snaps = len(conesnaps)

batch = rank%n_snaps

def read_G4_files(fname):
    if os.path.exists(fname) == True:
        print("This is rank no.", str(rank), " File: ", fname, " found")
    else:
        print("This is rank no.", str(rank), "!!ERROR!! File: ", fname, " found")

for conedir in conedirs:
    
    #datapath = '!!!FILE LOCATION!!!/mpi_testing/conedir_000{0:d}/'.format(conedir)
    # change the datapath to the location on your laptop
    datapath = '/Users/roisinoconnor/mpi_testing/conedir_000{0:d}/'.format(conedir)
    
    fname = datapath + 'conesnap_000{0:d}.{1:d}.hdf5'.format(conedir,batch)
    
    read_G4_files(fname)
    