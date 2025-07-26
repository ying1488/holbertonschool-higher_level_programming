#!/usr/bin/node

header = document.querySelector('header');
toggle_header = document.getElementById('toggle_header')

document.addEventListener('DOMContentLoaded', function () {
  toggle_header.addEventListener('click', function () {
    if(header.classList.contains ('red')){
      header.classList.remove('red');
      header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
  });
});
