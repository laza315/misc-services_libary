import os


def current_path():
    current_working_dir = os.getcwd()
    print(f'Current working directory: {current_working_dir}')
    os.chdir('/Users/sbg/PycharmProjects/praksa2022_zadaci')
    print("Set me at", os.getcwd())
    files_and_dir = '/Users/sbg/PycharmProjects/praksa2022_zadaci/'
    print('Available directories and files: ', os.listdir(files_and_dir))

def listing_dir_n_files():

 a = input('Insert one of these values:\n(-f) for files\n(-d)for directories')
 if a == '-f':

    files = '/Users/sbg/PycharmProjects/praksa2022_zadaci/'

    list_of_files = filter(lambda x: os.path.isfile(os.path.join(files, x)),
                    os.listdir(files))

    list_of_files = sorted(list_of_files, key=lambda x: os.stat
                    (os.path.join(files, x)).st_size)
    print('This is the list of files sorted by size:')
    for file_name in list_of_files:
                    file_path = os.path.join(files, file_name)
                    file_size = os.stat(file_path).st_size
                    print(f' {file_size} -->: {file_name}')

 elif a == '-d':
    # def dir_listing():
         dir = '/Users/sbg/PycharmProjects/praksa2022_zadaci/'

         list_of_files = filter(lambda x: os.path.isdir(os.path.join(dir, x)),
            os.listdir(dir))

         list_of_files = sorted(list_of_files, key=lambda x: os.stat
            (os.path.join(dir, x)).st_size)

         print('This is the list of directories sorted by size:')
         for file_name in list_of_files:
            file_path = os.path.join(dir, file_name)
            file_size = os.stat(file_path).st_size
            print(f' {file_size} -->: {file_name}')

 else:

        print("Sorry!Wrong Value\n Try again!")
        return listing_dir_n_files()

if __name__ == '__main__':
    current_path()
    listing_dir_n_files()
