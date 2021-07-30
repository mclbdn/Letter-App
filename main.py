with open("Input/names.txt") as file:
    name_list = file.readlines()
    names = []
    for name in name_list:
        new_name = name.strip()
        names.append(new_name)

for name in names:
    with open(f"Output/letter_for_{name}.txt", mode="w") as file:
        with open("Input/letter.txt") as letter_file:
            contents = letter_file.read()
            new_content = contents.replace("[name]", name)

        file.write(new_content)
