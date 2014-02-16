"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var Rate = require('../models/rate');

Backbone.$ = $;

var RateCollection = Backbone.Collection.extend({

    // Reference to this collection's model.
    model: Rate,
    url: '/sim/rates',
});

module.exports = RateCollection;
