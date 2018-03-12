'use strict';

exports.addOrUpdateFramework = function(args, res, next) {
  /**
   * Add a new or update an existing framework in the database.
   *
   * body Framework Framework object that needs to be added to the database.
   * returns ApiResponse
   **/
  var examples = {};
  examples['application/json'] = {
  "code" : 8,
  "message" : "aeiou"
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.getFrameworkById = function(args, res, next) {
  /**
   * Find framework by ID
   * Returns a single framework
   *
   * frameworkId String ID of framework to return
   * returns Framework
   **/
  var examples = {};
  examples['application/json'] = {
  "frameworkId" : "aeiou",
  "name" : "aeiou",
  "description" : "aeiou",
  "url" : "aeiou"
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

