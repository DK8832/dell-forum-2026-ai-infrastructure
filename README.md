# Dell Technologies Forum 2026 현장 체험과 AI·인프라 기술 탐색

2026년 8월 25일 서울 코엑스 그랜드볼룸에서 열린 Dell Technologies Forum 2026을 계기로, 현장에서 접한 기업 AI 인프라의 관점을 `데이터 → 연산 → 플랫폼 → 운영·보안 → 성과`의 다섯 층으로 다시 정리한 학습 기록이다.

이 저장소는 **확인된 사실**, **개인 활동 증빙**, **행사 후 재구성한 학습 내용**을 구분한다. 현장 방문 근거는 로컬 브라우저 기록에서 확인한 AIS테크놀러지의 `DellTechForum 2026 당사 부스 방문에 감사드립니다` 메일 제목이다. 메일 주소와 본문 등 개인정보는 저장소에 공개하지 않았다.

## 결과물

- `index.html`: 다섯 층 AI 인프라 탐색 페이지
- `data/event_facts.json`: 공식·공개 출처로 재확인한 행사 사실
- `src/build_learning_map.py`: 행사 주제를 학습 질문과 후속 실습으로 변환
- `outputs/learning_map.json`, `outputs/learning_map.md`: 실제 실행 결과
- `docs/IMR_PORTFOLIO.md`: IMR용 상세 원고
- `docs/VERIFICATION.md`: 주장·출처·개인정보 검증 기록

## 실행

```bash
python src/build_learning_map.py
python -m unittest discover -s tests -v
```

`index.html`은 별도 설치 없이 브라우저에서 열 수 있다.

## 핵심 학습

AI는 모델 하나만으로 서비스되지 않는다. 데이터가 이동·정제·보호되는 과정, GPU·CPU·스토리지의 역할, 모델 배포와 관측, 보안·거버넌스가 연결되어야 비즈니스 성과로 이어진다. 그래서 제품 이름을 나열하는 대신 각 층에서 반드시 답해야 할 질문과 작은 검증 실습을 만들었다.

## 사실 경계

- 확인: 행사 날짜·시간·장소·주제, Dell 공식 행사 성격, AIS테크놀러지의 부스 방문 감사 메일 제목
- 행사 후 정리: 다섯 층 구조, 비교 질문, 후속 실습 계획
- 주장하지 않음: 모든 세션 참석, 특정 제품 직접 조작, 성능 수치 측정, 수상·인증·도입 성과

## 출처

- [Dell Technologies Forum 2026 공식 안내](https://www.dell.com/ko-kr/lp/forums-calendar)
- [행사 일정·장소 안내](https://event-us.kr/dtf2026/event/130951)
- [Dell Technologies World 2026 세션 요약](https://www.dell.com/content/dam/web-resources/project-specific/events/dell-technologies-world/2026/files/unleash-the-future-k-01-session-summary.pdf)


