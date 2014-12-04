KORORA_DIR=$(DESTDIR)/usr/share/backgrounds/korora
GNOME_BG_DIR=$(DESTDIR)/usr/share/gnome-background-properties
KDE_BG_DIR=$(DESTDIR)/usr/share/wallpapers/
MATE_BG_DIR=$(DESTDIR)/usr/share/mate-background-properties
XFCE_BG_DIR=$(DESTDIR)/usr/share/xfce4/backdrops
INKSCAPE=/usr/bin/inkscape
MKDIR=/bin/mkdir -p
INSTALL=/usr/bin/install -p -m644 -D
LN_S=/bin/ln -s

all:

install:
	$(MKDIR) $(KORORA_DIR)/default/wide
	$(MKDIR) $(KORORA_DIR)/default/tv-wide
	$(MKDIR) $(KORORA_DIR)/default/standard
	$(MKDIR) $(KORORA_DIR)/default/normalish
	$(MKDIR) $(KORORA_DIR)/default-animated/wide
	$(MKDIR) $(KORORA_DIR)/default-animated/tv-wide
	$(MKDIR) $(KORORA_DIR)/default-animated/standard
	$(MKDIR) $(KORORA_DIR)/default-animated/normalish
	$(MKDIR) $(GNOME_BG_DIR)
	for size in normalish standard wide tv-wide; do \
	  $(INSTALL) $${size}/korora-01-day.png		    $(KORORA_DIR)/default/$${size}/korora.png ; \
	  $(LN_S) ../../default/$${size}/korora.png	    $(KORORA_DIR)/default-animated/$${size}/korora-01-day.png ; \
	  for tod in 00-dawn 02-dusk 03-night; do \
	    $(INSTALL) $${size}/korora-$${tod}.png 		$(KORORA_DIR)/default-animated/$${size}/korora-$${tod}.png ; \
	  done; \
	done;

	$(INSTALL) korora.xml         		            $(KORORA_DIR)/default/korora.xml
	#$(INSTALL) desktop-backgrounds-korora.xml 		$(GNOME_BG_DIR)/korora.xml
	$(INSTALL) korora-animated.xml         		            $(KORORA_DIR)/default-animated/korora.xml
	$(INSTALL) desktop-backgrounds-korora-animated.xml 		$(GNOME_BG_DIR)/korora-animated.xml
	$(MKDIR) $(KDE_BG_DIR)/Korora/contents/images
	$(INSTALL) korora-metadata.desktop $(KDE_BG_DIR)/Korora/metadata.desktop
	for res in 640x480 800x600 1024x768 1152x864 1200x900 1280x960 1440x1080 1600x1200 1600x1280 1920x1440 2048x1536; do \
	  $(LN_S) ../../../../backgrounds/korora/default/standard/korora.png \
	          $(KDE_BG_DIR)/Korora/contents/images/$${res}.png ; \
	done;
	for res in 1280x1024 ; do \
	  $(LN_S) ../../../../backgrounds/korora/default/normalish/korora.png \
	          $(KDE_BG_DIR)/Korora/contents/images/$${res}.png ; \
	done;
	for res in 800x480 1024x600 1152x720 1280x720 1280x768 1280x800 1366x768 1440x900 1680x1050 1920x1080 1920x1200 ; do \
	  $(LN_S) ../../../../backgrounds/korora/default/wide/korora.png \
	          $(KDE_BG_DIR)/Korora/contents/images/$${res}.png ; \
	done;

	$(MKDIR) $(MATE_BG_DIR)
	#$(INSTALL) mate-backgrounds-korora.xml 		$(MATE_BG_DIR)/korora.xml
	$(INSTALL) mate-backgrounds-korora-animated.xml 		$(MATE_BG_DIR)/korora-animated.xml

	$(MKDIR) $(XFCE_BG_DIR)
	$(LN_S) ../../backgrounds/korora/default/wide/korora.png \
			$(XFCE_BG_DIR)/korora.png
