"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var NavigationView = require('../base-nav');
var NavigationItemsCollection = require('../../collections/navigation-items');
var TransferCollection = require('../../collections/transfers');
var JST = require('../../templates');

Backbone.$ = $;

module.exports = Backbone.View.extend({

    manage: true,
    template: 'dashboard',

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

        this.collection = new TransferCollection();
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
/*
            _this.$('#chart').highcharts({
                chart: {
                    type: 'area'
                },
                title: {
                    text: 'Historic and Estimated Worldwide Population Growth by Region'
                },
                subtitle: {
                    text: 'Source: Wikipedia.org'
                },
                xAxis: {
                    categories: ['1750', '1800', '1850', '1900', '1950', '1999', '2050'],
                    tickmarkPlacement: 'on',
                    title: {
                        enabled: false
                    }
                },
                yAxis: {
                    title: {
                        text: 'Billions'
                    },
                    labels: {
                        formatter: function() {
                            return this.value / 1000;
                        }
                    }
                },
                tooltip: {
                    shared: true,
                    valueSuffix: ' millions'
                },
                plotOptions: {
                    area: {
                        stacking: 'normal',
                        lineColor: '#666666',
                        lineWidth: 1,
                        marker: {
                            lineWidth: 1,
                            lineColor: '#666666'
                        }
                    }
                },
                series: [{
                    name: 'Asia',
                    data: [502, 635, 809, 947, 1402, 3634, 5268]
                }, {
                    name: 'Africa',
                    data: [106, 107, 111, 133, 221, 767, 1766]
                }, {
                    name: 'Europe',
                    data: [163, 203, 276, 408, 547, 729, 628]
                }, {
                    name: 'America',
                    data: [18, 31, 54, 156, 339, 818, 1201]
                }, {
                    name: 'Oceania',
                    data: [2, 2, 2, 6, 13, 30, 46]
                }]
            });
*/
        });
    }
});