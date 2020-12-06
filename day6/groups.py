def count_questions(group):
    answers = set()
    for line in group.split():
        for answer in line:
            answers.add(answer)
    return len(answers)

def count_common(group):
    participants = group.split()
    answers = {}
    for line in participants:
        for answer in line:
            answers[answer] = answers.get(answer, 0) + 1
    return sum([1 for count in answers.values() if count == len(participants)])

def total_yes(codes):
    return sum(map(count_questions, codes.split("\n\n")))

def common_yes(codes):
    return sum(map(count_common, codes.split("\n\n")))

if __name__ == '__main__':
    data = open("input.txt","r").read()
    print("Part 1:", total_yes(data))
    print("Part 2:", common_yes(data))