'use strict';

exports.addSnapshot = function(args, res, next) {
  /**
   * Add a snapshot to the database, existent snapshots for the same framework and same time cannot be updated.
   *
   * body Snapshot Snapshot object that needs to be added to the database.
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

exports.listSnapshots = function(args, res, next) {
  /**
   * List the metrics of the different frameworks belonging to the exact same timestamp.
   *
   * body TimestampObject A timestamp we are looking the metrics for.
   * returns List
   **/
  var examples = {};
  examples['application/json'] = [ {
  "frameworkId" : "aeiou",
  "metrics" : {
    "forks" : 6,
    "watchers" : 5,
    "contributors" : 0,
    "stars" : 1
  },
  "timestamp" : { }
} ];
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

