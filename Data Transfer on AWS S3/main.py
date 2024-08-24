import configparser
config = configparser.ConfigParser()
import logging
import boto3

# import any api.client server
api = config.Api(url='https://api/v2', header_token='*********************', advance_access=True)


def get_s3_client(config_file='aws_config.config'):
    config = configparser.ConfigParser()

    config.read(config_file)

    aws_access_key_id = config.get('DEFAULT', 'aws_access_key_id')
    aws_secret_access_key = config.get('DEFAULT', 'aws_secret_access_key')
    aws_region = config.get('DEFAULT', 'aws_region')
    s3_bucket_name = config.get('DEFAULT', 's3_bucket_name')

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    try:
        s3_client.head_bucket(Bucket=s3_bucket_name)
        print(f"Connected to bucket: {s3_bucket_name}")
    except Exception as e:
        print(f"Error connecting to bucket: {e}")

    return s3_client


def get_all_files_from_folder(folder, prefix):
   folder_files = []

   for item in folder.list_files():
        if item.is_folder():
           folder_files = folder_files + get_all_files_from_folder(item, prefix + '/' + item.name)
        else:
            try:
               folder_files.append(item)
               file_name = prefix + '/' + item.name
               results.append(file_name)
               exports = []
               export = api.exports.submit_export(file=item, storage_vault='name/storage_entity', location=file_name, overwrite=False)
               exports.append(export)
            except Exception as ex_status:
                if ex_status == "errors.Forbidden: Check the documentation.":
                    logging.error(msg='Requested file cannot be exported')
                    continue
   return folder_files


results = []
def export(project):
    files_to_export = []
    files_all = api.files.query(project=project).all()
    files_all = [file for file in files_all]
    for file in files_all:
        if not file.is_folder():
            try:
                file_name = project + '/' + file.name
                files_to_export.append(file_name)
                exports = []
                export = api.exports.submit_export(file=file, storage_vault='name/storage_entity', location=file_name, overwrite=False)
                exports.append(export)
            except Exception as ex_status:
                if ex_status == "errors.Forbidden: Check the documentation.":
                    logging.error(msg='Requested file cannot be exported')
                    continue
        else:
            get_all_files_from_folder(file, project + '/' + file.name)

    return files_to_export + results

if __name__ == "__main__":
    s3_client = get_s3_client()
    final = export('name/storage_entity')
