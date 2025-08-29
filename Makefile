.PHONY: run summarize sweep all help

run:
	python3 code/dtg_simulation.py

summarize:
	python3 code/summarize_last_run.py

sweep:
	python3 code/run_experiment.py

# run 후 summarize를 연속 실행
all: run summarize

help:
	@echo "make run        # 단일 실험 실행"
	@echo "make summarize  # 가장 최근 run 요약/아카이브"
	@echo "make sweep      # 알파 스윕 자동 실행"
	@echo "make all        # run + summarize"
