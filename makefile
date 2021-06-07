.PHONY: all
all: combos_count.pdf
	
%.pdf: %.md
	pandoc -V geometry:margin=1in $^ -o $@
