# Minimal makefile for Sphinx documentation
#

# Color codes
BLUE = "'\033[0;34m'"
NC = "'\033[0m'"

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

	@echo "\nAdditional custom ${BLUE}target${NC} not provided by sphinx:"
	@echo "  ${BLUE}serve${NC}       serve the built html to localhost:8000"

.PHONY: help Makefile

serve:
	@python -m http.server --directory build/html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
