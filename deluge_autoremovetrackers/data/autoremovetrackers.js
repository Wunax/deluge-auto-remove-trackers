/**
 * Script: autoremovetrackers.js
 *     The client-side javascript code for the AutoRemoveTrackers plugin.
 *
 * Copyright:
 *     (C) Wunax 2022 <wunax@protonmail.com>
 *
 *     This file is part of AutoRemoveTrackers and is licensed under GNU GPL 3.0, or
 *     later, with the additional special exception to link portions of this
 *     program with the OpenSSL library. See LICENSE for more details.
 */

AutoRemoveTrackersPlugin = Ext.extend(Deluge.Plugin, {
    constructor: function(config) {
        config = Ext.apply({
            name: 'AutoRemoveTrackers'
        }, config);
        AutoRemoveTrackersPlugin.superclass.constructor.call(this, config);
    },

    onDisable: function() {
        deluge.preferences.removePage(this.prefsPage);
    },

    onEnable: function() {
        this.prefsPage = deluge.preferences.addPage(
            new Deluge.ux.preferences.AutoRemoveTrackersPage());
    }
});
new AutoRemoveTrackersPlugin();
