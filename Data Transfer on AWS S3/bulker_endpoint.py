import os
import csv
import logging
import time

api = Api(url='https://api/v2', token='<server_auth>')


from meta.resource import Resource
from meta.fields import (
    DateTimeField, StringField
)

logging.basicConfig(
    filename=os.getcwd() + '/deleter.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s',
)

logger = logging.getLogger(__name__)

def format_files_for_json():
    logger.info('Loading files...')
    with open('files_input.csv', 'r') as files:
        files_list = [f.strip() for f in files]
        nova_lista = [{"file": single_file} for single_file in files_list]
    return nova_lista

def create_report(deleted_files):
    subdir = "reports"
    if not os.path.exists(subdir):
        os.mkdir(subdir)

    file_path = os.path.join(subdir, 'Obrisani_fajlovi.csv')
    
    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['Deleted File IDs'])
        
        for file_id in deleted_files:
            writer.writerow([file_id])

    logger.info(f"Report created at {file_path}")

class AsyncJob(Resource):
    _URL = {
        'bulk_delete_files': '/async/files/delete'
    }

    id = StringField(read_only=True)
    state = StringField(read_only=True)
    started_on = DateTimeField(read_only=True)
    finished_on = DateTimeField(read_only=True)

    def __str__(self):
        return (f'<AsyncJob: id={self.id}, state={self.state}, '
                f'started_on={self.started_on}, finished_on={self.finished_on}>')

    @classmethod
    def file_bulk_delete(cls, files, api):
        print('Submitting async job for deleting files in bulk')

        data = {'items': files}
        try:
            response = api.post(url=cls._URL['bulk_delete_files'], data=data).json()
            deleted_files = [item['file'] for item in data['items']]
            logger.info(f"Deleted files: {deleted_files}")

            job = AsyncJob(api=api, **response)
            logger.info(f"Job '{job.id}' is in progress...")
            create_report(deleted_files)

            logger.info(f"Job '{job.id}' completed on: {job.finished_on}")
            return deleted_files

        except Exception as e:
            logger.warning(f"An error occurred: {str(e)}")
            logger.error(f"Problem occurred while deleting files: {[file['file'] for file in files]}")
            raise e

    @classmethod
    def delete_files_in_batches(cls, files, batch_size=100, wait_time=5):
        """
        Metoda koja pokreće brisanje fajlova u batch-ovima.
        :param files: Lista fajlova za brisanje
        :param batch_size: Broj fajlova po batch-u
        :param wait_time: Pauza između batch-ova
        """
        while files:
            batch = files[:batch_size]
            logger.info(f'Processing batch of {len(batch)} files for deletion.')
            
            cls.file_bulk_delete(batch, api)
            
            del files[:batch_size]
            
            logger.info(f'Waiting {wait_time} seconds before processing the next batch.')
            time.sleep(wait_time)
        
        logger.info("All specified files have been processed for deletion.")

if __name__ == '__main__':
    files_to_delete = format_files_for_json()
    
    AsyncJob.delete_files_in_batches(files=files_to_delete)
