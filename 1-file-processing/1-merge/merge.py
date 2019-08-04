
def merge():
    """Merge "schools.sql" and "users.sql", save the merged file as "merged.sql"""
    # Provide implememntation here
    files = ['users.sql','schools.sql']
    with open('merged.sql', 'w') as outfile:
        for fname in files:
            with open(fname) as infile:
                outfile.write(infile.read())
