#Use a loop to iterate over all rows in the moma list of lists. For each row:


for row in moma:
    gender = row[5]
    gender = gender.title()
    
    if not gender:
        gender = 'Gender Unknown/Other'
    row[5] = gender
    
    nationality = row[2]
    nationality = nationality.title()
    
    if not nationality:
        nationality = 'Nationality Unknown'
    row[2] = nationality