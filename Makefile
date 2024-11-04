COMPOSE = sudo docker compose

.PHONY: docker-build build-pdf build-clean clean


build-clean: build-pdf clean

build-pdf: latex
	rm -f TCC_FGA.pdf
	$(COMPOSE) up
	cp latex/TCC_FGA.pdf TCC_FGA.pdf 

clean:
		$(COMPOSE) run latex bash -c 'make clean'

docker-build: docker-compose.yml Dockerfile 
	$(COMPOSE) build latex