.PHONY: build_docker run_docker bash_docker stop_docker

build_docker:
	bash ./scripts/docker/build.sh

run_docker:
	bash ./scripts/docker/run.sh

bash_docker:
	bash ./scripts/docker/exec.sh

stop_docker:
	bash ./scripts/docker/stop.sh