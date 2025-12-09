import glob
import os
import pandas as pd
import numpy as np

#Change this according to your structure of CryoVirusDB directoryor 
#comment this line if project dir has not changed
project_dir = '/bml/CryoEM/CryoVirusDB/'




empiar_ids = ['10192','11060','10203','10033','10652','10341','10193','10205','10555']
#Put corresponding particle diameter of each empiar id in pixel
# Divide Diameter in Angstron by Pixel Spacing
particle_diameters = [470, 516, 377, 350, 374, 376, 516, 310, 564]   #Example diameters of EMPIAR IDs

for j in range(len(empiar_ids)):
    filename = glob.glob(project_dir + empiar_ids[j] + '/ground_truth/*_particles_selected.csv')[0]
    # print(filename)
    # print(empiar_ids[j])
    # print(particle_diameters[j])
    directory = filename.replace(filename.split('/')[-1], '')
    df = pd.read_csv(filename)
    # df['Diameter'] = np.array([particle_diameters[j] for k in range(len(df['X-Coordinate']))])
    files = df['Micrographs Filename'].unique()
    print("Number of Micrographs for "+ empiar_ids[j] , len(files))
    # for f in files:
    #     f_name = f[:-4]
    #     df_coord = df[df['Micrographs Filename'] == f]
    #     df_box = df_coord.loc[:, ['X-Coordinate', 'Y-Coordinate', 'Diameter', 'Angle-Psi', 'Origin X (Ang)', 'Origin Y (Ang)', 'Defocus U', 'Defocus V', 'Defocus Angle', 'Phase Shift', 'CTF B Factor']]
    #     df_box.to_csv(directory + "particle_coordinates/" + f_name + '.csv', index=False)
    # print("Completed for "+ empiar_ids[j])