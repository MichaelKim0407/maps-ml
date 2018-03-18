import location

__author__ = 'Michael'


def get_city_set(data):
    return sorted({d.city for d in data})


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    parser.add_argument('--binary')
    parser.add_argument('data', nargs='+')
    args = parser.parse_args()

    cities = get_city_set(location.read_files(*args.data))

    with open(args.output, 'w') as f:
        if not args.binary:
            i = 0
            for city in cities:
                f.write(f"{i},{city}\n")
                i += 1
        else:
            for city in cities:
                if city == args.binary:
                    f.write(f"1,{city}\n")
                else:
                    f.write(f"0,{city}\n")
