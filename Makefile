cv.pdf: cv.tex urlcheck
	rubber -d cv.tex
	rm -f cv.aux cv.out cv.log

clean:
	rm cv.pdf

urlcheck:
	./urlcheck.py cv.tex
