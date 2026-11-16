from pathlib import Path
from zipfile import ZipFile

import pandas as pd


script_path = Path(__file__).resolve().parent
print(script_path)
project_root = script_path.parent
print(project_root)

archive_path = project_root / 'data' / 'raw' / 'January2015toNovember2025.zip'
print(archive_path)

if not archive_path.is_file():
    raise FileNotFoundError(f'Archive not found: {archive_path}')
print('Archive file found.')

file_size_bytes = archive_path.stat().st_size
print(f'File Size: {file_size_bytes:,} bytes')
file_size_mib = file_size_bytes / (1024 * 1024)
print(f'File Size: {file_size_mib:.2f} MiB')

with ZipFile(archive_path, 'r') as zip_file:
    file_list = zip_file.namelist()
    print(f'Number of Files in Archive: {len(file_list)}')
    print('Files in Archive:')
    for file_name in file_list:
        print(f' - {file_name}')
    if len(file_list) != 1 or not file_list[0].lower().endswith('.csv'):
        raise ValueError(f'Unexpected archive contents: {file_list}')
    csv_info = zip_file.getinfo(file_list[0])
    print(f'CSV File Info: {csv_info.file_size:,} bytes')
    print(f'Compressed Size: {csv_info.compress_size:,} bytes')
    compression_saving_percent = (
        1 - (csv_info.compress_size / csv_info.file_size)) * 100
    print(f'Compression Saving: {compression_saving_percent:.2f}%')
    bad_file = zip_file.testzip()
    if bad_file:
        raise ValueError(f'Corrupt file in archive: {bad_file}')
    print('No Bad Files Found in Archive')

df = pd.read_csv(
    archive_path,
    dtype={
        'Primary NAICS': 'string',
        'Inspection': 'string',
        'Zip': 'string',
    },
)
print(f'DataFrame Type: {type(df)}')
print(f'DataFrame Shape: {df.shape}')
print(f'DataFrame Columns: {df.columns.tolist()}')
print(f'DataFrame Types:\n{df.dtypes}')
print(
    f'DataFrame Head For 15 Rows, 2 Columns:\n'
    f'{df[["Primary NAICS", "Inspection"]].head(15)}')

print(f'Missing Primary NAICS: {df["Primary NAICS"].isna().sum()}')
print(f'Missing Inspection: {df["Inspection"].isna().sum()}')
print(f'Zip Sample: {df["Zip"].dropna().head(3).tolist()}')
print(f'Missing Zip: {df["Zip"].isna().sum()}')

df['EventDate'] = pd.to_datetime(df['EventDate'], format='%m/%d/%Y')
print(
    f'EventDate Min and Max: {df['EventDate'].min()} and {df['EventDate'].max()}')

columns_to_clean = ['EventTitle', 'Secondary Source Title', 'SourceTitle',
                    'Part of Body Title', 'NatureTitle', 'Employer']
for column in columns_to_clean:
    print(f'Unique {column} Before Stripping: {df[column].nunique()}')
    df[column] = df[column].str.strip().str.replace(r'\s+', ' ', regex=True)
    print(f'Unique {column} After Stripping: {df[column].nunique()}')

print(f'UPA Is Unique: {df['UPA'].is_unique}')
print(f'Rows Duplicate by ID: {df['ID'].duplicated(keep=False).sum()}')
