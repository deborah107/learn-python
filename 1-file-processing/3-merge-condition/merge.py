def merge():
    # Merge all lines for all SQL files in the 'sqls' folder that include these keywords: INSERT, UPDATE, DELETE
    #print()

    keywords = ["UPDATE", "INSERT", "DELETE"]

    from os import listdir
    from os.path import isfile, join
    files = [f for f in listdir("sqls") if isfile(join("sqls", f))]
    print(files)

    with open('merged.sql', 'w') as outfile:
        for content in files:
            with open(join("sqls", content)) as files1:
                for line in files1:
                    for keyword in keywords:
                        print(keywords, line)
                        if keyword in line:
                            outfile.write(line)