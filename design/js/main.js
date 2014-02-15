"use strict";

var $ = require('jquery');
var _ = require('underscore');
var Backbone = require('backbone');
var AppView = require('./views/app');
var Workspace = require('./routers/router');

Backbone.$ = $;

// Extend Backbone Setup to add for_template
_.extend(Backbone.Model.prototype, {
    for_template: function () {
        return this.toJSON();
    }
});
_.extend(Backbone.Collection.prototype, {
    for_template: function (options) {
        return this.map(function (model) { return model.for_template(options); });
    }
});
_.extend(Backbone.View.prototype, {
    close: function (options) {
    }
});

// Initialize the application view
window.appView = new AppView({
    el: $('body')
});
window.appView.render();

// Initialize routing and start Backbone.history()
new Workspace();
Backbone.history.start();
