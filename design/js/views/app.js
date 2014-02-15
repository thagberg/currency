"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var NavigationView = require('./base-nav');
var NavigationItemsCollection = require('../collections/navigation-items');
var JST = require('../templates');

Backbone.$ = $;

module.exports = Backbone.View.extend({

    // Instead of generating a new element, bind to the existing skeleton of
    // the App already present in the HTML.
    el: '#currency-app',

    // Describes the navigation of the site
    currentViews: {},
    navItems: [
        {
            id: 'dashboard',
            title: 'Dashboard',
        },
        {
            id: 'settings',
            title: 'Settings'
        },
        {
            id: 'help',
            title: 'Help'
        }
    ],

    initialize: function (options) {
        this.navCollection = new NavigationItemsCollection(this.navItems);
    },

    showView: function (selector, view) {
        if (this.currentViews[selector]) {
            this.currentViews[selector].close();
        }

        this.currentViews[selector] = view;
        $(selector).empty().append(this.currentViews[selector].el);
        this.currentViews[selector].render();
    },

    render: function () {
        var NavView = new NavigationView({
            collection: this.navCollection,
            extraClasses: ['navbar-nav', 'navbar-right']
        });
        this.showView('#top-nav', NavView);
    }
});