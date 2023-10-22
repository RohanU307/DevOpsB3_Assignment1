
import shutil
from datetime import date
import datetime

def take_backup (src_file_name, dst_file_name=None, src_dir='D:/Backup_python_src/', dst_dir='D:/Backup_python_dest/'):
    
    today = date.today()
    date_format =today.strftime("%d_%b_%Y_")

    src_dir=src_dir+src_file_name
    
    if dst_file_name is None or not dst_file_name:
        dst_file_name = src_file_name
        dst_file_name = dst_dir+date_format+dst_file_name
    
    
    shutil.copy2(src_dir,dst_file_name)
    print("Backup Successful")

take_backup("New Text Document.txt")