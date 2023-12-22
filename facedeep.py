import os
import pandas as pd
from deepface import DeepFace

def process_images(folder_path):
    results = []

    # Check if the folder exists and has files
    if not os.path.exists(folder_path) or not os.listdir(folder_path):
        print(f"Folder not found or empty: {folder_path}")
        return

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {file_path}")  # Debug print

            # Analyze the image
            try:
                analysis = DeepFace.analyze(file_path, actions=['age', 'gender', 'race'])
                print(f"Analysis result for {filename}: {analysis}")  # Debug print

                # Assuming analysis is a list of dictionaries
                analysis_dict = {k: v for d in analysis for k, v in d.items()}

                result = {
                    "Filename": filename,
                    "Gender": analysis_dict.get("gender"),
                    "Race/ethnicity": analysis_dict.get("dominant_race"),
                    "Age": analysis_dict.get("age")
                }
                results.append(result)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Check if results were obtained
    if results:
        # Convert results to DataFrame and save as CSV
        df = pd.DataFrame(results)
        output_path = os.path.join(folder_path, "output.csv")
        df.to_csv(output_path, index=False)
        print(f"Results saved to {output_path}")
    else:
        print("No results to save.")

# Replace 'faceimages' with the path to your image folder
process_images("C:/Users/ambar/Downloads/faceimages")
