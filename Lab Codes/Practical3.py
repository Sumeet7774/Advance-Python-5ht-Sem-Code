import csv

input_file = "student.csv"
output_file = "student_average_grades.csv"
student_grades ={}

with open(input_file ,'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row ["NAME"]
        maths_score = int(row["MATHS"])
        science_score = int(row["SCIENCE"])
        english_score = int(row["ENGLISH"])
        score= [maths_score, science_score, english_score]
        average_score = sum(score)/ len(score)
        student_grades[name] = average_score

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["NAME", "AVERAGE GRADE"])

    for name, average in student_grades.items():
        writer.writerow([name, average])

print("Average grades have been calculated and saved to 'student_average_grades.csv'.")