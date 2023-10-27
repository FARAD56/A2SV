class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = words[0]
        array = []
        for i in range(1,len(words)):
            if len(line + " " + words[i]) <= maxWidth:
                line += (" " + words[i])
            else:
                array.append(line)
                line = words[i]
        array.append(line)

        def spacing(line):
            line = line.split()
            if len(line) > 1:
                total = 0
                for char in line:
                    total += len(char)
                spaces = maxWidth - total
                holes = spaces//(len(line) -1)
                left = spaces%(len(line) -1)
                for i in range(len(line)-1):
                    line[i] = line[i] + (' '*holes)
                for i in range(left):
                    line[i] = line[i] + ' '
            else:
                line[0] += ' '*(maxWidth-len(line[0]))
            return ''.join(line)

        for i in range(len(array)-1):
            array[i] = spacing(array[i])

        array[-1] += (maxWidth - len(array[-1]))*" "
            
            
        return array
        