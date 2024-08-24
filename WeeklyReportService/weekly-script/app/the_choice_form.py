import user_data as ent
import regular_user_data as regular
import exception_queries as exception_query
import logging


def question_form():
    question = str(input("Are you interested in User or Regular billing groups?: ")).lower()
    env_name = str(input("Insert environment ({type1}, {type2}): ")).upper()
    start_date = str(input("Insert start date (yyyy-mm-dd): "))
    end_date = str(input("Insert end date (yyyy-mm-dd): "))
    if question == 'User':
        if env_name == 'type1':
            query_result = user.tasks_info_query(env_name, start_date, end_date)

            results_for_user = user.process_user_billing_groups(query_result, env_name)
            report = user.create_report(results_for_user, start_date, end_date, env_name)
            return report
        elif env_name == 'type2':
            query_result = exception_query.tasks_info_query(env_name, start_date, end_date)

            results_for_user = user.process_enterprise_billing_groups(query_result, env_name)
            report = user.create_report(results_for_user, start_date, end_date, env_name)
            return report
        else:
            logging.error(msg="Invalid Platform name. Please try again: ")
            question_form()
    elif question == 'Regular':
        if env_name == 'type1':
            query_result_for_regular = regular.tasks_info_query_regular_data(env_name, start_date, end_date)

            results_for_regular = regular.process_regular_data_billing_groups(query_result_for_regular)
            report = regular.create_report(results_for_regular, start_date, end_date, env_name)
            return report
        elif env_name == 'type2':
            query_result_for_regular = regular.tasks_info_query_regular_data(env_name, start_date, end_date)

            results_for_regular = regular.process_regular_data_billing_groups(query_result_for_regular)
            report = regular.create_report(results_for_regular, start_date, end_date, env_name)
            return report
        else:
            logging.error("Invalid env name. Please try again: ")
            question_form()
    else:
        logging.error(msg="Invalid input. Please try again: ")
        question_form()

