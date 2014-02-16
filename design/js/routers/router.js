"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var DashboardView = require('../views/dashboard');
var SettingView = require('../views/settings');
var RatesView = require('../views/rates');

Backbone.$ = $;

module.exports = Backbone.Router.extend({

    routes: {
        'dashboard' : 'showDashboard',
        'settings'  : 'showSettings',
        'rates'     : 'showRates',
    },

    showDashboard: function () {
        var view = new DashboardView({

        });
        window.appView.showView('#main-content', view);
    },

    showSettings: function () {
        var view = new SettingView({

        });
        window.appView.showView('#main-content', view);
    },

    showRates: function () {
        var view = new RatesView({

        });
        window.appView.showView('#main-content', view);
    }
});
