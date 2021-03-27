#!/bin/bash
PYTHON = python3

help:
	@echo "Para compilar o programa digite 'make all'"
	@echo "Para executar o programa digite 'make run'"


all:
	${PYTHON} -m py_compile src/main.py

run:
	${PYTHON} src/main.py
