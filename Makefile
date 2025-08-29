.PHONY: run summarize sweep

run:
	python3 code/dtg_simulation.py

summarize:
	python3 code/summarize_last_run.py

sweep:
	python3 code/run_experiment.py
