from dotenv import load_dotenv
import os

load_dotenv()

coffee_maker_service = 'https://coffee-maker.poc.com/api/employee/profile/1'
wrong_coffee_maker_service = 'https://coffee-maker.poc.com/api/employee/profile/'
token_has_expired_text = 'The Token has expired on 2022-09-23T12:02:19Z.'
client_email = 'boris.vajagic-in@gmail.com'


class Confiq:

    high_fiver_url = os.getenv('high_fiver_url')
    end_point_login = os.getenv('end_point_login')
    end_point_home = os.getenv('end_point_home')
    end_point_admin = os.getenv('end_point_admin')
    award_end_point = os.getenv('award_end_point')
    client_email = os.getenv('client_email')
    test_dummy_in_secret = os.getenv('test_dummy_in_secret_new')
    test_dummy_secret = os.getenv('test_dummy_regular_secret_new')
    test_databasecode = os.getenv('test_dummy_database_secret_new')
    mail_test_database = os.getenv('mail_test_database')
    experience_test_secret = os.getenv('test_dummy_experience_secret_new')
    mail_intern = os.getenv('mail_intern')
    password = os.getenv('password')
    mail_employee = os.getenv('mail_employee')
    experience_mail = os.getenv('experience_mail')
    private_mail = os.getenv('private_mail')