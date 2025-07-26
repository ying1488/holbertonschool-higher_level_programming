#!/usr/bin/node

red_header = document.getElementById('red_header');
header = document.querySelector('header');

red_header.addEventListener('click', function () {
  red_header.style.color = '#FF0000';
});