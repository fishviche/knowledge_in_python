with open("./sql/1_table.sql", "r") as f:
    sentences = [x.replace("\n", "") + ";" for x in f.read().rsplit(";") if x != ""]
    print(sentences)

# print(sql_file)
# print(sql_file.read().split(';'))
