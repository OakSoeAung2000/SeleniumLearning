# file = open("text.txt")
#
# # line = file.readline()
# #
# # while line!="":
# #     print(line)
# #     line = file.readline()
#
# for line in file.readlines():
#     print(line)
#
# file.close()

with open('text.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)