from config import *


class LogicalPage:
    def __init__(self, physical_disk, current_time):
        self.allocation_time = current_time
        self.physical_page = None
        self.physical_disk = physical_disk
        self.physical_disk.reallocate_to_new_page(self)

    def set_physical_page(self, physical_page):
        self.physical_page = physical_page

    def update(self, update_time):
        self.physical_disk.reallocate_to_new_page(self)
