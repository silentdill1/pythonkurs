def dragon_curve(max_order, current_order=0, curve='F'):
    if max_order == current_order:
        return curve
    else:
        character_list = list(curve)
        curve += 'L'
        for character in reversed(character_list):
            if character == 'F':
                curve += 'F'
            elif character == 'L':
                curve += 'R'
            elif character == 'R':
                curve += 'L'
        return dragon_curve(max_order, current_order+1, curve)


for i in range(0, 6):
    print(dragon_curve(i))


