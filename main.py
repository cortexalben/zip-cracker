import timeit
import pyzipper as pyzip
import itertools
import string


def main():
    global zip_file
    zip_file = input(f"{'*' * 40}\n{' ' * 9}Z I P   C R A C K E R\nCrack password of an encrypted zip file.\n\n"
                     f"Name of (or path to) the file: ")
    min_limit = int(input("Minimum length of the password: "))
    crack_pwd(source_file=zip_file, min_length=min_limit, characters=string.ascii_lowercase)


def crack_pwd(source_file, min_length=1, characters=string.printable):
    """
    :param source_file: Add path to zip file
    :param min_length: Minimum length of the password
    :param characters: Default set to string.printable. Works best with one or a few of the following: string.digits, string.ascii_letters (string.ascii_lowercase, string.ascii_uppercase), string.punctuation, string.whitespace
    """
    count = 1
    start_time = timeit.default_timer()
    timeit.Timer()
    with pyzip.AESZipFile(zip_file, 'r') as placeholder_zipfile:
        while True:
            for pwd in itertools.product(characters, repeat=min_length):
                try:
                    placeholder_zipfile.extractall(pwd=bytes(''.join(pwd), encoding='utf-8'))
                    return print(f"{'*' * 50}\n[{count}] [SUCCESS] Password found: {''.join(pwd)}\n"
                                 f"It took {round((timeit.default_timer() - start_time), 5)} seconds to crack the password.\n{'*' * 50}")
                except (RuntimeError, pyzip.error, pyzip.BadZipFile):
                    print(f"[{count}] [FAILURE] Password failed: {''.join(pwd)}")
                    count += 1
            min_length += 1


if __name__ == '__main__':
    main()