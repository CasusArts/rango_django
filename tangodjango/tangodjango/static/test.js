const fs = require('fs');

fs.readFile(process.env[2], 'utf8', (err, data) => {
  if (err) {
    throw err;
  }

  console.log(JSON.parse(data));

});
