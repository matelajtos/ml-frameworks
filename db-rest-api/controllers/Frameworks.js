'use strict';

var url = require('url');

var Frameworks = require('./FrameworksService');

module.exports.addOrUpdateFramework = function addOrUpdateFramework (req, res, next) {
  Frameworks.addOrUpdateFramework(req.swagger.params, res, next);
};

module.exports.getFrameworkById = function getFrameworkById (req, res, next) {
  Frameworks.getFrameworkById(req.swagger.params, res, next);
};
