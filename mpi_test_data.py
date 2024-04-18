from mpi4py import MPI
import numpy as np
import os.path
import h5py

# To run: mpi_env > folder > 'mpirun -n [core no.] python mpi_test_data.py
# !!!!!!! core no. == n_snaps !!!!!!!!!!!

comm = MPI.COMM_WORLD
root = 0
n_cpus = MPI.COMM_WORLD.Get_size()
this_rank = comm.rank
#p = comm.Get_size()
#size = comm.Get_size()

conedirs = [7,8,9]
conesnaps = [0,1,2]
n_snaps = 3 #number of cores should match number of conesnaps 
# Below vals are for test run over 0 conesnaps only
#conedirs = [7]
#conesnaps = [0]
#n_snaps = 1

batch = this_rank%n_snaps

def read_header(fname):
    with h5py.File(fname,'r') as fi:
        h = fi['Header']
        nparts = h.attrs['NumPart_ThisFile'][1]
        print('Nparts={0:d}'.format(nparts))
    return nparts

def read_G4_files(fname, nparts):
    # Defining data type
    vect = np.dtype([('x', np.float32),('y', np.float32),('z', np.float32)])
    part = np.dtype([('pos', vect),('vel', vect),('ID', np.ulonglong), ('z', np.float32), ('r', np.float32),('RA', np.float32),('Dec', np.float32)])
    
    # Setting up arry to read G4 data into 
    po = np.empty((nparts,3), dtype=np.float32)
    ve = np.empty((nparts,3), dtype=np.float32)
    
    if os.path.exists(fname) == True:
        with h5py.File(fname,'r') as f:
            # Collecting data from hdf5 file
            p = f['PartType1/Coordinates']
            v = f['PartType1/Velocities']
            
            # Reading into array
            p.read_direct(po)
            v.read_direct(ve)
            
            # Separating into 6 compnents so rest of new_LC runs smoothly
            xPos, yPos, zPos = po[:,0], po[:,1],po[:,2]
            xVel, yVel, zVel = ve[:,0], ve[:,1],ve[:,2]
            # No need to delete first entry for G4 files
            #xPos = np.delete(xPos, 0)
            #yPos = np.delete(yPos, 0)
            #zPos = np.delete(zPos, 0)
            #xVel = np.delete(xVel, 0)
            #yVel = np.delete(yVel, 0)
            #zVel = np.delete(zVel, 0)
            
            print('reading ', fname,' ok')
            
            return xPos, yPos, zPos, xVel, yVel, zVel
    else:
        print('ERROR: ' + fname + ' not found')
        return 0, 0, 0, 0, 0, 0

for conedir in conedirs:
    
    datapath = '/Users/roisinoconnor/mpi_testing/conedir_000{0:d}/'.format(conedir)
    fname = datapath + 'conesnap_000{0:d}.{1:d}.hdf5'.format(conedir,batch)
    
    nparts = read_header(fname)
    
    xPos, yPos, zPos, xVel, yVel, zVel = read_G4_files(fname, nparts)
    
    print(xPos[0:3],yPos[0:3],zPos[0:3],xVel[0:3],yVel[0:3],zVel[0:3])
    