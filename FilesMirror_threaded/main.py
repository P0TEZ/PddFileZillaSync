import sys
from directory_manager import DirectoryManager
from get_parameters import get_user_parameters

if len(sys.argv) == 1:
    sys.argv.extend(("localhost,test,1234,,21", "/Users/yves/Desktop/SyncFTP", "2", "30", "8"))

if __name__ == "__main__":
    # get parameters from command line
    ftp_website, local_directory, max_depth, refresh_frequency, thread_number, excluded_extensions = get_user_parameters()

    # init directory manager with local directory and maximal depth
    directory_manager = DirectoryManager(ftp_website, local_directory, max_depth, thread_number, excluded_extensions)

    # launch the synchronization
    directory_manager.synchronize_directory(refresh_frequency)
