import locale
import datetime
import os

# Connect ru localization
locale.setlocale(locale.LC_ALL, "ru")

# Get path (current directory)
point = os.path.dirname(os.path.abspath(__file__)) + '\\'
print('\nIn folder', point, 'create:')

# Create folder with name 'month' and 'week' in 'month' folders
def create_f(month, week):
    try:
        os.makedirs(point + month + '\\' + week)
        print(f'\"{month}\" > \"{week}\"\nmsg: Folder created\n' + '-'*32)
    except OSError:
        print(f"\"{month}\" > \"{week}\"\nmsg: Can't create folder is already exists\n" + '-'*50)


def main():
    week = 0
    for j in range(1, 5):
        week = 'Неделя ' + str(j)
        for i in range(5, 10):
            
            # get month format in date i=(5-10 month)
            month = datetime.date(2019, i, 1).strftime('%m. %B')
            # create folder
            create_f(month, str(week))


if __name__ == "__main__":
    main()