def get_median_font_size(font_sizes):
    # font_sizes_sorted = sorted(font_sizes)
    # mid = len(font_sizes_sorted) // 2
    # if (len(font_sizes_sorted) == 0):
    #     return None
    # if (len(font_sizes_sorted) % 2 == 0):
    #     median = font_sizes_sorted[mid - 1]
    # else:
    #     median = font_sizes_sorted[mid]
    # return median

    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]


print (get_median_font_size([10, 8, 6, 5]))