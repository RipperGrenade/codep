if __name__ == '__main__':
    linelst = ['a\n', 'hello\n', 'b\n', 'world\n']
    generator_exp = (line.strip() for line in linelst if len(line) > 2)
