file_r = open('sample.txt', 'r')
file_w = open('copy.txt', 'w')
for line in file_r:
    file_w.write(line)
# 3,4行目では読み込んだファイルを1行ずつ新しいファイルに書き込む
file_r.close()
file_w.close()