"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var NavigationView = require('../base-nav');
var NavigationItemsCollection = require('../../collections/navigation-items');
var JST = require('../../templates');

Backbone.$ = $;

module.exports = Backbone.View.extend({

    manage: true,
    template: 'settings',

    // Describes the navigation of the site
    currentViews: {},
    navItems: [
		{
			id: 'overview',
			title: 'Account Overview'
		},
		{
			id: 'coin',
			title: 'Coin Addresses'
		}
    ],

    initialize: function () {
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
            extraClasses: ['nav-sidebar']
        });
        this.showView('#left-nav', NavView);

        this.$el.html(_.template(JST[this.template](), {
            _ : _
        }));
    }
});