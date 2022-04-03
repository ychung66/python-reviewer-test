

def main():
    ask_again = True
    operations_count = 0
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
        result, operations_count = perform_division(a,b, operations_count = 0)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            print("You performed " + str(operations_count) + " operations, bye!")


def perform_division(a,b, operations_count):
    global operations_count
    try:
        operations_count += 1
        return (int(a)/int(b), operations_count)
    except ZeroDivisionError as e:
        logging.exception('ZeroDivisionError: %s', e)



main()