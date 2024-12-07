def solution(id_list, report, k):
    data = {}
    mailTo = {}

    for i in id_list: #각 이용자 id를 key로 가지는 딕셔너리 생성
        i = i.lower()
        data[i] = set([]) #이용자id: [신고한사람들]
        mailTo[i] = 0 #이용자id: 받은메일수

    for i in report: #value에 신고한 사람들의 id를 set형태로 삽입
        source, target = map(str, i.split(" "))
        data[target.lower()].add(source.lower())

    for user, reports in data.items():
        if len(reports) >= k:
            for i in reports:
                mailTo[i] += 1

    return list(mailTo.values())


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","Frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))