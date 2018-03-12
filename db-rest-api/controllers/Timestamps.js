'use strict';

var url = require('url');

var Timestamps = require('./TimestampsService');

module.exports.listTimestampsInOrder = function listTimestampsInOrder (req, res, next) {
  Timestamps.listTimestampsInOrder(req.swagger.params, res, next);
};
