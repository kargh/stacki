# @copyright@
# Copyright (c) 2006 - 2019 Teradata
# All rights reserved. Stacki(r) v5.x stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

PKGROOT		= /opt/stack
ROLLROOT	= ../../../..
RPMFILE		= $(NAME)-$(VERSION)-1.noarch.rpm
DEPENDS.FILES	= $(RPMFILE)

include $(STACKBUILD)/etc/CCRules.mk

build:
	mkdir $(CURDIR)/tmp/
	(\
		FI=$(shell readlink -f $RPMFILE) ; \
		cd $(CURDIR)/tmp/ ; \
		rpm2cpio $(FI) | cpio --extract --unconditional --make-directories --verbose  ; \
	)

install::
	mkdir -p $(ROOT)/$(PKGROOT)/sbin
	$(INSTALL) -m755 \
		$(CURDIR)/tmp/opt/MegaRAID/storcli/storcli64 \
		$(ROOT)/$(PKGROOT)/sbin/storcli

clean::
	rm -rf tmp
