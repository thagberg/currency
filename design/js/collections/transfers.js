"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var Transfer = require('../models/transfer');

Backbone.$ = $;

var TransferCollection = Backbone.Collection.extend({

    // Reference to this collection's model.
    model: Transfer,
    url: '/sim/transfers',

    getByUserId: function (userId) {
        return this.filter(function (transaction) {
            if (transation.get('fields').destination_exchanger === 'userId' ||
                transation.get('fields').source_exchanger === 'userId' ) {
                return true;
            }
        });
    }
});

module.exports = TransferCollection;
