all:
	morloc make -o trim main.loc
	./nexus readFASTQ '"example.fastq"' | \
		./nexus trim config.json /dev/stdin | \
		./nexus writeFASTA '"obs.txt"' /dev/stdin

clean:
	rm -rf nexus* pool* __pycache__ trim
