def merge():
    # - Merge all files with an `.sql` extension in the folder `sqls`
    # - Save the file to `merged.sql`
    # provide implementation here

    

    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("sqls") if isfile(join("sqls", f))]
    print(onlyfiles)

    with open('merged.sql', 'w') as outfile:
        for fname in onlyfiles:
            with open(join("sqls", fname)) as infile:
                outfile.write(infile.read())
