import koik

# Read the CSV file and process the data
with open('your_file.csv', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # Create a list to store the processed data
    processed_data = []

    for row in csv_reader:
        # Splitting the full-time score to extract goals
        home_goals, away_goals = map(int, row['lõppseis'].split(' - '))

        # Extracting team names, year, and constructing the desired format
        processed_row = [
            row['kodu'],  # Home team
            row['võõras'],  # Away team
            row['aasta'],  # Year
            home_goals,  # Home team goals
            away_goals  # Away team goals
        ]

        # Append processed row to the list
        processed_data.append(processed_row)

# Enumerating and printing the formatted data
for idx, match in enumerate(processed_data, start=1):
    print(f"{match[0]}, {match[1]}, {match[2]}, {match[3]}, {match[4]}")

