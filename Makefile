default:
	@echo "call 'make create_dotenv' to create .env file"
	@echo "call 'make clean' to fresh install"

create_dotenv:
	./scripts/gen_dotenv.sh > .env

clean:
	./scripts/clean.sh

test:
	./scripts/test.sh
