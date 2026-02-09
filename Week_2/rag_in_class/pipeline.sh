#!/bin/bash
python zero_shot_refactor.py
cd dataset/outputs
python -m pytest -q 2>&1 | tee explanations/pytest_error_log.txt
