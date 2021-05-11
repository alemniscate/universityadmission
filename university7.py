def write_applicants(department, applicants_list):
    file = open(department.lower() + ".txt", "w", encoding="utf-8")
    text = ""
    for applicant in applicants_list:
        text += applicant[0] + " " + applicant[1] + " " + str(applicant[2]) + "\n"
    file.write(text)
    file.close()

def mean(applicant, exam_index):
    if len(exam_index) == 1:
        return float(applicant[exam_index[0]])
    else:
        return (float(applicant[exam_index[0]]) + float(applicant[exam_index[1]])) / 2
           

limit = int(input())
file = open("applicant.txt", encoding="utf-8")
applicants = file.readlines()
file.close()

for i in range(len(applicants)):
    applicants[i] = applicants[i].split()
departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
successful_applicants = dict.fromkeys(departments)
for department in successful_applicants:
    successful_applicants[department] = []

exam_indexs = {"Biotech": [2, 3], "Chemistry": [3], "Engineering": [4, 5], "Mathematics": [4], "Physics": [2, 4]}

for priority in range(3): 
    for department in successful_applicants:
        value = successful_applicants[department]
        department_limit = limit - len(value)
        if department_limit <= 0:
            continue

        department_applicants = list(filter(lambda x: x[priority + 7] == department, applicants))
        exam_index = exam_indexs[department]
        department_applicants.sort(key=lambda x: (-max(mean(x, exam_index), float(x[6])), x[0] + x[1]))
           
        for i in range(min(department_limit, len(department_applicants))):
            applicant = department_applicants[i]
            value.append(applicant)
            applicants.remove(applicant)
        successful_applicants[department] = value

for department in successful_applicants:
    print(department)
#    print(department, len(successful_applicants[department]))
    applicants = successful_applicants[department]
    exam_index = exam_indexs[department]
    applicants.sort(key=lambda x: (-max(mean(x, exam_index), float(x[6])), x[0] + x[1]))
    for applicant in applicants:
        print(applicant[0], applicant[1], max(mean(applicant, exam_index), float(applicant[6])))
#        print(applicant)t
    print()

#print(applicants)

for department in successful_applicants:
    applicants_list = []
    applicants = successful_applicants[department]
    exam_index = exam_indexs[department]
    applicants.sort(key=lambda x: (-max(mean(x, exam_index), float(x[6])), x[0] + x[1]))
    for applicant in applicants:
        applicants_list.append([applicant[0], applicant[1], max(mean(applicant, exam_index), float(applicant[6]))])
    write_applicants(department, applicants_list)
