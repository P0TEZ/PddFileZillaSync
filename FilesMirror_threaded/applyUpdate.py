import logging
import threading
import time

from talk_to_ftp import TalkToFTP

class ApplyUpdate:
    def __init__(self, ftp_website, thread_number, fileToSent):
        # Set the number of thread
        print("Number of thread: " + str(thread_number))
        self.MAX_TRHEAD = thread_number

        # Set the FTP website
        self.ftp_website = ftp_website

        # The Queue of file to send
        self.fileToSent = fileToSent
        
        # List of thread
        self.threadList = []

        # Start all thread
        self.startAllThread()


    def startAllThread(self):
        """
        Creates a list of threads, and then starts them all
        """
        try:

            for _ in range(self.MAX_TRHEAD):

                # Create a thread and add it to the list
                thread = threading.Thread(target=self.send_file)
                self.threadList.append(thread)

                # Start the thread
                thread.start()
        except Exception as e:
            logging.error("Error while starting thread: " + str(e))


    def send_file(self):
        """
        Runs in a thread and waits for files to be added to a queue. When a file is
        added to the queue, it connects to an FTP server, uploads the file, and then disconnects
        """
        while True:

            # If there is a file to send
            if self.fileToSent.empty() == False:
                try:
                    file = self.fileToSent.get()

                    # Connect to the FTP server
                    tmpFtp = TalkToFTP(self.ftp_website)
                    tmpFtp.connect()


                    # If the file is an update, we need to remove the old file
                    if(file['action'] == "update"):
                        tmpFtp.remove_file(file['srv_full_path'])

                    # Send the file
                    tmpFtp.file_transfer(file['path_file'], file['srv_full_path'], file['file_name'])

                    # Disconnect from the FTP server
                    tmpFtp.disconnect()

                except Exception as e:
                    logging.error("Error while sending file: " + str(e))

            else:
                # if there is no file to send wait for 1 second 
                time.sleep(1)