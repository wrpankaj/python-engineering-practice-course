import pandas as pd

data = {
    "Student_ID": [101, 102, 103],
    "Quiz1": [20, 18, 25],
    "Quiz2": [25, 22, 25],
    "Quiz3": [30, 24, 25]
}

df = pd.DataFrame(data)

df.to_excel("student_quiz_input.xlsx", index=False)

df_read = pd.read_excel("student_quiz_input.xlsx")

df_read["Average"] = df_read[["Quiz1", "Quiz2", "Quiz3"]].mean(axis=1)

print(df_read)

df_read.to_excel("student_quiz_output.xlsx", index=False)

print("Output Excel file created successfully.")
