
class bcolors:
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

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
    failed = 0
    passed = 0
    for idx, test in enumerate(tests):
        print(f'Test Case {idx+1}')
        result = func_to_test(**test['input'])
        print('input:', test['input'])
        print('expected output:', test['output'])
        print('actual output:', result)
        if result==test['output']:
            passed += 1
            print(bcolors.OKGREEN + 'PASSED' + bcolors.ENDC)
        else:
            failed += 1
            print(bcolors.FAIL + 'FAILED' + bcolors.ENDC)
        print()

    print('Total Tests:',(failed+passed))
    print(bcolors.OKGREEN + f'PASSED: {passed}' + bcolors.ENDC)
    print(bcolors.FAIL + f'FAILED: {failed}' + bcolors.ENDC)
