all:

clean:
	$(MAKE) clean -C tests/

tests_run:
	$(MAKE) -C tests/

.PHONY:	all clean