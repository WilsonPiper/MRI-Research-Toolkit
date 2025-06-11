import pandas as pd

def count_patients_by_diagnosis(csv_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Check if the diagnosis column exists
        if "Research Group" not in df.columns:
            raise ValueError(f"Research Group not found in the CSV file.")
        
        # Count occurrences of each diagnosis
        diagnosis_counts = df["Research Group"].value_counts().to_dict()
        
        return diagnosis_counts
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def count_unique_patients_by_diagnosis(csv_file, subject_col="Subject ID", diagnosis_col="Research Group"):
    try:
        df = pd.read_csv(csv_file)
        
        if diagnosis_col not in df.columns:
            raise ValueError(f"Column '{diagnosis_col}' not found.")
        if subject_col not in df.columns:
            raise ValueError(f"Column '{subject_col}' not found.")
        
        unique_subjects = df.drop_duplicates(subset=[subject_col])
        
        diagnosis_counts = unique_subjects[diagnosis_col].value_counts().to_dict()
        
        return diagnosis_counts
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return {}
    except Exception as e:
        print(f"Error: {e}")
        return {}

if __name__ == "__main__":
    csv_file = "replace_with_csv_name"
    
    counts = count_patients_by_diagnosis(csv_file)
    
    if counts:
        print("Number of scans:")
        total = sum(counts.values())
        for diagnosis, count in counts.items():
            print(f"{diagnosis}: {count}")
        print(f"Total MRI Scans: {total}")
    
    # Get counts
    unique_counts = count_unique_patients_by_diagnosis(csv_file)
    
    if unique_counts:
        print("Unique patients by diagnosis:")
        total = sum(unique_counts.values())
        for diagnosis, count in unique_counts.items():
            print(f"{diagnosis}: {count}")
        print(f"Total unique subjects: {total}")
