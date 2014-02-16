"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var moment = require('moment');

Backbone.$ = $;

module.exports = Backbone.Model.extend({
    // Default attributes for the todo
    // and ensure that each todo created has `title` and `completed` keys.

    urlRoot: '/sim/rates',

    for_template: function () {
        var timeFormatted = moment(this.get('time')).format("dddd, MMMM Do YYYY, h:mm:ss a");
        return _.extend(this.toJSON(), {
            timeFormatted: timeFormatted
        });
    }
});
