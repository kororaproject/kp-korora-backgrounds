SUBDIRS = default
VERSION = 20.0
NAME = heisenbug-backgrounds-$(VERSION)

all:
	@for i in $(SUBDIRS) ; do \
		(cd $$i; make) ;\
	done;

install:
	@for i in $(SUBDIRS) ; do \
		(cd $$i; make install) ; \
	done;

dist:
	mkdir -p $(NAME)
	#cp -a CC-BY-SA-3.0 $(NAME)
	#~ cp -a CC-BY-3.0 $(NAME)
	#cp -a Attribution $(NAME)
	#~ cp -a Attribution-Extras $(NAME)
	cp -a Makefile $(NAME)
	cp -a default $(NAME)
	#cp -a extras $(NAME)
	tar -c --xz -f $(NAME).tar.xz $(NAME)
	rm -rf $(NAME)

