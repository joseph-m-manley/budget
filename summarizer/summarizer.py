#!/usr/bin/env python3


def invert_dict(d):
    return {value: key for key in d for value in d[key]}


def summarize(categories, activity):
    inverted = invert_dict(categories)


def main():
    config = get_config()
    categories = get_categories(config['categories'])
    activity = get_jsn(config['csvfilepath'])

    summarize(categories, activity)


if __name__ == '__main__':
    main()