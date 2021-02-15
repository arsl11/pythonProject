def open_or_senior(data):
    # categories = []
    # for i in data:
    #     if i[0] >= 55 and i[1] > 7:
    #         categories.append("Senior")
    #     else:
    #         categories.append("Open")
    # return categories
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(data))
