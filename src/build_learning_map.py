"""행사 주제를 검증 가능한 AI 인프라 학습 질문으로 변환한다."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LAYERS = [
    {
        "id": "data",
        "name": "1. 데이터",
        "question": "학습·추론 데이터는 어디서 오고, 품질과 접근 권한은 어떻게 검증하는가?",
        "practice": "작은 CSV의 결측치·중복·스키마를 검사하고 처리 전후 행 수를 기록한다.",
    },
    {
        "id": "compute",
        "name": "2. 연산",
        "question": "CPU·GPU·가속기의 선택이 지연시간·비용·전력에 어떤 영향을 주는가?",
        "practice": "같은 추론 작업의 실행 시간과 메모리 사용량을 조건별로 비교한다.",
    },
    {
        "id": "storage_network",
        "name": "3. 저장·네트워크",
        "question": "대용량 데이터가 연산 장치에 병목 없이 도달하도록 어떻게 설계하는가?",
        "practice": "파일 크기별 읽기 시간을 반복 측정하고 평균·편차를 표로 남긴다.",
    },
    {
        "id": "platform",
        "name": "4. AI 플랫폼",
        "question": "모델 학습·배포·버전·롤백을 어떤 단위로 관리하는가?",
        "practice": "모델 버전, 데이터 버전, 지표, 배포 시각을 한 JSON 문서에 연결한다.",
    },
    {
        "id": "operations",
        "name": "5. 운영·보안·성과",
        "question": "정확도 외에 안전성·관측성·비용·업무 결과를 어떻게 함께 판단하는가?",
        "practice": "오류율·응답시간·비용·사람의 검토 비율을 함께 보는 운영 표를 설계한다.",
    },
]


def build_map() -> dict:
    facts = json.loads((ROOT / "data" / "event_facts.json").read_text(encoding="utf-8"))
    return {
        "event": facts["event"],
        "generated_for": "post-event learning review",
        "principle": "제품 이름보다 데이터 흐름과 검증 질문을 우선한다.",
        "layers": LAYERS,
        "claim_boundary": [
            "공개 자료로 확인한 행사 사실",
            "로컬 기록으로 확인한 부스 방문 후속 메일 제목",
            "행사 후 재구성한 학습 질문과 후속 실습",
        ],
    }


def write_outputs(result: dict) -> None:
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    (out / "learning_map.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [f"# {result['event']} 학습 지도", "", result["principle"], ""]
    for layer in result["layers"]:
        lines += [f"## {layer['name']}", "", f"- 질문: {layer['question']}", f"- 후속 실습: {layer['practice']}", ""]
    (out / "learning_map.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    write_outputs(build_map())
    print(f"generated {len(LAYERS)} infrastructure layers")


