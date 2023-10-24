import sys


def os_you_use():
    return sys.platform


if __name__ == "__main__":
    platform = os_you_use()
    print("Operating System Platform:", platform)
