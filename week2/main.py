from Person import Person

if __name__ == "__main__":
    some_list = ['bob', 'jane', 'cat', 'dog', 'scooby doo']
    
    try:
        for some_name in range(6):
            print(Person(some_list[some_name]))
    except Exception as e:
        print(f'Some exception occurred: { e.with_traceback() }')