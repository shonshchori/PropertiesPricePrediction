from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired
import pickle
import os
import Data_Clean

prop_model = pickle.load(open('properties_model.pkl', 'rb'))
preprocessor = pickle.load(open('fitted_preprocessor.pkl', 'rb'))

app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = "MySecretKey"


class PredictForm(FlaskForm):
    city = SelectField("City", choices=[('פתח תקווה', 'פתח תקווה'), ('נתניה', 'נתניה'), ('באר שבע', 'באר שבע'),
                                        ('הרצליה', 'הרצליה'), ('דימונה', 'דימונה'), ('רחובות', 'רחובות'),
                                        ('גבעת שמואל', 'גבעת שמואל'), ('ירושלים', 'ירושלים'), ('שוהם', 'שוהם'),
                                        ('כפר סבא', 'כפר סבא'), ('רעננה', 'רעננה'), ('נהריה', 'נהריה'),
                                        ('זכרון יעקב', 'זכרון יעקב'), ('קרית ביאליק', 'קרית ביאליק'), ('חיפה', 'חיפה'),
                                        ('הוד השרון', 'הוד השרון'), ('תל אביב', 'תל אביב'),('ראשון לציון', 'ראשון לציון'),
                                        ('יהוד מונוסון', 'יהוד מונוסון'), ('נס ציונה', 'נס ציונה'), ('אילת', 'אילת'),
                                        ('חולון', 'חולון'), ('צפת', 'צפת'), ('בת ים', 'בת ים'), ('רמת גן', 'רמת גן'),
                                        ('נוף הגליל', 'נוף הגליל'), ('בית שאן', 'בית שאן')] , validate_choice=True)
    prop_type = SelectField("Type", choices = [('דירה', 'דירה'), ('דירת גן', 'דירת גן'), ('דירת גג', 'דירת גג'),
                                          ("קוטג'", "קוטג'"), ('בית פרטי', 'בית פרטי'), ('דופלקס', 'דופלקס'),
                                          ('דירת נופש', 'דירת נופש'), ("קוטג' טורי", "קוטג' טורי"), ('פנטהאוז', 'פנטהאוז'),
                                          ('מיני פנטהאוז', 'מיני פנטהאוז'), ('בניין', 'בניין'),
                                          ('דו משפחתי', 'דו משפחתי'), ('אחר', 'אחר')], validate_choice = True)
    room_number = StringField("Room Number", validators=[DataRequired()])
    area = StringField("Area", validators=[DataRequired()])
    street = StringField("Street", validators=[DataRequired()])
    number_in_street = StringField("Street Number", validators=[DataRequired()])
    city_area = StringField("Neighborhood", validators=[DataRequired()])
    num_of_images = IntegerField("Images No.", validators=[DataRequired()])
    hasElevator = BooleanField("Elevator")
    hasParking = BooleanField("Parking")
    hasBars = BooleanField("Bars")
    hasStorage = BooleanField("Storage")
    hasAirCondition = BooleanField("AirCondition")
    hasBalcony = BooleanField("Balcony")
    hasMamad = BooleanField("Mamad")
    handicapFriendly = BooleanField("Handicap Friendly")
    condition = SelectField("Condition", choices=[('שמור', 'שמור'), ('חדש', 'חדש'), ('משופץ', 'משופץ'),
                                              ('לא צויין', 'לא צויין'), ('ישן', 'ישן'),
                                              ('דורש שיפוץ', 'דורש שיפוץ')] , validate_choice=True)
    entranceDate = DateField("Entrance Date", validators=[DataRequired()])
    furniture = SelectField("Furniture", choices=[('לא צויין', 'לא צויין'), ('חלקי', 'חלקי'),
                                          ('אין', 'אין'), ('מלא', 'מלא')] , validate_choice=True)
    publishedDays = IntegerField("Published Days", validators=[DataRequired()])
    floor = IntegerField("Property Floor", validators=[DataRequired()])
    total_floors = IntegerField("Out of Floors", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    # email = EmailField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['GET', 'POST'])
def prop_prediction():
    city = None
    prop_type = None
    room_number = None
    area = None
    street = None
    number_in_street = None
    city_area = None
    num_of_images = None
    hasElevator = None
    hasParking = None
    hasBars = None
    hasStorage = None
    hasAirCondition = None
    hasBalcony = None
    hasMamad = None
    handicapFriendly = None
    condition = None
    entranceDate = None
    furniture = None
    publishedDays = None
    floor = None
    total_floors = None
    description = None
    prediction = None
    hasShopping = None
    hasEducation = None
    form = PredictForm()
    # Validate Form
    if form.validate_on_submit():
        city = form.city.data
        prop_type = form.prop_type.data
        room_number = form.room_number.data
        area = form.area.data
        street = form.street.data
        number_in_street = form.number_in_street.data
        city_area = form.city_area.data
        num_of_images = form.num_of_images.data
        hasElevator = form.hasElevator.data
        hasParking = form.hasParking.data
        hasBars = form.hasBars.data
        hasStorage = form.hasStorage.data
        hasAirCondition = form.hasAirCondition.data
        hasBalcony = form.hasBalcony.data
        hasMamad = form.hasMamad.data
        handicapFriendly = form.handicapFriendly.data
        condition = form.condition.data
        entranceDate = form.entranceDate.data
        furniture = form.furniture.data
        publishedDays = form.publishedDays.data
        floor = form.floor.data
        total_floors = form.total_floors.data
        description = form.description.data

        import pandas as pd
        prop = pd.DataFrame([[city, prop_type, room_number, area, street, number_in_street, city_area,
                              num_of_images, hasElevator, hasParking, hasBars, hasStorage, hasAirCondition, hasBalcony,
                              hasMamad, handicapFriendly, condition, entranceDate, furniture, publishedDays, floor,
                              total_floors, description]],
                            columns=['City', 'type', 'room_number', 'Area', 'Street', 'number_in_street',
                                     'city_area', 'num_of_images', 'hasElevator', 'hasParking', 'hasBars', 'hasStorage',
                                     'hasAirCondition', 'hasBalcony', 'hasMamad', 'handicapFriendly', 'condition',
                                     'entranceDate', 'furniture', 'publishedDays', 'floor',
                                     'total_floors', 'description'])

        prop = Data_Clean.clean_data(prop)
        hasShopping = prop.Shopping_Center.values[0]
        hasEducation = prop.Education.values[0]
        processed_prop = preprocessor.transform(prop)
        prop = prop.drop(columns=['description', 'City', 'type', 'condition', 'entranceDate', 'furniture',
                                  'room_number', 'Area', 'floor', 'total_floors'])
        processed_prop = pd.DataFrame(processed_prop, columns=preprocessor.get_feature_names_out())
        prop = pd.concat([prop, processed_prop], axis=1)
        prediction = prop_model.predict(prop)[0]
        prediction = "₪{:,.3f}".format(float(prediction))


    return render_template("Prediction.html",
                           city=city, prop_type=prop_type, room_number=room_number, area=area, street=street,
                           number_in_street=number_in_street, city_area=city_area, num_of_images=num_of_images,
                           hasElevator=hasElevator, hasParking=hasParking, hasBars=hasBars, hasStorage=hasStorage,
                           hasAirCondition=hasAirCondition, hasBalcony=hasBalcony, hasMamad=hasMamad,
                           handicapFriendly=handicapFriendly, condition=condition, entranceDate=entranceDate,
                           furniture=furniture, publishDays=publishedDays, floor=floor, total_floors=total_floors,
                           description=description, prediction=prediction, hasShopping=hasShopping,
                           hasEducation=hasEducation, form=form)


@app.route('/team')
def about_us():
    return render_template('team.html')


@app.route('/about')
def about_the_project():
    return render_template('about.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
