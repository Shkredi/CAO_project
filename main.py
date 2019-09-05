import data_parse
from observ_object import ObservObject


def read_data():
    """Input of all necessary data"""
    print()
    print('Enter your location data.')
    lon = float(input('Please, enter your longitude in degrees (north with "+", south with "-": '))
    lat =  float(input('Please, enter your latitude in degrees (east with "+", west with "-": '))
    timezone = int(input('Please, enter your timezone including summer/winter time: '))
    location = [lat, lon]

    print()
    print('Enter date fot observing.')
    year = int(input('Please, enter year: '))
    month = int(input('Please, enter number of month: '))
    day = int(input('Please, enter day: '))
    date = [year, month, day]

    print()
    print()

    return date, location, timezone


def write_results(date, location, timezone):
    """Print all information"""
    print()
    print(('NAME' + 40*' ')[:40] + ('R.A.'+5*' ')[:10] + '\t' + ('DECL.'+13*' ')[:13] + \
               '\t' + 'MAG  ' + '\t' + ('CONSTELLATION'+15*' ')[:15] + '\t' + 'RISE' + '\t' + 'SET')
    print('-'*105)

    objects = [ObservObject(*data) for data in data_parse.get_all()]
    for obj in objects:
        obj.calc_time(date, location, timezone)
        print(obj)
    print()


def main_loop():
    """Main loop of program"""
    date, location, timezone = read_data()
    write_results(date, location, timezone)
    input("\nIf you want to try again - press Enter\n")

main_loop()