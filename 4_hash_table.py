def process_numbers_simple(input_file="input.txt", output_file="output.txt"):

    numbers = []
    result = []

    with open(input_file, "r") as f_in:
        nums_str = f_in.read().split()  # Чтение чисел и преобразование их в строки
        nums = [int(num) for num in nums_str]  # Теперь, наоборот, в числа

    for num in nums:
        if num > 0:
            if num not in result:
                result.append(num)
        elif num < 0:
            abs_num = abs(num)
            if abs_num in result:
                result.remove(abs_num)
        else:
            result.sort()
            with open(output_file, "w") as f_out:
                f_out.write(
                    " ".join(map(str, result))
                )  # Вследствие нехитрых преобзований, числа выводятся в файле output.txt через пробел
            return


process_numbers_simple()
