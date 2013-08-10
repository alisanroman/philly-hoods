var db = require('../lib/db');

exports.get = function (req, res) {

  var editedName = req.params.name.toUpperCase();
  var editedName = editedName.replace(' ', '_');
  db.fromName(editedName, function (err, result) {
    if (err) {
      res.json(500, {error: 'Error attempting to get neighborhood: ' + err});
    } else {
      res.json(200, {request: { neighborhood: req.params.name }, results: result});
    }

  });
};