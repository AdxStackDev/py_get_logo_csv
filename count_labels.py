import pandas as pd

# Path to your CSV file
csv_path = 'logos_with_imgType.csv'  # Update if needed

# Read CSV
df = pd.read_csv(csv_path)

print('First few rows:')
print(df.head())

# Count how many images per label
label_counts = df['label'].value_counts().reset_index()
label_counts.columns = ['label', 'image_count']

print('\nLabel counts:')
print(label_counts)

# Save to CSV
label_counts.to_csv('label_counts.csv', index=False)
print('\nSaved label counts to label_counts.csv')

# Total unique labels (categories)
total_labels = label_counts.shape[0]
print(f'\nTotal unique labels (categories): {total_labels}')

# Total images
total_images = df.shape[0]
print(f'Total images: {total_images}')
