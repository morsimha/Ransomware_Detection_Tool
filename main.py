# IMPORTS
import os
from pathlib import Path
from SusFile import SusFile

# TOGA TOGA TOGA
abs_path = Path(r'C:\Users\morsimha\OneDrive - Intel Corporation\Desktop\Hacathon toga\Flash')

vols = list(os.listdir(abs_path))
snaps = []

for x in (range(10)):
    snaps.append(f'snapshot_{x+1}')

data = {}

diff_list = []
vol1 = []
vol2 = []
vol3 = []

infected_vols = [vol1, vol2, vol3]

vol1_log = []
vol2_log = []
vol3_log = []

infected_vols_logs = [vol1_log, vol2_log, vol3_log]
i = 0
curr_infected_list_log = infected_vols_logs[i]

curr_infected_list = infected_vols[i]
old_snap = ""

# Organizing the information in such a way that each file can be accessed
for vol in vols:
    data[f'{vol}'] = {}
    for snap in snaps:
        data[f'{vol}'][f'{snap}'] = {}
        # Enter all the file names in the database
        for filename in os.listdir(abs_path / str(vol) / str(snap)):
            current_path = abs_path / str(vol) / str(snap) / str(filename)
            current_size = os.path.getsize(current_path)

            # Add susFile object to dictionary
            data[f'{vol}'][f'{snap}'][f'{filename}'] = SusFile(current_path)  # init new file obj
            currFile = data[f'{vol}'][f'{snap}'][f'{filename}']
            currFile.collect_metadata_content()
            # Checking whether the group also exists in the previous snap for comparison
            if not snap == 'snapshot_1':
                old_path = abs_path / str(vol) / str(old_snap) / str(filename)
                if os.path.exists(old_path):
                    old_file = data[f'{vol}'][f'{old_snap}'][f'{filename}']
                    currFile.compare(old_file, currFile)
                    # Checks per file
                    currFile.compare_file_format()
                    if currFile.grade != 70:  # No changes at all
                        currFile.compare_antropy()

                    if currFile.grade > 70:
                        msg = currFile.file_name
                        if msg not in curr_infected_list:
                            print(msg)
                            curr_infected_list.append(msg)
                            msg = "{:20s} \t Infect at \t{:20s}".format(currFile.file_name, snap)
                            curr_infected_list_log.append(msg)

        # end of snapshot run
        old_snap = str(snap)

    with open(f"{vol}_file_list.txt", "w") as f:
        for line in curr_infected_list:
            f.writelines(f'{line}\n')
        f.writelines(f'Number of files in current vol: {len(curr_infected_list_log)}\n')

    with open(f"{vol}_log_file.txt", "w") as f:
        for line in curr_infected_list_log:
            f.writelines(f'{line}\n')
        f.writelines(f'Number of files in current vol: {len(curr_infected_list_log)}\n')

    i += 1
    if i < 3:
        curr_infected_list = infected_vols[i]
        curr_infected_list_log = infected_vols_logs[i]
