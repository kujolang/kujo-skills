.PHONY: validate lint format-check clean-checkout

validate:
	bash tests/release-readiness.sh

lint:
	python3 scripts/validate_skills.py

format-check:
	git diff --check

clean-checkout:
	bash tests/clean-checkout.sh
