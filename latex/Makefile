TARGET = TCC_FGA.pdf

LATEX = pdflatex
BIBTEX = bibtex

VERSION = 0.1.0

FIXOS_DIR = fixos
FIXOS_SOURCES = informacoes.tex fichaCatalografica.tex folhaDeAprovacao.tex pacotes.tex comandos.tex setup.tex listasAutomaticas.tex indiceAutomatico.tex
FIXOS_FILES = $(addprefix $(FIXOS_DIR)/, $(FIXOS_SOURCES))
EDITAVEIS_DIR = editaveis
EDITAVEIS_SOURCES = informacoes.tex errata.tex dedicatoria.tex agradecimentos.tex epigrafe.tex resumo.tex abstract.tex abreviaturas.tex simbolos.tex Capitulo1.tex textoepostexto.tex apendices.tex anexos.tex
EDITAVEIS_FILES = $(addprefix $(EDITAVEIS_DIR)/, $(EDITAVEIS_SOURCES))
AUXILIARES_DIR = auxiliares
AUXILIARES_SOURCES = aspectosgerais.tex consideracoes.tex elementosdotexto.tex elementosdopostexto.tex
AUXILIARES_FILES = $(addprefix $(AUXILIARES_DIR)/, $(AUXILIARES_SOURCES))

MAIN_FILE = tcc.tex
DVI_FILE  = $(addsuffix .dvi, $(basename $(MAIN_FILE)))
AUX_FILE  = $(addsuffix .aux, $(basename $(MAIN_FILE)))
PS_FILE   = $(addsuffix .ps, $(basename $(MAIN_FILE)))
PDF_FILE  = $(addsuffix .pdf, $(basename $(MAIN_FILE)))

SOURCES = $(FIXOS_FILES) $(EDITAVEIS_FILES)

.PHONY: all clean dist-clean

EPS_FILES = $(wildcard figuras/*.eps)
EPS_TO_PDF_FILES= $(addsuffix .pdf, $(basename $(EPS_FILES)))

all: 
	@make $(TARGET)

$(TARGET): $(MAIN_FILE) $(SOURCES) bibliografia.bib $(EPS_TO_PDF_FILES)
	echo $(EPS_TO_PDF_FILES)
	$(LATEX) $(MAIN_FILE)
	$(BIBTEX) $(basename $(MAIN_FILE))
	$(LATEX) $(MAIN_FILE)
	$(LATEX) $(MAIN_FILE)
	@cp $(PDF_FILE) $(TARGET)   

%.pdf: %.eps
	epstopdf $<

clean-soft:
	rm -f *~ *.dvi *.ps *.backup *.aux *.log
	rm -f *.lof *.lot *.bbl *.blg *.brf *.toc *.idx
	rm -f tcc.pdf

clean: clean-soft
	rm -f *.pdf
	
dist: clean-soft
	tar vczf tcc-fga-latex-$(VERSION).tar.gz *

dist-clean: clean
	rm -f $(PDF_FILE) $(TARGET)