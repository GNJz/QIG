# QIG — Spiking Neural Intelligence *(Planaria Project)*

> **초저전력 SNN × 다중 AI 합의(Multi-Agent Consensus)** 기반 연구 레포  
> LIF 뉴런 + 동적 임계값 게이팅(DTG) 실험 및 시뮬레이션.  
> 재현 가능한 **코드 · 데이터 · 그래프** 포함.

---

## 📌 Notice

- 데이터와 그림은 **실행 시 자동 생성**됩니다.
- 저장소에서는 **메타 파일**(`config.json`, `metadata.json`)만 버전 관리합니다.
- 대용량 이미지(`figures/*.png`)는 **Git LFS**를 사용하세요.

---

## 📂 Folder Structure

```plaintext
QIG/
├── code/                     # 시뮬레이션 및 유틸 코드
│   ├── dtg_simulation.py     # 메인: LIF + Dynamic Threshold Gating
│   ├── lif_model.py          # LIF 뉴런 (refractory 포함)
│   ├── utils.py              # CSV / JSON / 경로 헬퍼
│   └── requirements.txt      # 실행 패키지 목록
│
├── data/                     # 실행 산출물 (CSV, 메타)
│   ├── config.json           # 마지막 실행 파라미터 스냅샷
│   ├── spikes.csv            # [run_id, ts, alpha, spikes]
│   ├── energy.csv            # [run_id, ts, alpha, energy_proxy]
│   └── metadata.json         # 실험 메타데이터
│
├── figures/                  # 실행 산출물 (그래프)
│   ├── membrane_alpha_1.0.png
│   ├── membrane_alpha_0.7.png
│   └── membrane_alpha_0.5.png
│
├── logs/                     # 로그 및 메모
│   ├── ai_consensus.log
│   ├── meeting_notes.md
│   └── version_history.md
│
├── paper_v1.0.md             # 논문 초안 (KR/EN 병기 예정)
└── README.md

---

# 1. 의존성 설치
python3 -m pip install -r code/requirements.txt

# 2. 시뮬레이션 실행
python3 code/dtg_simulation.py

결과:
	•	data/spikes.csv, data/energy.csv → 누적 기록
	•	figures/membrane_alpha_{1.0,0.7,0.5}.png → 그래프 자동 저장

⸻

---

📌 Next Steps
	•	LIF 뉴런 기반 시뮬레이션 자동화 및 시각화 고도화
	•	Multi-Agent Consensus 실험 준비
	•	논문 초안(paper_v1.0.md) KR/EN 병기 작성

---

🔗 Links
	•	GitHub: https://github.com/GNJz/QIG

