all: cv.tex urlcheck
	rubber -d cv.tex
	rm -f cv.aux cv.out cv.log

urlcheck:
	./urlcheck.py cv.tex
