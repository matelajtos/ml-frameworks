'use strict';

exports.listTimestampsInOrder = function(args, res, next) {
  /**
   * List all the timestamps in chronological ascending order. Timestamps are populated automatically by the /snapshots PUT API.
   *
   * returns List
   **/
  var examples = {};
  examples['application/json'] = [ {
  "timestamp" : { }
} ];
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

