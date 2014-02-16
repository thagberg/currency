"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var User = require('../models/user');

Backbone.$ = $;

var UserCollection = Backbone.Collection.extend({

    // Reference to this collection's model.
    model: User,
    url: '/sim/users/1'
});

module.exports = UserCollection;
