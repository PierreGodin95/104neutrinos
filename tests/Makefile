all: tests_run

clean:
	$(RM) .coverage

tests_run:
	coverage run -m unittest discover --start-directory . --verbose
	coverage report --omit=test_*

.PHONY:	all clean
