import argparse

def main(name, destination):
    print('hello', name, 'bye', destination)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a Web App!')
    parser.add_argument('name', help='Name of the to-be-created app')
    parser.add_argument('destination', default='.', help='Destination to create app')
    params = parser.parse_args()
    main(params.name, params.destination)