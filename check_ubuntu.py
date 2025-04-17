from typing import List  # Для Python < 3.9
import random

def generate_phone_number() -> str:
    return f"+7{''.join(str(random.randint(0, 9)) for _ in range(9))}"

def write_phones_to_files(numbers: list[str], filenames: list[str]) -> None:
    for filename in filenames:
        with open(filename, 'w') as f:
            f.write('\n'.join(numbers))

if __name__ == "__main__":
    phone_numbers: list[str] = [generate_phone_number() for _ in range(10)]
    output_files: list[str] = ["phones.txt", "phones_1.txt"]
    write_phones_to_files(phone_numbers, output_files)