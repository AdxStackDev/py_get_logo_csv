import os
import csv

# Path to images
folder_path = r'C:\Users\adity\Desktop\py\pytorch\logo\data\logo_1\Logos'

output_csv = 'logos_with_imgType.csv'

files = os.listdir(folder_path)

image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.svg'))]

rows = []
for file in image_files:
    name, ext = os.path.splitext(file)
    label = name.split('-')[0] if '-' in name else name
    # rows.append([name, label])
    # rows.append([file, name, label])
    rows.append([file, name, label, ext])    

# Creating CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['name', 'label'])
    writer.writerow(['image','name', 'label', 'img_type'])
    writer.writerows(rows)

print(f'Done! CSV file saved as {output_csv}')
