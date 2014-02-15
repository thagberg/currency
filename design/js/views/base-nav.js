"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var JST = require('../templates');

Backbone.$ = $;

module.exports = Backbone.View.extend({

    template: 'nav-list',

    initialize: function (options) {
        this.options = options;
    },

    serialize: function () {
        return {
            _            : _,
            baseURL      : this.options.baseURL,
            navItems     : this.collection.for_template(),
            templateVars : this.options.templateVars
        };
    },

    events: {
        'click a[data-id]' : 'updateSelected'
    },

    updateSelected: function (e) {
        e.preventDefault();
        e.stopPropagation();
        
        //can stop propagation by setting data-stopprop="yes" on target
        var stopprop = $(e.currentTarget).data('stopprop');
        if(stopprop !== undefined && stopprop === 'yes') {
            e.stopPropagation();
        }
        
        this.selectItem(e, $(e.currentTarget).data('id'));
    },
    
    // default implementation of selecting an item just calls complete
    selectItem: function(e, itemId) {
        this.completeItemSelection(e);
    },
    
    // actually selects the selected item
    completeItemSelection: function(e) {
        switch ($(e.currentTarget).data('navigate')) {
        case "trigger":
            Backbone.history.navigate($(e.currentTarget).attr('href'), {
                trigger: true
            });
            break;
        case "no-trigger":
            Backbone.history.navigate($(e.currentTarget).attr('href'));
            break;
        }

        this.collection.setSelected($(e.currentTarget).data('id'));
    },

    render: function () {
        this.$el.html(_.template(JST[this.template](), {
            _ : _,
            navItems: this.collection.for_template(),
            extraClasses: this.options.extraClasses || [],
            baseURL: this.options.baseURL
        }));
    }
});