"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var NavigationView = require('../base-nav');
var NavigationItemsCollection = require('../../collections/navigation-items');
var RatesCollection = require('../../collections/rates');
var JST = require('../../templates');

Backbone.$ = $;

module.exports = Backbone.View.extend({

    manage: true,
    template: 'rates',

    // Describes the navigation of the site
    currentViews: {},
    navItems: [
        {
            id: 'dashboard',
            title: 'Overview'
        },
        {
            id: 'activity',
            title: 'Activity'
        },
        {
            id: 'rates',
            title: 'Exchange Rates'
        },
        {
            id: 'transactions',
            title: 'Export Transactions'
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
        var _this = this;

        this.collection = new RatesCollection();
        this.collection.fetch().then(function () {
            var NavView = new NavigationView({
                collection: _this.navCollection,
                extraClasses: ['nav-sidebar']
            });
            _this.showView('#left-nav', NavView);

            _this.$el.html(_.template(JST[_this.template](), {
                _ : _,
                transfers: _this.collection.for_template()
            }));
        });
    }
});