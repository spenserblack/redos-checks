#!/usr/bin/env node
const { catastrophes } = require("../redos.json");

catastrophes.forEach(({ regex, input }) => {
  const r = new RegExp(regex);
  r.exec(input);
});
