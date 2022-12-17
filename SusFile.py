import math
import os.path
import magic


class SusFile:
    def __init__(self, path):
        self.path = str(path)
        self.file_name = os.path.basename(self.path)
        self.meta_data = os.stat(self.path)
        self.size = os.path.getsize(self.path)
        self.meta_data_size = ''
        self.date_modified = ""

        # self.snap_diff_size = [1,2,3,4,5,6,7,8,9,10]
        # self.date_modified = ""
        # self.date_modified = ""
        # self.is_encrypted = True
        # self.signature = ''

        self.grade = 100  # start by suspect. 100 is severe.
        # self.next_snap_grade = self.grade  # start by suspect. 100 is severe.

    def get_size(self):
        return self.size

    def collect_metadata_content(self):
        self.meta_data_size = self.meta_data.st_size
        self.date_modified = self.meta_data.st_mtime

    def compare(self, old_file, new_file):
        self.compare_size(old_file, new_file)
        self.compare_metadata(old_file, new_file)
        self.compare_time_modified(old_file, new_file)

    def compare_size(self, old_file, new_file):
        # Compare the metadata for each file
        if old_file.get_size() != new_file.size:
            pass
        else:
            self.grade -= 10
        return

    def compare_metadata(self, old_file, new_file):
        # Compare the metadata for each file
        if old_file.meta_data_size != new_file.meta_data_size:
            pass
        else:
            self.grade -= 10

        return new_file.size - old_file.get_size()

    def compare_time_modified(self, old_file, new_file):
        # Compare the metadata for each file
        if old_file.date_modified != new_file.date_modified:
            pass
        else:
            self.grade -= 10

    def compare_file_format(self):
        # Compare the metadata for each file
        file_format = magic.from_file(self.path)
        if file_format != "data":
            self.grade -= 20
        else:
            pass

    def compare_antropy(self):
        with open(self.path, 'rb') as file:
            data = file.read()
        ent = 0.0
        if len(data) < 2:
            return ent
        size = float(len(data))
        for b in range(256):
            freq = data.count(b)
            if freq > 0:
                freq = float(freq) / size
                ent = ent + freq * math.log(freq, 2)
                # print(-ent / 8 > 0.8)
        if (-ent / 8) > 0.8:  # Antropy return true if infected
            pass
        else:
            self.grade -= 50
        return (-ent / 8) > 0.8
