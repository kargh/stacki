# @copyright@
# Copyright (c) 2006 - 2019 Teradata
# All rights reserved. Stacki(r) v5.x stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@

import stack.commands


class Plugin(stack.commands.Plugin):
    def provides(self):
        return "route"

    def requires(self):
        return ["network"]

    def run(self, section):
        self.owner.set_scope("global")
        self.owner.load_route(section)
