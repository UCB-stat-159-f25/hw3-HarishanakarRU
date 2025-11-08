.PHONY : env html clean

env:
	conda env update -f environment.yml

html:
	myst build --html

clean:
	rm -rf _build/* figures/* audio/*