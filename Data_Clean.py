import pandas as pd
import re
from datetime import datetime

# Functions

def clean_area(area):
    if isinstance(area, str) and re.findall(r'[\d,]+', area) and 'עסקאות באיזור' not in area:
        return int(re.findall(r'[\d,]+', area)[0])
    return None


def extract_room(room):
    try:
        room_num = re.findall(r'\d\.*\d*', room)
        if len(room_num) == 1:  # in case of only one digit (e.g. 6.5 rooms).
            return float(room_num[0])
        elif len(room_num) > 1:  # in case of range of digits (e.g. 3-5 rooms).
            numbers = [int(x) for x in room_num]
            mean_room = np.mean(numbers)
            return mean_room
    except:
        return None


# Change the city names that appear more than once.

def clean_city(city):
    return city.strip().replace('נהרייה', 'נהריה')

def boolean_encoding(row):
    truth_vals = ['True', 'TRUE', '1', 'כן', 'יש', 'yes']
    return 1 if str(row) in truth_vals or 'יש' in str(row) else 0


def extract_flexibility(ent_date):
    today = datetime.today().date()  # Today's date
    delta = (ent_date - today).days  # Delta in days
    delta = delta / 30.44  # Delta in months
    if delta < 6:
        return 'less_than_6_months'
    elif delta < 12:
        return '6-12_months'
    return 'above_year'


def fix_address(address):
    street = str(address[0])
    number = str(address[1])
    area = str(address[2])
    if 'בשכונת ' in street:
        area = re.sub(r'[^א-ת\s]|בשכונת', '', street).strip()  # Replace the special characters with ''
        try:
            number = re.search(r'\d+', number).group()  # Find the first sequence of digits
        except:
            number = None
        street = None
    else:
        street = re.sub(r'[^א-ת\s]|בשכונת', '', street).strip()  # Replace the special characters with ''
        try:
            number = re.search(r'\d+', number).group()  # Find the first sequence of digits
        except:
            try:
                number = re.search(r'\d+', address[0]).group()
            except:
                number = None
        area = re.sub(r'[^א-ת\s]|בשכונת', '', area).strip()  # Replace the special characters with ''
    if street == '':
        street = None
    if number == '':
        number = None
    if area == '':
        area = None
    return street, number, area


def clean_data(dataset):
    # Rename columns
    dataset.rename(columns={'hasElevator ': 'hasElevator', 'hasParking ': 'hasParking', 'hasBars ': 'hasBars',
                            'hasStorage ': 'hasStorage', 'condition ': 'condition',
                            'hasAirCondition ': 'hasAirCondition',
                            'hasBalcony ': 'hasBalcony', 'hasMamad ': 'hasMamad',
                            'handicapFriendly ': 'handicapFriendly',
                            'entranceDate ': 'entranceDate', 'furniture ': 'furniture',
                            'publishedDays ': 'publishedDays',
                            'description ': 'description'}, inplace=True)

    # Fix and Clean Values:
    dataset['Area'] = dataset['Area'].apply(clean_area)
    dataset.room_number = dataset.room_number.apply(extract_room)
    dataset.City = dataset.City.apply(clean_city)

    bool_cols = ['hasElevator', 'hasParking', 'hasBars', 'hasStorage',
                 'hasAirCondition', 'hasBalcony', 'hasMamad', 'handicapFriendly']
    dataset[bool_cols] = dataset[bool_cols].applymap(boolean_encoding)

    dataset.entranceDate = dataset.entranceDate.apply(extract_flexibility)

    address_cols = ['Street', 'number_in_street', 'city_area']
    dataset[address_cols] = dataset[address_cols].apply(lambda x: pd.Series(fix_address(x)), axis=1)

    # Fill Missing Values

    dataset.condition.fillna('לא צויין', inplace=True)
    dataset.condition = dataset.condition.replace({'None': 'לא צויין', 'FALSE': 'לא צויין'})

    dataset.num_of_images.fillna(0, inplace=True)

    dataset.description = dataset.description.replace({'None': 'אין', 'None ': 'אין'})
    dataset.description.fillna('אין', inplace=True)

    dataset.publishedDays = dataset.publishedDays.replace(
        {'Nan': 'None', '-': 'None', 'None ': 'None', 'חדש': 0, 'חדש!': 0})

    dataset.total_floors.fillna(dataset.floor, inplace=True)

    conditions = (dataset['floor'].isna()) & (dataset['type'].isin(["קוטג'", 'דו משפחתי']))
    dataset.loc[conditions, 'floor'] = 0
    dataset.loc[conditions, 'total_floors'] = 0

    mean_floor = round(dataset.floor.mean())
    dataset.floor.fillna(mean_floor, inplace=True)

    mean_tot_floor = round(dataset.total_floors.mean())
    dataset.total_floors.fillna(mean_tot_floor, inplace=True)

    # Feature Engineering
    mean_room_size = (dataset.Area / dataset.room_number).mean()
    # Now we can fill the Area for the entires who missing it.
    dataset.loc[dataset.Area.isna(), 'Area'] = mean_room_size * dataset.loc[dataset.Area.isna(), 'room_number']

    # Now we can fill the room number for the entires who missing it.
    dataset.loc[dataset.room_number.isna(), 'room_number'] = dataset.loc[
                                                                 dataset.room_number.isna(), 'Area'] / mean_room_size

    dataset['Shopping_Center'] = dataset.description.apply(
        lambda x: int(any(map(lambda value: value in x, ['מסחרי', 'בילוי']))))

    edu_list = ['חינוך', 'בית ספר', 'בתי ספר', ' גנים', 'מוסד', 'אוניברסיט']
    dataset['Education'] = dataset.description.apply(lambda x: int(any(map(lambda value: value in x, edu_list))))

    # Drop the unrelevant columns
    dataset.drop(columns=['city_area', 'Street', 'number_in_street', 'num_of_images', 'publishedDays'], inplace=True)

    return dataset