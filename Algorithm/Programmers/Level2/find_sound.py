def solution(m, musicinfos):
    convert_list: list = [('A#', 'a'), ('C#', 'c'), ('D#', 'd'),
                          ('F#', 'f'), ('G#', 'g')]
    music_patterns: dict = {}
    
    for string in musicinfos:
        start, end, title, sound = map(str, string.split(','))
        start_hour, start_min = map(int, start.split(":"))
        end_hour, end_min = map(int, end.split(":"))
        total: int = (end_hour - start_hour) * 60 + (end_min - start_min)
        convert_sound = sound
        
        for target, converted in convert_list:
            convert_sound = convert_sound.replace(target, converted)
            
        total_sound: str = ''.join(list(convert_sound * (total // len(convert_sound) + 1))[:total])
        music_patterns[title] = (total, total_sound)
    
    for target, converted in convert_list:
        m = m.replace(target, converted)
        
    answer: tuple = (0, '(None)')
    for title, (length, sound) in music_patterns.items():
        if m in sound and answer[0] < length:
            answer = (length, title)
        
    return answer[1]

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))