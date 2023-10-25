# Using command-line arguments involves the sys module. Review the docs for this
# module and using the information in there write a short program that when run
# from the command-line reports what operating system platform is being used.

import sys


def os_you_use():
    return sys.platform


if __name__ == "__main__":
    platform = os_you_use()
    print("Operating System Platform:", platform)

# python os_you_are_use.py


# or another solution
# def os_you_use():
#     return sys.platform
# 
#
# platform = os_you_use()
# print("Operating System Platform:", platform)
