from subprocess import call


def main():
    print("WELCOME")
    print("TO")
    print("TUNGON BANK NG")

    input("Press Enter to continue...")
    call(["python", "banking.py"])


if __name__ == "__main__":
    main()
