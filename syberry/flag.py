class ArgumentError(ValueError):
    pass


def flag(N):
    if not isinstance(N, int) or N % 2:
        raise ArgumentError(
            'ArgumentError: Value should be an integer even number'
        )
    # first row - border
    result_list = ['#' * (3 * N + 2)]
    # add vertical distance to circle
    vertical_distance_string = (' ' * (3 * N)).center(3 * N + 2, '#')
    result_list.extend([vertical_distance_string] * int(N / 2))
    # add half of circle
    result_list.extend([('*' + 'o' * i + '*').center(3 * N).center(
        3 * N + 2, '#') for i in range(0, N, 2)])
    # generate flag
    result = '\n'.join(result_list)
    return '\n'.join([result, result[::-1]]) 


# if __name__ == "__main__":
#     print(flag(2))
#     print(flag(4))
#     print(flag(6))
#     print(flag(16))
