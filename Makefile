.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9\/-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


##@ Setup
.PHONY: bootstrap/uv
bootstrap/uv:
	@case "$$(uname -s)" in \
		Darwin*) which uv || HOMEBREW_NO_AUTO_UPDATE=1 brew install uv ;; \
		Linux*) which uv || curl -LsSf https://astral.sh/uv/install.sh | sh ;; \
		*) echo -e "\033[33mCannot install 'uv' automatically. Install manually instead: https://docs.astral.sh/uv/getting-started/installation/#standalone-installer\033[0m" ;; \
	esac

.PHONY: bootstrap
bootstrap: bootstrap/uv ## Install the required dependencies to use this project.

##@ Formatting & linting

.PHONY: lint
lint: buf/deps ## Check protobuf files for linting errors.
	buf lint
ifneq ($(ALLOW_BREAKING),true)
	buf breaking --against https://github.com/qdrant/qdrant-cloud-public-api.git
else
	@echo "⚠️  Skipping buf breaking checks..."
endif

.PHONY: format
format: buf/deps ## Format protobuf files (in-place) using `buf format`.
	buf format -w

##@ Generating code

.PHONY: generate
generate: clean format lint ## Generate language bindings.
	uv run buf generate
	./scripts/cleanup-gencode-comments.sh
	rm -rf gen-dummy/

.PHONY: build-go
build-go:
	go build ./...

.PHONY: clean
clean: ## Clean the directory with the generated language bindings.
	rm -rf gen/
	rm -rf gen-dummy/

##@ Dependencies

.PHONY: deps
deps: ## Install the required dependencies to use this project.
	HOMEBREW_NO_AUTO_UPDATE=1 brew install \
		bufbuild/buf/buf uv
	uv sync

.PHONY: buf/plugins
buf/plugins: ## Install the required buf plugins (those that can't be installed using Buf's deps option).
	go install github.com/qdrant/qdrant-cloud-buf-plugins/cmd/buf-plugin-required-fields@latest && \
	go install github.com/qdrant/qdrant-cloud-buf-plugins/cmd/buf-plugin-method-options@latest && \
	go install github.com/qdrant/qdrant-cloud-buf-plugins/cmd/buf-plugin-permissions-breaking@latest

.PHONY: buf/deps
buf/deps: buf/plugins ## Install the required dependencies to work with the protobuf files.
	buf dep update

.PHONY: python/dev-install
python/dev-install: ## Install the required Python dependencies to work with the project.
	uv sync \
		--dev \
		--locked

.PHONY: py.sdist.public-api
py.sdist.public-api:
	rm -rf dist
	uv build -v \
		--sdist \
		.
