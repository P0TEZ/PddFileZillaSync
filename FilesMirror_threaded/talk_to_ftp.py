import os
from ftplib import FTP, FTP_TLS, error_perm
from logger import Logger


class TalkToFTP:
    def __init__(self, ftp_website):
        my_srv = ftp_website.split(",")
        self.host = my_srv[0]
        self.user = my_srv[1]
        self.password = my_srv[2]
        self.directory = my_srv[3]
        if len(my_srv) == 5:
            self.port = int(my_srv[4]) or 21
        self.ftp = None

    def connect(self):
        self.ftp = FTP()
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.user, self.password)

    def disconnect(self):
        self.ftp.quit()

    def go_to(self, folder_path):
        self.ftp.cwd(folder_path)

    def create_folder(self, folder):
        try:
            folder = self.change_separator(folder)
            self.ftp.mkd(folder)
            Logger.log_info("Folder created : " + folder)
        except error_perm as e:
            Logger.log_warning("Folder created : " + folder + " " + str(e))


    def remove_folder(self, folder):
        try:
            folder = self.change_separator(folder)
            self.ftp.rmd(folder)
            Logger.log_info("Folder removed : " + folder)
        except error_perm as e:
            Logger.log_warning("Folder removed : " + folder + " " + str(e))

    def file_transfer(self, path, srv_path, file_name):
        try:
            srv_path = self.change_separator(srv_path)
            file = open(os.path.join(path, file_name), 'rb')
            self.ftp.storbinary('STOR ' + srv_path, file)
            file.close()
            Logger.log_info("File created / updated : srv {0} file {1}".format(srv_path, file_name ))
        except Exception as e:
            Logger.log_warning("File created / updated : srv {0} file {1} -> error on {2}".format(srv_path, file_name, str(e)))

    def remove_file(self, file):
        try:
            file =  self.change_separator(file)
            self.ftp.delete(file)
            Logger.log_info(f"File removed : {file}")
        except Exception as e:
            Logger.log_warning(f"File removed : {file} -> error: {e}")

    def get_folder_content(self, path):
        path = self.change_separator(path)
        init_list = self.ftp.nlst(path)
        new_list = []
        for path in init_list:
            new_list.append(path.replace("/", os.path.sep))
        return new_list

    def if_exist(self, element, list):
        if element in list:
            return True
        else:
            return False

    def change_separator(self, where):
        return where.replace('\\','/')


