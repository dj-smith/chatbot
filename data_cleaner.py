import re

def clean(file_name, printed_rows = 6):
    file = open(file_name, encoding='utf-8', errors='ignore')
    raw_rows = file.read().split('\n')
    raw_rows.pop()
    raw_rows.reverse()
    rows = []

    assert(len(raw_rows) > 0)

    for line in raw_rows:
        cleaned = re.sub(r"\"+", "", line).split('\t')
        cleaned[0] = int(cleaned[0][1:])
        cleaned[1] = int(cleaned[1][1:])
        cleaned[2] = int(cleaned[2][1:])
        cleaned[3] = cleaned[3].lower()
        cleaned[4] = re.sub(r"(\w)([\?\!\;\.\,])", r"\1 \2", cleaned[4]).lower()
        rows.append(cleaned)

    create__cleaned_file(rows)

    return rows

def create_cleaned_file(cleaned_data, file_name = 'cleaned_lines.txt'):
    f = open(file_name, 'w', encoding='utf-8', errors='ignore')
    for line in cleaned_data:
        s = "{0}\t{1}\t{2}\t{3}\t{4}\n".format(line[0], line[1], line[2], line[3], line[4])
        f.write(s)

    print("File created.")
