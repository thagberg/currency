"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');

Backbone.$ = $;

module.exports = Backbone.Model.extend({
    // Default attributes for the todo
    // and ensure that each todo created has `title` and `completed` keys.
    defaults: {
        title: '',
        completed: false
    },

    url: ''
});
