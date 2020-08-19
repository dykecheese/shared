import sys
import csv

def main():

    #check command line arguments
    if len(sys.argv) != 3:
        print("insufficient command line arguments")
        exit()

    #load database
    with open(sys.argv[1], newline='') as database:
        fieldnames = next(csv.reader(database))
        STR_names = fieldnames[1:]
        data = csv.DictReader(database, fieldnames=fieldnames)
        listed_data = []
        for line in data:
            listed_data.append(line)

    #define location for STR counts
    STR_totals = dict.fromkeys(fieldnames, 0)

    #load DNA sequence
    with open(sys.argv[2], "r") as sequence:

        DNA = sequence.read()
        len_STR_names = len(STR_names)

        #analyse DNA sequence for STR's
        for i in range(len_STR_names):
            for j in range(len(DNA)):
                count = STR_compare(DNA, j, STR_names[i])
                if count > STR_totals[f'{STR_names[i]}']:
                    STR_totals[f'{STR_names[i]}'] = count

    #check for DNA match
    ln = 0
    for line in listed_data:
        for z in range(len_STR_names):
            if int(line[f'{STR_names[z]}']) == STR_totals[f'{STR_names[z]}']:
                if z == len_STR_names-1:
                    print(f"Match {line['name']}")
            else:
                break
        ln += 0

def STR_compare(DNA, position, STR):
    STR_len = len(STR)
    temp = 0
    for byte in DNA:
        if DNA[position:position+STR_len] != STR:
            return temp
        else:
            temp += 1
            position += STR_len

main()