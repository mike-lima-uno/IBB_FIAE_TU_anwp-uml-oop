concatenate_name = lambda first_name, last_name: \
    f"{"*" * (len(first_name + last_name)+1)}\n{first_name} {last_name}\n{"*" * (len(first_name + last_name)+1)}"

if __name__ == "__main__":
    names = [("John", "Doe"), ("Jane", "Smith"), ("Alice", "Johnson")]

    for first_name, last_name in names:
        print(concatenate_name(first_name, last_name), end="\n\n")