"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');

Backbone.$ = $;

var NavigationItems = Backbone.Collection.extend({

    initialize : function (models, options) {

        /**
          * If options is empty or missing the selectedChildId then
          * just prefill it with null
          */
        this.options = _.extend({}, {
            selectedChildId: null,
            showInNav: function (navigationItem) { return true; }
        }, options);

        _.each(models, function (navigationItem) {
            navigationItem.selected = (navigationItem.id === this.options.selectedChildId);
        }, this);
    },

    for_template: function (options) {
        var itemsForDisplay = this.filter(function (navigationItem) {
            return this.options.showInNav(navigationItem);
        }, this);

        return _.map(itemsForDisplay, function (model) {
            return model.for_template(options);
        });
    },

    /**
     * Set the currently selected nav item, if not id is passed then default to first child
     */
    setSelected : function (selectedChildId, options) {
        var model;

        // if not id is passed then default to first child
        selectedChildId = selectedChildId || this.models[0].id;
        options = options || {};

        this.each(function (navigationItem) {
            navigationItem.set({selected: false});
        });
        model = this.get(selectedChildId);

        if (!model) {
            return null;
        }

        model.set({selected: true});
        if (!options.silent) {
            this.trigger('selectedChange');
        }

        return model;
    },

    /**
     * Get the currently selected nav item, if none are selected then select the first child,
     * and return it.
     */
    getSelected : function () {
        var foundItem = this.find(function (navigationItem) {
            return navigationItem.get('selected');
        });

        // If no item was found the set the first child as selected and return it.
        if (!foundItem && this.length > 0) {
            this.setSelected();
            foundItem = this.getSelected();
        }

        return foundItem;
    },

    nextItem : function () {
        var foundItem = this.getSelected(),
            nextItemIndex = this.indexOf(foundItem),
            nextItem = this.at(nextItemIndex + 1) || false;

        if (nextItem) {
            this.setSelected(nextItem.get('id'));
        }

        return nextItem;
    }
});

module.exports = NavigationItems;
