var JST = {};JST["coins"] = function anonymous(it) {
var out='<h1 class="page-header">Coin Addresses</h1><div class=""></div>';return out;
};
JST["dashboard"] = function anonymous(it) {
var out='<h1 class="page-header">Dashboard</h1><div class="table-responsive"> <div class="col-md-12" id="chart"></div> <table class="table table-striped"> <thead> <tr> <th>Transfer Number</th> <th>Currency</th> <th>Seller</th> <th>Buyer</th> <th>Date</th> </tr> </thead> <tbody> <% _.each(transfers, function(transfer) { %> <tr> <td><%= transfer.pk %></td> <td><%= transfer.fields.currency %></td> <td><%= transfer.fields.source_exchanger %></td> <td><%= transfer.fields.destination_exchanger %></td> <td><%= transfer.timeFormatted %></td> </tr> <% }); %> </tbody> </table></div>';return out;
};
JST["nav-list"] = function anonymous(it) {
var out='<ul class="nav<% _.each(extraClasses, function (klass) { %> <%= klass %><% }); %>"><% _.each(navItems, function (item) { %><li class="<% if (item.selected) { %>active<% } %>"><a href="#<%= baseURL %>/<%= item.id %>"><%= item.title %></a></li><% }); %></ul>';return out;
};
JST["settings"] = function anonymous(it) {
var out='';return out;
};module.exports = JST;