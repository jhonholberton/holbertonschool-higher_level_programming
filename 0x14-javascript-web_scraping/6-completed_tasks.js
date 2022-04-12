#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.

const request = require('request');
const { argv } = require('process');

if (argv[2]) {
  const url = argv[2];
  const complet = {};
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    const usr = JSON.parse(body);
    usr.forEach(element => {
      if (element.userId in complet && element.completed === true) {
        ++complet[element.userId];
      } else {
        if (element.completed === true) {
          complet[element.userId] = 1;
        }
      }
    });
    console.log(complet);
  });
}
