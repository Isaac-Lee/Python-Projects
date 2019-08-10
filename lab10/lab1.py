copy = input("복사할 파일의 경로와 이름을 입력하세요: ")

paste = input("복사한 파일을 저장할 경로와 이름을 입력하세요: ")

infile = open("%s" % copy, "r")
lines = infile.read()
infile.close()

outfile = open("%s" % paste, "a")
outfile.write(lines)
outfile.close()

print(outfile)