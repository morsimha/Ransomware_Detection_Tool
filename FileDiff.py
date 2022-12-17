from SusFile import SusFile


class FileDiff:
    def __init__(self, old_path, new_path):
        self.old_file = SusFile(old_path)
        self.new_file = SusFile(new_path)
        self.metadata_size_diff = 0
        self.last_date_modified = ""
        self.first_infected = ""
        self.new_grade = 100

        self.snap_diff_size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.date_modified = ""
        self.date_modified = ""
        self.is_encrypted = True
        self.signature = ''
        self.old_file = ''
        self.new_file = ''

    # def compare(self):
    #     self.compare_size()
    #     self.compare_metadata()
    #
    #     return []  # if there is something return not empty list
    #
    #     # will return fileDiff obj
    #
    # def compare_size(self):
    #     # Compare the metadata for each file
    #     if self.old_file.get_size() = 0:
    #         print("Watch! Files are different sizes.")
    #     else:
    #         self.new_grade -= 1
    #
    # def compare_metadata(self):
    #     # Compare the metadata for each file
    #     if self.old_file.meta_data_size != self.new_file.meta_data_size:
    #         print("Watch! Files are different sizes.")
    #     else:
    #         self.new_grade-=1
    #
    # def compare_time_modified(self):
    #     # Compare the metadata for each file
    #     if self.old_file.date_modified != self.new_file.date_modified:
    #         print("Watch! Files were modified at different times.")
    #     else:
    #         self.new_grade -= 1
