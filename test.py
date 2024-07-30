import math
from textwrap import dedent
from timeit import default_timer as timer
import tracemalloc

class bcolors:
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    # BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def _str_truncate(data, size=200):
    data_str = str(data)

    if len(data_str) > size + 3:
        return data_str[:size] + '...'
    
    return data_str

def display_test_case(test_case):
    print(dedent("""
    Input:
    {}

    Expected Output:
    {}
    """.format(_str_truncate(test_case['input']), _str_truncate(test_case['output']))))

def display_result(result):
    actual_output, passed, runtime, traced_memory = result
    message = bcolors.OKGREEN + 'PASSED' + bcolors.ENDC if passed else bcolors.FAIL + 'FAILED' + bcolors.ENDC
    memory_usage = 'Current %.2fKB, Peak %.2fKB' % tuple(x / (1024) for x in traced_memory)

    print(dedent("""
    Actual Output:
    {}

    Execution Time:
    {} ms
                 
    Memory Use:
    {}

    Test Result:
    {}
    """.format( _str_truncate(actual_output), runtime, memory_usage, message)))


def evaluate_test_cases(func_to_test, tests):
    """
    The `evaluate_test_cases` function takes a function and a list of test cases as input, runs the
    function with each test case, compares the output with the expected result, and prints the results
    of the tests.
    
    :param func_to_test: A function that you want to test with the provided test cases
    :param tests: The `tests` parameter should be a list of dictionaries where each dictionary
    represents a test case. Each dictionary should have an 'input' key with a value that is another
    dictionary containing the input arguments for the function `func_to_test`, and an 'output' key with
    the expected output for that test

    Example of a test in tests list:
    ```
    {
        'input': {
            'piles': [30,11,23,4,20],
            'h': 6
        }, 'output': 23
    }
    ```
    """
    failed_count = 0
    passed_count = 0
    for idx, test in enumerate(tests):
        print(bcolors.UNDERLINE + f'Test Case {idx+1}' + bcolors.ENDC)
        display_test_case(test)
        tracemalloc.start()
        start = timer()
        actual_output = func_to_test(**test['input'])
        end = timer()
        traced_memory = tracemalloc.get_traced_memory()
        tracemalloc.clear_traces()
        runtime = math.ceil((end - start)*1e6)/1000
        if actual_output==test['output']:
            passed_count += 1
        else:
            failed_count += 1
        result = actual_output, actual_output==test['output'], runtime, traced_memory
        display_result(result)


    print(bcolors.UNDERLINE + 'Summary' + bcolors.ENDC)
    print('Total Tests:',(failed_count+passed_count))
    print(bcolors.OKGREEN + f'PASSED: {passed_count}' + bcolors.ENDC)
    print(bcolors.FAIL + f'FAILED: {failed_count}' + bcolors.ENDC)
