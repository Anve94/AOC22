from os import path

def input_to_sections() -> list:
    here = path.dirname(path.abspath(__file__))
    filename = path.join(here, '04.txt')
    sections = []
    
    with open(filename, 'r') as f:
        lines = f.read().strip().split()
        for line in lines:
            line_sections = line.split(',')
            left_sections = line_sections[0].split('-')
            right_sections = line_sections[1].split('-')
            sections.append(
                {
                    'left_min': int(left_sections[0]),
                    'left_max': int(left_sections[1]),
                    'right_min': int(right_sections[0]),
                    'right_max': int(right_sections[1])
                    
                }
            )
            
    return sections

def count_section_overlap(sections: list) -> int:
    count = 0
    for section in sections:
        if has_section_overlap(section):
            count += 1
            
    return count

def has_section_overlap(section: dict) -> bool:
    # 6-8,6-6 has overlap because right_min >= left_min and right_max <= left_max
    # 5-7,2-9 has overlap because left_min >= right_min and left_max <= right_max
    if section['right_min'] >= section['left_min'] and section['right_max'] <= section['left_max']:
        return True
    
    if section['left_min'] >= section['right_min'] and section['left_max'] <= section['right_max']:
        return True
    
    return False

sections = input_to_sections()
print(count_section_overlap(sections))