#!/usr/bin/node

header = document.querySelector('header');
red_header = document.getElementById('red_header')

document.addEventListener('DOMContentLoaded', function () {
  red_header.addEventListener('click', function () {
    header.classList.add('red');
  });
});
