.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9\/-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Formatting & linting

.PHONY: lint
lint: buf/deps ## Check protobuf files for linting errors
	buf lint

.PHONY: format
format: buf/deps ## Format protobuf files (in-place) using `buf format`.
	buf format -w

##@ Generating code

.PHONY: generate
generate: clean format lint ## Generate language bindings.
	uv run buf generate

.PHONY: clean
clean: ## Clean the directory with the generated language bindings.
	rm -rf gen/

##@ Dependencies

.PHONY: deps
deps: ## Install the required dependencies to use this project.
	HOMEBREW_NO_AUTO_UPDATE=1 brew install \
		bufbuild/buf/buf
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync


.PHONY: buf/deps
buf/deps: ## Install the required dependencies to work with the protobuf files.
	buf dep update
