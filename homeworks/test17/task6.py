def work_with_file(path):
    with open(path, 'r') as file:
        content_lines = file.readlines()
    line_count = len(content_lines)
    word_count = 0
    for i in content_lines:
        word_count += len(i.split())
    letter_count = 0
    for i in content_lines:
        for word in i.split():
            letter_count += len(word)
    output_text = (
        f'String count: {line_count}\n'
        f'Word count: {word_count}\n'
        f'Letter count: {letter_count}\n'
    )
    with open(path, 'a') as file:
        file.write(output_text)
    print(output_text)


work_with_file(
    'C:\\Homework\\template-py-sdet-course-clone-hm4\\'
    'homeworks\\test17\\task6.txt'
)
