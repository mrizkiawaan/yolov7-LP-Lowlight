import splitfolders

# Replace 'LP_Lowlight_Dataset_Resized' with the path to your dataset folder
input_folder = "Dataset/input_ds"

# Define the output folder where the split dataset will be saved
output_folder = "Dataset/split2"

# Define the split ratio
split_ratio = (0.8, 0.1, 0.1)  # 80% for training, 10% for validation, 10% for testing

# Split the dataset using split-folders
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=split_ratio, group_prefix=2)
