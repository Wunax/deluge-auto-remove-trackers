# -*- coding: utf-8 -*-
# Copyright (C) 2022 Wunax <wunax@protonmail.com>
#
# Basic plugin template created by the Deluge Team.
#
# This file is part of AutoRemoveTrackers and is licensed under GNU GPL 3.0, or later,
# with the additional special exception to link portions of this program with
# the OpenSSL library. See LICENSE for more details.
from __future__ import unicode_literals

import logging

from deluge.core.rpcserver import export
from deluge.plugins.pluginbase import CorePluginBase
import deluge.component as component

log = logging.getLogger(__name__)

class Core(CorePluginBase):
    def enable(self):
        component.get("EventManager").register_event_handler("TorrentStateChangedEvent", self.on_torrent_state_changed)

    def disable(self):
        component.get("EventManager").deregister_event_handler("TorrentStateChangedEvent", self.on_torrent_state_changed)

    def update(self):
        pass

    def on_torrent_state_changed(self, torrent_id, state):
        try:
            if state == "Downloading":
                torrentmanager = component.get("TorrentManager")
                torrent = torrentmanager.torrents.get(torrent_id)
                torrent.set_trackers([])
        except:
            pass
