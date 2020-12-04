def check_field(field):
    name, value = field
    try:
        return field_funcs[name](value)
    except:
        return False

def check_byr(value):
    return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002

def check_iyr(value):
    return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020

def check_eyr(value):
    return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030

def check_hgt(value):
    height = int(value[:-2])
    units = value[-2:]
    return (150 <= height <= 193) if units == "cm" else (59 <= height <= 76) if units == "in" else False

def check_hcl(value):
    red = 0 <= int(value[1:2],16) <= 255
    green = 0 <= int(value[3:4],16) <= 255
    blue = 0 <= int(value[5:],16) <= 255
    return value[0]=="#" and red and green and blue

def check_ecl(value):
    return value in ["amb", "blu", "brn","gry","grn","hzl","oth"]

def check_pid(value):
    return len(value)==9 and (0 <= int(value) <= 999999999)

def valid(passport):
    valid = field_funcs.keys()
    fields = [(name, value) for name, value in [field.split(":") for field in passport.split()] if name in valid]
    return sum(map(check_field,fields)) >= len(valid)

def total_valid(passports):
    return sum(map(valid, passports.split("\n\n")))

field_funcs = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid
}

if __name__ == '__main__':
    data = open("input.txt","r").read()
    print(total_valid(data))