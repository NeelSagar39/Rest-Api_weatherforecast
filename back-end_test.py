# include unit test and interfaces test, after finish test there will be a log file can be tracked

import datetime
import requests

ROOT_URL = 'http://3.82.248.105/'
ISOTIMEFORMAT = 'GMT %Y-%m-%d %H:%M:%S'


def log_file_and_timestamp(test_type: str):
    try:
        present_time = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        log_path = test_type + '_test_log.txt'
        record = open(log_path, 'a')
        record.write('TEST TIME:' + present_time + '\n')
    except IOError:
        print('log file operation failed!')
    else:
        return record, log_path


class InterfacesTester:
    interfaces_test_urls = {
        'temp_predictions': 'get-temp-predictions',
        'rainfall_predictions': 'get-rainfall-predictions',
        'humidity_predictions': 'get-humidity-predictions',
        'wind_predictions': 'get-wind-predictions',
        'cloudy_predictions': 'get-cloudy-predictions',
        'weekly_temperature': 'get-temp-weekly',
        'weekly_rainfall': 'get-rain-weekly',
        'weekly_humidity': 'get-humidity-weekly',
        'weekly_cloud': 'get-cloud-weekly',
        'weekly_wind': 'get-wind-weekly',
    }

    @staticmethod
    def test():
        record, log_path = log_file_and_timestamp(test_type='interface')
        for interface_name, url in InterfacesTester.interfaces_test_urls.items():
            res = requests.get(ROOT_URL + url)
            result = 'PASS' if res.status_code is 200 else 'FAILED'
            if result is 'FAILED':
                result += ', ERROR CODE:' + str(res.status_code)
            record.write('interface name:' + interface_name + '    test_result:' + result + '\n')
        record.write('\n\n')
        record.close()
        print('all interfaces tests have been finished, please check test log file in ' + log_path)


class UnitTester():
    unit_test_failed_types = {
        'FUNCTION_MISSING': 'function can not be found in this module!',
        'FUNCTION_RETURN_NONE': 'function return None value!',
        'FUNCTION_ERROR': 'function internal error!'
    }
    modules_list = ['data', 'model']
    functions_list = {
        'data': [
            'request_hourly',
            'request_weekly'
        ],
        'model': [
            'pre_process',
            'train_temp_model',
            'train_rainfall_model',
            'train_humidity_model',
            'train_wind_speed_model',
            'train_cloudy_model',
            'train_temp_model_weekly',
            'train_humidty_model_weekly',
            'train_cloud_model_weekly',
            'train_rain_model_weekly',
            'train_wind_model_weekly',
        ]
    }

    @staticmethod
    def test():
        record, log_path = log_file_and_timestamp(test_type='unit')
        historical_data_hourly = None
        historical_data_weekly = None
        # reflection feature
        for module in UnitTester.modules_list:
            module_ref = __import__(module)
            record.write('test module: ' + module + '\n')
            for func_name in UnitTester.functions_list[module]:
                func_ref = getattr(module_ref, func_name, None)

                # if the function exists
                if func_ref is None:
                    record.write(
                        'function: ' + func_name + '    test_result: FAILED!' + UnitTester.unit_test_failed_types[
                            'FUNCTION_MISSING'])
                else:
                    # all functions from 'model' needs parameters
                    if module is 'model':
                        param = historical_data_weekly if 'weekly' in func_name else historical_data_hourly
                        try:
                            func_response = func_ref(param)
                        except BaseException:
                            record.write(
                                'function: ' + func_name + '    test_result: FAILED!' +
                                UnitTester.unit_test_failed_types[
                                    'FUNCTION_ERROR'])
                        else:
                            if func_response is None:
                                record.write(
                                    'function: ' + func_name + '    test_result: FAILED!' +
                                    UnitTester.unit_test_failed_types[
                                        'FUNCTION_RETURN_NONE'])
                            else:
                                record.write('function: ' + func_name + '    test_result: PASS!')
                    else:
                        # all functions in 'data' does not need params
                        try:
                            func_response = func_ref()
                        except BaseException:
                            record.write(
                                'function: ' + func_name + '    test_result: FAILED!' +
                                UnitTester.unit_test_failed_types[
                                    'FUNCTION_ERROR'])
                        else:
                            if func_response is None:
                                record.write(
                                    'function: ' + func_name + '    test_result: FAILED!' +
                                    UnitTester.unit_test_failed_types[
                                        'FUNCTION_RETURN_NONE'])
                            else:
                                record.write('function: ' + func_name + '   test_result: PASS!')
                                # maybe there will be error in the future since some functions have not been implemented
                                historical_data_hourly = func_ref() if 'hourly' in func_name else None
                                historical_data_weekly = func_ref() if 'weekly' in func_name else None
                record.write('\n')
            record.write('\n')
        record.write('\n\n')
        record.close()
        print('all unit tests have been finished, please check test log file in ' + log_path)


InterfacesTester.test()
UnitTester.test()
# from model import pre_process
# from data import request_hourly
# print(pre_process(request_hourly()))
