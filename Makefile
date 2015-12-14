all:
	pandoc -t beamer slides.md -o slides.pdf

clean:
	rm -f *.{aux,log,nav,out,snm,toc} 
