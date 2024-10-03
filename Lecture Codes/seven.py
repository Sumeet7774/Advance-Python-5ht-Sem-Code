import csv
import pandas as pd;

input_file = "student_grades.csv"
output_file = "student_average_grades.csv"
student_grades = {}

with open(input_file,"r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        name=row["Name"]
        math_score=int(row['Maths'])
        science_score=int(row["Science"])
        english_score=int(row["English"])
        score=[math_score,science_score,english_score]
        average_score=sum(score)/len(score)
        student_grades[name]=average_score
        

calculate_average = lambda scores: sum(scores)/len(scores)

def main():
    input_file = "student_grades.csv"
    df = pd.read_csv(input_file)
    df["Average"] = df.apply(lambda row: 
        calculate_average([row["Maths"], row["Science"], row["English"]]), axis=1)