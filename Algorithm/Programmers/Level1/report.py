from typing import List
from collections import defaultdict

def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    id_report: defaultdict[str, List[str]] = defaultdict(list)
    report_count: defaultdict[tuple, int] = defaultdict(int)
    total_count: defaultdict[str, int] = defaultdict(int)
    mail_count: defaultdict[str, int] = defaultdict(int)

    # 초기화
    for id in id_list:
        id_report[id]
        mail_count[id]
    
    # 신고 횟수 저장
    for report_word in report:
        reporter, reported = report_word.split(" ")
        if report_count[(reporter, reported)] == 0:
            id_report[reporter].append(reported)
        report_count[(reporter, reported)] = 1

    # 누적 횟수 저장
    for report_list in report_count.keys():
        total_count[report_list[1]] += 1

    # 메일 카운트 저장
    for reported, count in total_count.items():
        if count >= k:
            for id, id_list in id_report.items():
                if reported in id_list:
                    mail_count[id] += 1

    answer: List[int] = list(mail_count.values())
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))