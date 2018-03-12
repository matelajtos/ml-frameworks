'use strict';

var url = require('url');

var Snapshots = require('./SnapshotsService');

module.exports.addSnapshot = function addSnapshot (req, res, next) {
  Snapshots.addSnapshot(req.swagger.params, res, next);
};

module.exports.listSnapshots = function listSnapshots (req, res, next) {
  Snapshots.listSnapshots(req.swagger.params, res, next);
};
