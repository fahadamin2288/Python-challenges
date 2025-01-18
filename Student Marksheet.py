import pandas as pd

def get_subjects_and_marks():
    subjects = []
    obtained_marks = []
    
    while True:
        subject = input("Enter the subject (or type 'stop' to finish): ")
        if subject.lower() == 'stop':
            break
        marks = int(input(f"Enter the marks obtained in {subject} (out of 100): "))
        subjects.append(subject)
        obtained_marks.append(marks)
    
    return subjects, obtained_marks

def calculate_percentage(marks_obtained):
    return (marks_obtained / 100) * 100

def determine_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def apply_star_pass_system(df):
    fail_count = 0
    star_pass_index = -1

    # Count fails and determine if a star pass should be applied
    for idx in range(len(df)):
        if df.loc[idx, "Obtained Marks"] < 33:
            fail_count += 1
            if df.loc[idx, "Obtained Marks"] >= 28:
                star_pass_index = idx  # Store index of potential star pass

    # Apply pass statuses
    for idx in range(len(df)):
        if fail_count == 1 and idx == star_pass_index:
            df.loc[idx, "Pass Status"] = f"{df.loc[idx, 'Obtained Marks']}*"
        elif df.loc[idx, "Obtained Marks"] >= 33:
            df.loc[idx, "Pass Status"] = "Pass"
        else:
            df.loc[idx, "Pass Status"] = "Fail"

    return df

def main():
    subjects, obtained_marks = get_subjects_and_marks()
    
    # Initialize DataFrame
    data = {
        "Subject": subjects,
        "Total Marks": [100] * len(subjects),
        "Obtained Marks": obtained_marks
    }
    
    df = pd.DataFrame(data)
    
    # Calculate percentage for each subject
    df["Percentage"] = df["Obtained Marks"].apply(calculate_percentage)
    
    # Determine grade for each subject
    for idx in range(len(df)):
        df.loc[idx, "Grade"] = determine_grade(df.loc[idx, "Percentage"])
    
    # Apply pass/fail status initially
    for idx in range(len(df)):
        df.loc[idx, "Pass Status"] = "Pass" if df.loc[idx, "Obtained Marks"] >= 33 else "Fail"
    
    # Apply the star pass system
    df = apply_star_pass_system(df)
    
    # Check for distinction
    for idx in range(len(df)):
        if df.loc[idx, "Percentage"] >= 75:
            df.loc[idx, "Distinction"] = "Distinction"
        else:
            df.loc[idx, "Distinction"] = "No"
    
    # Print the DataFrame
    print("\nStudent Marksheet:")
    print(df)
    
    # Calculate total percentage, grade, and distinction
    total_obtained_marks = df["Obtained Marks"].sum()
    total_percentage = total_obtained_marks / (100 * len(subjects)) * 100
    total_grade = determine_grade(total_percentage)
    total_distinction = "Distinction" if total_percentage >= 75 else "No"
    
    # Check if the student failed any subjects
    failed_subjects = df[df["Pass Status"] == "Fail"]
    
    if len(failed_subjects) == 0:
        print(f"\nTotal Obtained Marks: {total_obtained_marks}")
    else:
        print(f"\nTotal Obtained Marks: ")

    print("\nFinal Results:")
    print(f"Total Percentage: {total_percentage:.2f}%")
    print(f"Total Grade: {total_grade}")
    print(f"Total Distinction: {total_distinction}")

if __name__ == "__main__":
    main()
