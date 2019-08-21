def merge():
    # - Merge all files with an `.sql` extension in the folder `sqls`
    # - Save the file to `merged.sql`
    # provide implementation here

    #print()

    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("sqls") if isfile(join("sqls", f))]

    files = ['schools.sql','users.sql']
    with open('merged.sql', 'w') as outfile:
        for fname in files:
            with open(fname) as infile:
                outfile.write(infile.read())
